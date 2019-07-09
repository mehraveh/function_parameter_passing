import re
import sys


class Token(object):
    """ A simple Token structure.
        Contains the token type, value and position.
    """
    def __init__(self, type, val):
        self.type = type
        self.val = val
        # self.pos = pos
        # self.line = line

    def __str__(self):
        return '%s %s' % (self.type, self.val)

class LexerError(Exception):
    """ Lexer error exception.
        pos:
            Position in the input line where the error occurred.
    """
    def __init__(self, pos, line):
        self.pos = pos
        self.line = line

class Lexer(object):

    def __init__(self, rules, skip_whitespace=True):
        idx = 1
        regex_parts = []
        self.group_type = {}

        for regex, type in rules:
            groupname = 'GROUP%s' % idx
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type
            idx += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('[^ \t\r\f]')

    def input(self, buf):
        self.buf = buf
        self.pos = 0
        self.line = 1
        self.end_of_last_n = 0

    def token(self):
        if self.pos >= len(self.buf):
            return None

        else:
            if self.skip_whitespace:
                m = self.re_ws_skip.search(self.buf, self.pos)
                if m:
                    self.pos = m.start()

                else:
                    return None
            m = self.regex.match(self.buf, self.pos)
            if m:
                groupname = m.lastgroup
                if m.group() == "\n":
                    tok = 1
                    self.line += 1
                    self.pos = m.end()
                    self.end_of_last_n = self.pos
                    return tok
                else:
                    tok_type = self.group_type[groupname]
                    if self.end_of_last_n != 0:
                        start = self.pos - self.end_of_last_n
                    else:
                        start = self.pos
                    tok = Token(tok_type, m.group(groupname))
                    self.pos = m.end()
                    return tok
            # if we're here, no rule matched
            raise LexerError(self.pos, self.line)

    def tokens(self):
        while(1):
            tok = self.token()
            if tok is None: break
            if tok != 1:
                yield tok


if __name__ == '__main__':
    rules = [
        ('def',                                                's_func'),
        ('[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?',             's_num'),
        ('#define',         's_def'),
        ('[a-zA-Z_]\w*',    's_id'),
        ('\\n',             's_newLine'),
        ('\:',              's_colon'),
        ('\;',              's_semicolon'),
        ('\+',              's_plus'),
        ('\|',              's_or'),
        ('\<\=',            's_le'),
        ('\>\=',            's_ge'),
        ('\<',              's_lt'),
        ('\>',              's_gt'),
        ('\<\>',            's_ne'),
        ('\,',              's_comma'),
        ('\(',              's_openpar'),
        ('\)',              's_closepar'),
        ('\[',              's_openbr'),
        ('\]',              's_closebr'),
        ('\{',              's_openac'),
        ('\}',              's_closeac'),
        ('\*\*',            's_pow'),
        ('\-',              's_minus'),
        ('\*',              's_mul'),
        ('\/',              's_div'),
        ('\(',              's_openpar'),
        ('\)',              's_closepar'),
        ('==',              's_eq'),
        ('!=',              's_noteq'),
        ('=',               's_assign'),
        ('\#([^\n])*',        's_singleLineComment'),
        ('\"\"\"([^\"]|\\"|\"([^\"]|\\.)|\"\"([^\"]|\\"))*\"\"\"|'
         '\'\'\'([^\']|\\\'|\'([^\']|\\\')|\'\'([^\']|\\\'))*\'\'\'',
         's_com'),
        ('\"([^\"])*\"|\'([^\'])*\'',                  's_string'),
    ]
    lx = Lexer(rules, skip_whitespace=True)
    file = open(sys.argv[1], "r")
    result = open("result.txt", "w")
    line1 = ''
    for line in file:
        result.write('*')
        result.write('\n')
        # line1 += line
        lx.input(line)
        try:
            for tok in lx.tokens():
                result.write(str(tok))
                result.write("\n")
        except LexerError as err:
            print('LexerError at position %s' % err.pos)

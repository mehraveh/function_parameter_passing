
import math
import random


file = open('back.cpp', 'w')
lex_file = open('result.txt', 'r')
file.write('#include <iostream> \n')
file.write('#include <fstream> \n\n')
file.write('using namespace std; \n')
mode = 4
if mode == 1: #pass by val
    map_words = {
        'def': 'void',
                }
    line = 1
    cr_line = []
    count = 0
    tab = 0
    func_names = []
    params_count = []
    pr_count = -1
    params = []
    for x in lex_file:
        if 's' in x:
            if not cr_line:
                for i in range(tab):
                    file.write('    ')
            cr_line.append(x.split(' ')[0])
            s = x.split(' ')[1].replace('\n','')
            s = s.strip()
            if 's_func' in cr_line:
                if x.split(' ')[0] == 's_id' and  not count is 1:
                    params.append(s)
                    s = 'double ' + s
                    params_count[pr_count] += 1
                if x.split(' ')[0] == 's_id' and count is 1:
                    func_names.append(s)
                    params_count.append(0)
                    pr_count += 1
            if s in map_words.keys():
                s = map_words[s]
            if x.split(' ')[0] =='s_openac':
                tab += 1
            if x.split(' ')[0] =='s_closeac':
                tab -= 1
                for param in params:
                    if not param is params[0]:
                        file.write('    ') 
                    file.write('cout<< ' + param + " << endl; \n")
                    file.write('    cout<< &' + param + " << endl; \n")
                params = []
            file.write(s + ' ')
            count +=1
        if not 's' in x and line > 0:
            if 's_assign' in cr_line:
                file.write(';')
            file.write('\n')
            line +=1
            cr_line = []
            count = 0
            #pr_count = 0

    file.write('int main()\n{ \n')
    mx = max(params_count)
    file.write('    cout << "parameters addresses" << endl;\n')
    for i in range(mx):
        file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
        file.write('    cout << &x' + i.__str__() +  ' << endl;\n')
    for j in range(len(func_names)):
        file.write( '    ' + func_names[j] + '(')
        for i in range(params_count[j]):
            if i + 1 == params_count[j]:
                file.write('x'+i.__str__())
            else:
                file.write('x'+i.__str__() + ' ,')
        file.write(');\n')
    mx = max(params_count)
    for i in range(mx):
        file.write('    cout << x' + i.__str__() +  ' << endl;\n')
    file.write('} \n')

if mode == 2: #pass by ref
    map_words = {
        'def': 'void',
                }
    line = 1
    cr_line = []
    count = 0
    tab = 0
    func_names = []
    params_count = []
    pr_count = -1
    params = []
    for x in lex_file:
        if 's' in x:
            if not cr_line:
                for i in range(tab):
                    file.write('    ')
            cr_line.append(x.split(' ')[0])
            s = x.split(' ')[1].replace('\n','')
            s = s.strip()
            if 's_func' in cr_line:
                if x.split(' ')[0] == 's_id' and  not count is 1:
                    params.append(s)
                    s = 'double &' + s
                    params_count[pr_count] += 1
                if x.split(' ')[0] == 's_id' and count is 1:
                    func_names.append(s)
                    params_count.append(0)
                    pr_count += 1
            if s in map_words.keys():
                s = map_words[s]
            if x.split(' ')[0] =='s_openac':
                tab += 1
            if x.split(' ')[0] =='s_closeac':
                tab -= 1
                for param in params:
                    if not param is params[0]:
                        file.write('    ') 
                    file.write('cout<< ' + param + " << endl; \n")
                    file.write('    cout<< &' + param + " << endl; \n")
                params = []
            file.write(s + ' ')
            count +=1
        if not 's' in x and line > 0:
            if 's_assign' in cr_line:
                file.write(';')
            file.write('\n')
            line +=1
            cr_line = []
            count = 0
            #pr_count = 0

    file.write('int main()\n{ \n')
    mx = max(params_count)
    file.write('    cout << "parameters addresses" << endl;\n')
    for i in range(mx):
        file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
        file.write('    cout << &x' + i.__str__() +  ' << endl;\n')
    for j in range(len(func_names)):
        file.write( '    ' + func_names[j] + '(')
        for i in range(params_count[j]):
            if i + 1 == params_count[j]:
                file.write('x'+i.__str__())
            else:
                file.write('x'+i.__str__() + ' ,')
        file.write(');\n')
    mx = max(params_count)
    for i in range(mx):
        file.write('    cout << x' + i.__str__() +  ' << endl;\n')
    file.write('} \n')
if mode == 3: #pass by pointer
    map_words = {
        'def': 'void',
                }
    line = 1
    cr_line = []
    count = 0
    tab = 0
    func_names = []
    params_count = []
    pr_count = -1
    params = []
    for x in lex_file:
        if 's' in x:
            if not cr_line:
                for i in range(tab):
                    file.write('    ')
            cr_line.append(x.split(' ')[0])
            s = x.split(' ')[1].replace('\n','')
            s = s.strip()
            if 's_func' in cr_line:
                if x.split(' ')[0] == 's_id' and  not count is 1:
                    params.append(s)
                    s = 'double *' + s
                    params_count[pr_count] += 1
                if x.split(' ')[0] == 's_id' and count is 1:
                    func_names.append(s)
                    params_count.append(0)
                    pr_count += 1
            else:
                if x.split(' ')[0] == 's_id' and not count is 1:
                    s = '*' + s
            if s in map_words.keys():
                s = map_words[s]
            if x.split(' ')[0] =='s_openac':
                tab += 1
            if x.split(' ')[0] =='s_closeac':
                tab -= 1
                for param in params:
                    if not param is params[0]:
                        file.write('    ') 
                    file.write('cout<< *' + param + " << endl; \n")
                    file.write('    cout<< ' + param + " << endl; \n")
                params = []
            file.write(s + ' ')
            count +=1
        if not 's' in x and line > 0:
            if 's_assign' in cr_line:
                file.write(';')
            file.write('\n')
            line +=1
            cr_line = []
            count = 0
            #pr_count = 0

    file.write('int main()\n{ \n')
    mx = max(params_count)
    file.write('    cout << "parameters addresses" << endl;\n')
    for i in range(mx):
        file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
        file.write('    cout << &x' + i.__str__() +  ' << endl;\n')
    for j in range(len(func_names)):
        file.write( '    ' + func_names[j] + '(')
        for i in range(params_count[j]):
            if i + 1 == params_count[j]:
                file.write('&x'+i.__str__())
            else:
                file.write('&x'+i.__str__() + ' ,')
        file.write(');\n')
    mx = max(params_count)
    for i in range(mx):
        file.write('    cout << x' + i.__str__() +  ' << endl;\n')
    file.write('} \n')

if mode == 4: #pass by name
    map_words = {
        'def': '#define ',
                }
    line = 1
    cr_line = []
    count = 0
    tab = 0
    func_names = []
    params_count = []
    pr_count = -1
    params = []
    s = ''
    for x in lex_file:
        if 's' in x:
            cr_line.append(x.split(' ')[0])
            s = x.split(' ')[1].replace('\n','')
            s = s.strip()
            if 's_func' in cr_line:
                if count is 0:
                    file.write('\n')
                if x.split(' ')[0] == 's_id' and not count is 1:
                    params.append(s)
                    params_count[pr_count] += 1
                if x.split(' ')[0] == 's_id' and count is 1:
                    func_names.append(s)
                    params_count.append(0)
                    pr_count += 1
            if s in map_words.keys():
                s = map_words[s]
            sp = x.split(' ')[0]
            if sp !='s_openac' and sp !='s_closeac' and sp != 's_assign' and not (count == 0 and sp == 's_id'):
                file.write(s)
        count +=1
        if not 's' in x and line > 0:
            line +=1
            cr_line = []
            count = 0
    mx = max(params_count)
    for i in range(mx):
        file.write('\ndouble x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';')
    #file.write('    cout << "parameters addresses" << endl;\n')
    file.write('\nint main()\n{ \n')
    for i in range(mx):
        #file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
        file.write('    cout << x' + i.__str__() +  ' << endl;\n')
    for j in range(len(func_names)):
        file.write( '    cout<< ' + func_names[j] + '(')
        for i in range(params_count[j]):
            if i + 1 == params_count[j]:
                file.write('x'+i.__str__())
            else:
                file.write('x'+i.__str__() + ' ,')
        file.write(') <<endl;\n')
    mx = max(params_count)
    for i in range(mx):
        file.write('    cout << x' + i.__str__() +  ' << endl;\n')
    file.write('} \n')

if mode == 5: #pass by val res
    map_words = {
        'def': 'void',
                }
    line = 1
    cr_line = []
    count = 0
    tab = 0
    func_names = []
    params_count = []
    pr_count = -1
    params = []
    for x in lex_file:
        if 's' in x:
            if not cr_line:
                for i in range(tab):
                    file.write('    ')
            cr_line.append(x.split(' ')[0])
            s = x.split(' ')[1].replace('\n','')
            s = s.strip()
            if 's_func' in cr_line:
                if x.split(' ')[0] == 's_id' and  not count is 1:
                    params.append(s)
                    s = 'double &' + s
                    params_count[pr_count] += 1
                if x.split(' ')[0] == 's_id' and count is 1:
                    func_names.append(s)
                    params_count.append(0)
                    pr_count += 1
            if s in map_words.keys():
                s = map_words[s]
            if x.split(' ')[0] =='s_openac':
                tab += 1
            if x.split(' ')[0] =='s_closeac':
                tab -= 1
                for param in params:
                    if not param is params[0]:
                        file.write('    ') 
                    file.write('cout<< ' + param + " << endl; \n")
                    file.write('    cout<< &' + param + " << endl; \n")
                params = []
            file.write(s + ' ')
            count +=1
        if not 's' in x and line > 0:
            if 's_assign' in cr_line:
                file.write(';')
            file.write('\n')
            line +=1
            cr_line = []
            count = 0
            #pr_count = 0

    file.write('int main()\n{ \n')
    mx = max(params_count)
    file.write('    cout << "parameters addresses" << endl;\n')
    for i in range(mx):
        file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
        file.write('    double temp' + i.__str__() + " = x"+  i.__str__() + ';\n')
        file.write('    cout << &x' + i.__str__() +  ' << endl;\n')
        file.write('    cout << x' + i.__str__() +  ' << endl;\n')
    for j in range(len(func_names)):
        file.write( '    ' + func_names[j] + '(')
        for i in range(params_count[j]):
            if i + 1 == params_count[j]:
                file.write('temp'+i.__str__())
            else:
                file.write('temp'+i.__str__() + ' ,')
        file.write(');\n')
    mx = max(params_count)
    for i in range(mx):
        file.write('    x' + i.__str__() + " = temp" + i.__str__() + ';\n')
        file.write('    cout << &x' + i.__str__() +  ' << endl;\n')
        file.write('    cout << x' + i.__str__() +  ' << endl;\n')
    file.write('} \n')
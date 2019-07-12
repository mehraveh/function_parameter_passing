
import sys
import random

main_str = ''
file = open('back.cpp', 'w')
lex_file = open('result.txt', 'r')
main_str += '#include <iostream> \n'
main_str += '#include <fstream> \n\n'
main_str += 'using namespace std; \n'
#file.write('double globl' + " = " + random.randint(0,10).__str__() + ';\n')
mode = sys.argv[1]
is_glob = sys.argv[2]
mode = int(mode)
is_glob = int(is_glob)
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
    globals_arr = []
    for x in lex_file:
        if 's' in x:
            if not cr_line:
                for i in range(tab):
                    main_str += '    '
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
            elif not 's_func' in cr_line and tab == 0:
                if x.split(' ')[0] == 's_id' and count == 0:
                    globals_arr.append(s)
                    s = 'double ' + s
            if s in map_words.keys():
                s = map_words[s]
            if x.split(' ')[0] =='s_openac':
                tab += 1
            if x.split(' ')[0] =='s_closeac':
                tab -= 1
                main_str += 'cout<< ' + '"in functions function parameters"' + " << endl; \n"
                for param in params:
                    if not param is params[0]:
                        main_str +='    '
                    main_str +='    cout<< ' +'" value of ' + param  + ' : " <<' + param + " << endl; \n"
                    main_str +='    cout<< ' +'" address of ' + param + ' :" << &' + param + " << endl; \n"
                params = []
                main_str += '    cout<< ' + '"in functions global parameters"' + " << endl; \n"
                for glb in globals_arr:
                    main_str +='    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n"
                    main_str +='    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n"
            main_str += (s + ' ')
            count +=1

                #file.write("\n    globl =  globl + " + random.randint(0,10).__str__() + ';')
        if not 's' in x and line > 0:
            if 's_assign' in cr_line:
                main_str +=';'
            main_str +='\n'
            line +=1
            cr_line = []
            count = 0
            #pr_count = 0
    file.write(main_str)

    file.write('int main()\n{ \n')
    file.write('cout<< ' + '"************pass by value*****************"' + " << endl; \n")
    mx = max(params_count)
    file.write('    cout << "before calling function :" << endl;\n')
    for i in range(mx):
        file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
        file.write('    cout << " value of x' + i.__str__() + ' : "  << x' + i.__str__() +  ' << endl;\n')
        file.write('    cout << " address  of x' + i.__str__() + ' :" << &x' + i.__str__() +  ' << endl;\n')
    for glb in globals_arr:
        file.write('    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n")
        file.write('    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n")
    for j in range(len(func_names)):
        file.write( '    ' + func_names[j] + '(')
        if is_glob == 0:
            for i in range(params_count[j]):
                if i + 1 == params_count[j]:
                    file.write('x'+i.__str__())
                else:
                    file.write('x'+i.__str__() + ' ,')
        else:
            for j in range(len(globals_arr)):
                if i + 1 == len(globals_arr):
                    file.write(globals_arr[i])
                else:
                    file.write(globals_arr[i]+ ' ,')
        file.write(');\n')
    mx = max(params_count)
    file.write('    cout << "after calling function :" << endl;\n')
    for i in range(mx):
        file.write('    cout << " value of x' + i.__str__() + ' : " << x' + i.__str__() +  ' << endl;\n')
        file.write('    cout << " address  of x' + i.__str__() + ' : " << &x' + i.__str__() +  ' << endl;\n')
    for glb in globals_arr:
        file.write('    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n")
        file.write('    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n")
    file.write('} \n')

if mode == 2 or mode == 4: #pass by ref
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
    globals_arr = []
    for x in lex_file:
        if 's' in x:
            if not cr_line:
                for i in range(tab):
                    main_str += '    '
            cr_line.append(x.split(' ')[0])
            s = x.split(' ')[1].replace('\n','')
            s = s.strip()
            if 's_func' in cr_line:
                if mode == 4  and len(globals_arr ) == 0:
                    print("must have global var\n\n\n\n\n\n")
                    exit()
                if x.split(' ')[0] == 's_id' and  not count is 1:
                    params.append(s)
                    s = 'double &' + s
                    params_count[pr_count] += 1
                if x.split(' ')[0] == 's_id' and count is 1:
                    func_names.append(s)
                    params_count.append(0)
                    pr_count += 1
            elif not 's_func' in cr_line and tab == 0:
                if x.split(' ')[0] == 's_id' and count == 0:
                    globals_arr.append(s)
                    s = 'double ' + s
            if s in map_words.keys():
                s = map_words[s]
            if x.split(' ')[0] =='s_openac':
                tab += 1
            if x.split(' ')[0] =='s_closeac':
                tab -= 1
                main_str += 'cout<< ' + '"in functions function parameters"' + " << endl; \n"
                for param in params:
                    if not param is params[0]:
                        main_str +='    '
                    main_str +='    cout<< ' +'" value of ' + param  + ' : " <<' + param + " << endl; \n"
                    main_str +='    cout<< ' +'" address of ' + param + ' :" << &' + param + " << endl; \n"
                params = []
                main_str += '    cout<< ' + '"in functions global parameters"' + " << endl; \n"
                for glb in globals_arr:
                    main_str +='    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n"
                    main_str +='    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n"
            main_str += (s + ' ')
            count +=1
                #file.write("\n    globl =  globl + " + random.randint(0,10).__str__() + ';')
        if not 's' in x and line > 0:
            if 's_assign' in cr_line:
                main_str +=';'
            main_str +='\n'
            line +=1
            cr_line = []
            count = 0
            #pr_count = 0
    file.write(main_str)

    file.write('int main()\n{ \n')
    if mode == 2:
        file.write('cout<< ' + '"************pass by reference*****************"' + " << endl; \n")
    else:
        file.write('cout<< ' + '"************pass by result*****************"' + " << endl; \n")        
    mx = max(params_count)
    file.write('    cout << "before calling function :" << endl;\n')
    for i in range(mx):
        file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
        file.write('    cout << " value of x' + i.__str__() + ' : "  << x' + i.__str__() +  ' << endl;\n')
        file.write('    cout << " address  of x' + i.__str__() + ' :" << &x' + i.__str__() +  ' << endl;\n')
    for glb in globals_arr:
        file.write('    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n")
        file.write('    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n")
    for j in range(len(func_names)):
        file.write( '    ' + func_names[j] + '(')
        if is_glob == 0:
            for i in range(params_count[j]):
                if i + 1 == params_count[j]:
                    file.write('x'+i.__str__())
                else:
                    file.write('x'+i.__str__() + ' ,')
        else:
            for j in range(len(globals_arr)):
                if i + 1 == len(globals_arr):
                    file.write(globals_arr[i])
                else:
                    file.write(globals_arr[i]+ ' ,')
        file.write(');\n')
    mx = max(params_count)
    file.write('    cout << "after calling function :" << endl;\n')
    for i in range(mx):
        file.write('    cout << " value of x' + i.__str__() + ' : " << x' + i.__str__() +  ' << endl;\n')
        file.write('    cout << " address  of x' + i.__str__() + ' : " << &x' + i.__str__() +  ' << endl;\n')
    for glb in globals_arr:
        file.write('    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n")
        file.write('    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n")
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
    globals_arr = []
    for x in lex_file:
        if 's' in x:
            if not cr_line:
                for i in range(tab):
                    main_str += '    '
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
            elif not 's_func' in cr_line and tab == 0:
                if x.split(' ')[0] == 's_id' and count == 0:
                    globals_arr.append(s)
                    s = 'double ' + s
            elif x.split(' ')[0] == 's_id' and s not in globals_arr:
                s = '*' + s 
            if s in map_words.keys():
                s = map_words[s]
            if x.split(' ')[0] =='s_openac':
                tab += 1
            if x.split(' ')[0] =='s_closeac':
                tab -= 1
                main_str += 'cout<< ' + '"in functions function parameters"' + " << endl; \n"
                for param in params:
                    if not param is params[0]:
                        main_str +='    '
                    main_str +='    cout<< ' +'" value of ' + param  + ' : " << *' + param + " << endl; \n"
                    main_str +='    cout<< ' +'" address of ' + param + ' :" << ' + param + " << endl; \n"
                params = []
                main_str += '    cout<< ' + '"in functions global parameters"' + " << endl; \n"
                for glb in globals_arr:
                    main_str +='    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n"
                    main_str +='    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n"
            main_str += (s + ' ')
            count +=1
                #file.write("\n    globl =  globl + " + random.randint(0,10).__str__() + ';')
        if not 's' in x and line > 0:
            if 's_assign' in cr_line:
                main_str +=';'
            main_str +='\n'
            line +=1
            cr_line = []
            count = 0
            #pr_count = 0
    file.write(main_str)

    file.write('int main()\n{ \n')
    file.write('cout<< ' + '"************pass by pointer*****************"' + " << endl; \n")
    mx = max(params_count)
    file.write('    cout << "before calling function :" << endl;\n')
    for i in range(mx):
        file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
        file.write('    cout << " value of x' + i.__str__() + ' : "  << x' + i.__str__() +  ' << endl;\n')
        file.write('    cout << " address  of x' + i.__str__() + ' :" << &x' + i.__str__() +  ' << endl;\n')
    for glb in globals_arr:
        file.write('    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n")
        file.write('    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n")
    for j in range(len(func_names)):
        file.write( '    ' + func_names[j] + '(')
        if is_glob == 0:
            for i in range(params_count[j]):
                if i + 1 == params_count[j]:
                    file.write('&x'+i.__str__())
                else:
                    file.write('&x'+i.__str__() + ' ,')
        else:
            for j in range(len(globals_arr)):
                if i + 1 == len(globals_arr):
                    file.write('&' + globals_arr[i])
                else:
                    file.write('&' + globals_arr[i]+ ' ,')
        file.write(');\n')
    mx = max(params_count)
    file.write('    cout << "after calling function :" << endl;\n')
    for i in range(mx):
        file.write('    cout << " value of x' + i.__str__() + ' : " << x' + i.__str__() +  ' << endl;\n')
        file.write('    cout << " address  of x' + i.__str__() + ' : " << &x' + i.__str__() +  ' << endl;\n')
    for glb in globals_arr:
        file.write('    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n")
        file.write('    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n")
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
    globals_arr = []
    for x in lex_file:
        if 's' in x:
            if not cr_line:
                for i in range(tab):
                    main_str += '    '
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
            elif not 's_func' in cr_line and tab == 0:
                if x.split(' ')[0] == 's_id' and count == 0:
                    globals_arr.append(s)
                    s = 'double ' + s
            if s in map_words.keys():
                s = map_words[s]
            if x.split(' ')[0] =='s_openac':
                tab += 1
            if x.split(' ')[0] =='s_closeac':
                tab -= 1
                main_str += 'cout<< ' + '"in functions function parameters"' + " << endl; \n"
                for param in params:
                    if not param is params[0]:
                        main_str +='    '
                    main_str +='    cout<< ' +'" value of ' + param  + ' : " <<' + param + " << endl; \n"
                    main_str +='    cout<< ' +'" address of ' + param + ' :" << &' + param + " << endl; \n"
                params = []
                main_str += '    cout<< ' + '"in functions global parameters"' + " << endl; \n"
                for glb in globals_arr:
                    main_str +='    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n"
                    main_str +='    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n"
            main_str += (s + ' ')
            count +=1

                #file.write("\n    globl =  globl + " + random.randint(0,10).__str__() + ';')
        if not 's' in x and line > 0:
            if 's_assign' in cr_line:
                main_str +=';'
            main_str +='\n'
            line +=1
            cr_line = []
            count = 0
            #pr_count = 0
    file.write(main_str)

    file.write('int main()\n{ \n')
    file.write('cout<< ' + '"************pass by value result*****************"' + " << endl; \n")
    mx = max(params_count)
    file.write('    cout << "before calling function :" << endl;\n')
    for i in range(mx):
        file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
        file.write('    cout << " value of x' + i.__str__() + ' : "  << x' + i.__str__() +  ' << endl;\n')
        file.write('    double temp' + i.__str__() + " = x"+  i.__str__() + ';\n')
        file.write('    cout << " address  of x' + i.__str__() + ' :" << &x' + i.__str__() +  ' << endl;\n')
    c = 0;
    for glb in globals_arr:
        file.write('    double _' +  c.__str__()+'temp' + " = " + glb + ';\n')
        file.write('    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n")
        file.write('    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n")
    for j in range(len(func_names)):
        file.write( '    ' + func_names[j] + '(')
        if is_glob == 0:
            for i in range(params_count[j]):
                if i + 1 == params_count[j]:
                    file.write('x'+i.__str__())
                else:
                    file.write('x'+i.__str__() + ' ,')
        else:
            for j in range(len(globals_arr)):
                if i + 1 == len(globals_arr):
                    file.write(globals_arr[i])
                else:
                    file.write(globals_arr[i]+ ' ,')
        file.write(');\n')
    mx = max(params_count)
    file.write('    cout << "after calling function :" << endl;\n')
    for i in range(mx):
        file.write('    x' + i.__str__() + " = temp" + i.__str__() + ';\n')
        file.write('    cout << " value of x' + i.__str__() + ' : " << x' + i.__str__() +  ' << endl;\n')
        file.write('    cout << " address  of x' + i.__str__() + ' : " << &x' + i.__str__() +  ' << endl;\n')
    c = 0;
    for glb in globals_arr:
        file.write('    ' +  glb + " =  _" + c.__str__() +"temp" + ';\n')
        file.write('    cout<< ' +'" value of ' + glb  + ' : " << ' + glb + " << endl; \n")
        file.write('    cout<< ' +'" address of ' + glb + ' :" << &' + glb + " << endl; \n")
        c += 1
    file.write('} \n')



# if mode == 4: #pass by name
#     map_words = {
#         'def': '#define ',
#                 }
#     line = 1
#     cr_line = []
#     count = 0
#     tab = 0
#     func_names = []
#     params_count = []
#     pr_count = -1
#     params = []
#     s = ''
#     for x in lex_file:
#         if 's' in x:
#             cr_line.append(x.split(' ')[0])
#             s = x.split(' ')[1].replace('\n','')
#             s = s.strip()
#             if 's_func' in cr_line:
#                 if count is 0:
#                     file.write('\n')
#                 if x.split(' ')[0] == 's_id' and not count is 1:
#                     params.append(s)
#                     params_count[pr_count] += 1
#                 if x.split(' ')[0] == 's_id' and count is 1:
#                     func_names.append(s)
#                     params_count.append(0)
#                     pr_count += 1
#             if s in map_words.keys():
#                 s = map_words[s]
#             sp = x.split(' ')[0]
#             if sp !='s_openac' and sp !='s_closeac' and sp != 's_assign' and not (count == 0 and sp == 's_id'):
#                 file.write(s)
#         count +=1
#         if not 's' in x and line > 0:
#             line +=1
#             cr_line = []
#             count = 0
#     mx = max(params_count)
#     for i in range(mx):
#         file.write('\ndouble x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';')
#     #file.write('    cout << "parameters addresses" << endl;\n')
#     file.write('\nint main()\n{ \n')
#     for i in range(mx):
#         #file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
#         file.write('    cout << x' + i.__str__() +  ' << endl;\n')
#     for j in range(len(func_names)):
#         file.write( '    cout<< ' + func_names[j] + '(')
#         for i in range(params_count[j]):
#             if i + 1 == params_count[j]:
#                 file.write('x'+i.__str__())
#             else:
#                 file.write('x'+i.__str__() + ' ,')
#         file.write(') <<endl;\n')
#     mx = max(params_count)
#     for i in range(mx):
#         file.write('    cout << x' + i.__str__() +  ' << endl;\n')
#     file.write('} \n')


























    # map_words = {
    #     'def': 'void',
    #             }
    # line = 1
    # cr_line = []
    # count = 0
    # tab = 0
    # func_names = []
    # params_count = []
    # pr_count = -1
    # params = []
    # for x in lex_file:
    #     if 's' in x:
    #         if not cr_line:
    #             for i in range(tab):
    #                 file.write('    ')
    #         cr_line.append(x.split(' ')[0])
    #         s = x.split(' ')[1].replace('\n','')
    #         s = s.strip()
    #         if 's_func' in cr_line:
    #             if x.split(' ')[0] == 's_id' and  not count is 1:
    #                 params.append(s)
    #                 s = 'double &' + s
    #                 params_count[pr_count] += 1
    #             if x.split(' ')[0] == 's_id' and count is 1:
    #                 func_names.append(s)
    #                 params_count.append(0)
    #                 pr_count += 1
    #         if s in map_words.keys():
    #             s = map_words[s]
    #         if x.split(' ')[0] =='s_openac':
    #             tab += 1
    #         if x.split(' ')[0] =='s_closeac':
    #             tab -= 1
    #             for param in params:
    #                 if not param is params[0]:
    #                     file.write('    ') 
    #                 file.write('cout<< ' + param + " << endl; \n")
    #                 file.write('    cout<< &' + param + " << endl; \n")
    #             params = []
    #         file.write(s + ' ')
    #         count +=1
    #     if not 's' in x and line > 0:
    #         if 's_assign' in cr_line:
    #             file.write(';')
    #         file.write('\n')
    #         line +=1
    #         cr_line = []
    #         count = 0
    #         #pr_count = 0

    # file.write('int main()\n{ \n')
    # mx = max(params_count)
    # file.write('    cout << "parameters addresses" << endl;\n')
    # for i in range(mx):
    #     file.write('    double x' + i.__str__() + " = " + random.randint(0,10).__str__() + ';\n')
    #     file.write('    double temp' + i.__str__() + " = x"+  i.__str__() + ';\n')
    #     file.write('    cout << &x' + i.__str__() +  ' << endl;\n')
    #     file.write('    cout << x' + i.__str__() +  ' << endl;\n')
    # for j in range(len(func_names)):
    #     file.write( '    ' + func_names[j] + '(')
    #     for i in range(params_count[j]):
    #         if i + 1 == params_count[j]:
    #             file.write('temp'+i.__str__())
    #         else:
    #             file.write('temp'+i.__str__() + ' ,')
    #     file.write(');\n')
    # mx = max(params_count)
    # for i in range(mx):
    #     file.write('    x' + i.__str__() + " = temp" + i.__str__() + ';\n')
    #     file.write('    cout << &x' + i.__str__() +  ' << endl;\n')
    #     file.write('    cout << x' + i.__str__() +  ' << endl;\n')
    # file.write('} \n')
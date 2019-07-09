import os
os.system('python3 ply.py python_code.txt')
os.system('python3 code_generating.py')
os.system('g++ back.cpp -o back')
os.system('./back')
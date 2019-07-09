import os
import sys
if __name__ == '__main__':

	os.system('python3 ply.py ' + sys.argv[1] )
	os.system('python3 code_generating.py ' + sys.argv[2])
	os.system('g++ back.cpp -o back')
	os.system('./back')
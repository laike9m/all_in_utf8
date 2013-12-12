'''
recursively find and convert gbk py, txt files to utf-8
use:
    python convert_to_utf8.py top_directory

will automatically list all modified files' name on the screen 
'''

import sys
import os
import chardet


class BaseInfo:
    
    file_type = ('.txt', '.py', '.cpp', '.c')
    
    def __init__(self, top_dir):
        self.top_dir = top_dir
        

class Convert(BaseInfo):
    
    'copy original files to ./copy folder'

    def __init__(self, top_dir):
        self.top_dir = top_dir
        if not os.path.exists('copy'):
            os.mkdir('copy')
            
    def get_file_list(self):
        for root, _, files in os.walk(self.top_dir):
            for file in files:
                if any(file.endswith(t) for t in self.file_type):
                    file = open(os.path.join(root, file), 'rb')
                    encoding = chardet.detect(file.read())['encoding']
                    if encoding:
                        print(os.path.split(file.name)[1] + ': ' + encoding)
                    else:
                        print(os.path.split(file.name)[1] + ' is none')

    def print_instance(self):
        print(str(self.__dict__))

    def print_all_attr(self):
        print(dir(self))

if __name__ == '__main__':
    #top_dir = sys.argv[1]
    t = Convert(r'C:\ZY\EverythingandNothing\Python\MyWork\Test_Py3.3')
    t.get_file_list()

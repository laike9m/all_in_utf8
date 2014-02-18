"""
recursively find and convert non-utf8 .py, .txt, .cpp, .c files to utf-8
use:
    python convert_to_utf8.py top_directory

will automatically list all modified files' name on the screen 
"""

import os
import sys
import chardet
from shutil import copy


class BaseInfo:
    
    file_type = ('.txt', '.py', '.cpp', '.c')
    
    def __init__(self, top_dir):
        self.top_dir = top_dir
        

class Convert(BaseInfo):
    """copy original files to ./copy folder"""
    def __init__(self, top_dir):
        self.top_dir = top_dir
        self.filelist = {}

    def get_file_list(self):
        for root, _, files in os.walk(self.top_dir):
            for file in files:
                if any(file.endswith(t) for t in self.file_type):
                    filename = os.path.join(root, file)
                    with open(filename, 'rb') as file:
                        encoding = chardet.detect(file.read())['encoding']
                        if encoding and encoding.lower() != 'utf-8':
                            self.filelist[filename] = encoding  # {filename:encoding}
                            print(os.path.split(file.name)[1] + ': ' + encoding)
    
    
    def make_copy(self):
        """copy those files that need to be modified"""
        os.chdir(self.top_dir)
        if not os.path.exists('../copy'):
            os.mkdir('../copy')
        os.chdir('../copy')
        
        for file in self.filelist.keys(): 
            filename = os.path.split(file)[1]
            if os.path.exists(filename):
                os.remove(filename)
            try:
                copy(file, '.')
            except IOError:
                print('you may not have permission to write')
    
    
    def re_encoding(self):
        for file, encoding in self.filelist.items():
            with open(file, 'rt', encoding=encoding) as f:
                content = f.read()
            os.remove(file)
            with open(file, 'wt', encoding='utf-8') as new_f:
                new_f.write(content)
    

    def print_instance(self):
        print(str(self.__dict__))


    def print_all_attr(self):
        print(dir(self))


if __name__ == '__main__':
    try:
        top_dir = sys.argv[1]
        t = Convert(top_dir)
    except IndexError:
        t = Convert('.')
    t.get_file_list()
    t.make_copy()
    t.re_encoding()

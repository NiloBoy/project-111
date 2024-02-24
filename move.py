import os
import shutil

from_dir="C:/Users/MY PC/Documents"
to_dir="C:/Users/MY PC/Downloads"
list_of_file=os.listdir(from_dir)
print(list_of_file)
for file_name in list_of_file:
    name,extention = os.path.splitext(file_name)
    print(name)
    print(extention)

    

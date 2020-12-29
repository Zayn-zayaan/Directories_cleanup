'''
This program will help u to manage u'r dirs.It accepts the path of folder which u want to clean up,
 a txt file which contains the file/folder names which u do not want to be rename and a file format so that file 
 present of that format will get rename as 1,2,3... , and it will capitalize the first letter of every file/folder
 which don't contain in txt file and doesn't have same file ext as given by u.
'''

import os

def cleanup(path, file, format):
    os.chdir(path)
    i=1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("/n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1

if __name__ == "__main__":
    a = ''
    print(r"Heyy buddy!! I am here to manage your directories. After the process u will find files/folders arrange in neat and clean order")
    while True:
        path = input("Enter the path of the directory which u want to cleanup: ")
        file_path = input("Enter the path of the txt file contain names of imp. files.")
        file_ext = input("Enter the file format.Files of that format will rename in numerical order as 1,2,3...")
        cleanup(path, file_path, file_ext)
        print("Done!!!!!!!!!!!")
        a = input("Want me run again?? Y/N: ")
        if a=="N" or a=="n":
            break
        else:
            continue

    print("See u later. bubbyee!!")


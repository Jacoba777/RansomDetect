from shutil import copyfile
import os


def add_class(foldername, classname, destfolder):
    index = 0
    dir = '.\\' + foldername

    for filename in os.listdir(dir):
        extention = filename.split('.')[-1]
        if extention == 'jfif' or extention == 'jpeg':
            extention = 'jpg'
        newfilename = classname + '-' + str(index).zfill(4) + '.' + extention
        index += 1

        source = dir + '\\' + filename
        dest = destfolder + '\\' + newfilename
        copyfile(source, dest)
    print('Added', index, classname, 'images to', destfolder)


add_class('input_class_benign', 'benign', 'input_data')
add_class('input_class_ransomware', 'ransomware', 'input_data')
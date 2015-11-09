# Information
__author__ = "Daniel Roland Henrik Jensen"
__copyright__ = "Copyright (C) 2015 Daniel Jensen"
__license__ = "Apache License 2.0, See the LICENSE file included"
__version__ = "1.0"

import os
from os.path import expanduser
import glob
import shutil

_home = expanduser("~")
print(_home)

home = _home+'/Desktop/'

print('Files in Desktop:\n')

for name in glob.glob(home + r'*.*'):
    print(name+"\n")

print("Directories in Desktop:\n")

for dir_ in glob.glob(home+r'*/'):
    print(dir_+"\n")

if not os.path.exists(home+'Text Dokuments'):
    os.makedirs(home+'Text Dokuments')

if not os.path.exists(home+'Programs'):
    os.makedirs(home+'Programs')

if not os.path.exists(home+'Images'):
    os.makedirs(home+'Images')

if not os.path.exists(home+'Media'):
    os.makedirs(home+'Media')


dest_dir_file = home+'Text Dokuments'
dest_dir_programs = home+'Programs'
dest_dir_images = home+'Images'

#Programs
for exe in glob.glob( home+r'*.exe'):
    print(exe)
    shutil.move(exe, dest_dir_programs)

for lnk in glob.glob( home+r'*.lnk'):
    print(lnk)
    shutil.move(lnk, dest_dir_programs)
    
for url in glob.glob( home+r'*.url'):
    print(url)
    shutil.move(url, dest_dir_programs)

#Images
image = ['*.jpeg', '*.png' , '*.tif',  '*.gif' , '*.ico']

for image in glob.glob(home+r''+image[0]):
    print(image)
    shutil.move(image, dest_dir_images)

for image in glob.glob(home+r''+image[4]):
    print(image)
    shutil.move(image, dest_dir_images)

for image in glob.glob(home+r'*png'):
    print(image)
    shutil.move(image, dest_dir_images)

for image in glob.glob(home+r'*tif'):
    print(image)
    shutil.move(image, dest_dir_images)

for image in glob.glob(home+r'*gif'):
    print(image)
    shutil.move(image, dest_dir_images)

#Files
files = ['*.html', '*.txt', '*.py', '*.odt', '*.tmp', '*.doc', '*.rtf', '*.docx', '*.pdf']

for file in glob.glob(home+r''+files[0]):
    print(file)
    shutil.move(file, dest_dir_file)

for file in glob.glob(home+r''+files[1]):
    print(file)
    shutil.move(file, dest_dir_file)

for file in glob.glob(home+r''+files[2]):
    print(file)
    shutil.move(file, dest_dir_file)

for file in glob.glob(home+r''+files[3]):
    print(file)
    shutil.move(file, dest_dir_file)

for file in glob.glob(home+r''+files[4]):
    print(file)
    shutil.move(file, dest_dir_file)
    
for file in glob.glob(home+r''+files[5]):
    print(file)
    shutil.move(file, dest_dir_file)

for file in glob.glob(home+r''+files[6]):
    print(file)
    shutil.move(file, dest_dir_file)

for file in glob.glob(home+r''+files[7]):
    print(file)
    shutil.move(file, dest_dir_file)

for file in glob.glob(home+r''+files[8]):
    print(file)
    shutil.move(file, dest_dir_file)

input()

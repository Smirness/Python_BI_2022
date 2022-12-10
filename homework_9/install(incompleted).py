#!/usr/bin/env python3

### Don't run. It's code in proccessing 

import os
import shutil

# preparing scripts for coping
source = os.path.abspath('./scripts_smirnov_vv')
source_scripts = []
# print(source)

for file in os.listdir(source):
    source_scripts.append(os.path.join(source, file))

# finding directory suitable for adding in $PATH
exec_path = os.get_exec_path()
exec_first_path = exec_path[0]

# creating destination path, adding our directory to path, coping to our directory
dest_path = os.path.dirname(exec_first_path)
dest_dir = os.path.join(dest_path, 'scripts_smirnov_vv')

os.mkdir(dest_dir)

for file in source_scripts:
    shutil.copy(file, dest_dir)


# adding path of our directory to #PATH
path_file = '/etc/environment'

with open(path_file, 'r') as file:
    line = file.readline()
    print('Your previous paths in $PATH: %s, keep it for your calm' % line)
    input('Type Enter if want to add %s in $PATH' % dest_dir)
    path_var = line.split(':')
    path_var.insert(1, dest_dir)
    path_var = ':'.join(path_var)

# with open(path_file, 'w') as file:
#     file.write(path_var)

print(path_var)

#  PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"

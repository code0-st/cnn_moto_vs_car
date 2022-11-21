import os
import random as rnd

# label = 'car'
label = 'bike'
# data_type = "test"
data_type = "train"
dir_name = os.path.join('dataset', data_type, label)
files_count = len(os.listdir(dir_name)) * 10000
data = os.scandir(dir_name)

for file in data:
    file_name = os.path.split(file.path)[1]
    extension = file_name.split('.')[1]
    new_file_name = str(rnd.randint(0, files_count)) + "_" + label + "." + extension
    os.rename(file.path, os.path.join(dir_name, new_file_name))
data.close()

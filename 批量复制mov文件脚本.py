import os
import shutil

path = ""
new_path = ""

for root, dirs, files in os.walk(path):
	for i in range(len(files)):
		if files[i][-3:] == 'mov':
			file_path = root + '/' + files[i]
			new_file_path = new_path + '/' + files[i]
			shutil.copy(file_path, new_file_path)




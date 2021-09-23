import os
import zipfile

name_zip = zipfile.ZipFile('/home/phien/Desktop/main.zip')
name_zip.extractall('/home/phien/Desktop/w3')
name_zip.close()

file_zip = open('filez.txt','w')
arr = []
for folder, subfolder, files in os.walk('/home/phien/Desktop/w3'):
	for file in files:
		if file.endswith('.py'):
			arr.append(file)
			break

arr.sort()
file_zip.write('\n'.join(arr))

file_zip.close()
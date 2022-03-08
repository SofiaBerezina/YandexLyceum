from zipfile import ZipFile
import json


with ZipFile('input.zip') as myzip:
    count = 0
    info = myzip.infolist()
    for i in range(len(info)):
        file = info[i].filename
        if file.split('.')[-1] == 'json':
            print(info[i])
            with open(file) as data:
                file_js = json.load(data)
            for key, value in file_js.items():
                if key == 'city' and value == 'Moscow':
                    count += 1
print(count)
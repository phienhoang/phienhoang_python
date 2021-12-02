import pickle
import os
from pathlib import Path
import re


class TextLoader:
    def __init__ (self, adress):
        self.path = adress
        self.files_list = [x for x in list(os.listdir(self.path))]
        self.iterable = iter (self.files_list)
        self.made = set()

    def __len__ (self):
        return len(self.files_list)

    def __getitem__ (self, path):
        return formatted(path)

    def formatted (self, path): 
        file = open(path, "r+t", encoding='utf-8')
        text = ''
        for line in file:
            line = line.lower()
            line = re.sub(r'[^\w\s]','', line) 
            text += '\n'
            text += line
        file.close()
        return text

    def __iter__ (self):
         return self

    def __next__ (self):
        file_path = next(self.iterable)
        while file_path in self.made:
            file_path = next(self.iterable)
        self.made.add(file_path)
        print (file_path)
        text = self.formatted(file_path)
        return text

    def __getstate__(self):
        state = self.__dict__.copy()
        return state

    def ndump(self):
        os.chdir('..')
        with open('./data.pickle', 'wb') as f:
            pickle.dump(self, f , pickle.HIGHEST_PROTOCOL)

    def __setstate__(self, state):
        self.__dict__.update(state)


if not os.path.exists('./data.pickle'):
    texts = TextLoader('sample')
else:
    with open("./data.pickle", "rb") as f:
        texts = pickle.load(f)
        texts.files_list = [x for x in list(os.listdir(texts.path))]
        texts.iterable = iter (texts.files_list)
os.chdir('sample')
while True:
    print("Ожидание команды: ", end= '')
    In = input()
    if In == 'next':
        try:
            print(texts.__next__())
        except Exception:
            break
    if In == 'end':
        texts.ndump()
        break


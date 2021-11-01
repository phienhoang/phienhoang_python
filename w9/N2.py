import zipfile
import pathlib
import io
import re

class TextLoader:
    def __init__(self, address):
        a = zipfile.ZipFile(address)
        a.extractall('file')
        a.close()
        self.path = pathlib.Path('/home/phien/Desktop/w9/file/sample')
        list_files  =  [name for name in list(self.path.glob('**/*.txt')) if name.is_file()]
        self.files = list_files
        self.iterable = iter(self.files)

    def __len__(self):
        return len(self.files)

    def __next__(self):
        text = next(self.iterable)
        with text.open('r') as f:
            r = f.read()
        with text.open('w') as f:
            norm = self.__getitem__(r)
            f.write(norm)

    def __iter__(self):
        return self

    def __getitem__(self,t):
         t = re.sub(r'[,.:;?!]','', t)
         t = t.lower()

if __name__ == "__main__":
    address = '/home/phien/Desktop/w9/sample.zip'
    a = TextLoader(address)
    print(len(a))
    for i in range(len(a)):
        try:
            b = next(a)
            print(b.read())
            print("----------")
        except StopIteration:
            print("End.")
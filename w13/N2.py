
import pickle

class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data
        self.size = 0
    def append(self, val):
        if self.data == None:
            self.data = val
            self.size += 1
        else:
            end = Node(val)
            n = self
            while (n.next):
                n = n.next
            n.next = end
            self.size += 1
    def delete(self, n):
        if self.data == None:
            print('Нечего удалять')
        else:
            last = self
            now = last.next
            if n == 0:
                self.data = now
            elif n >= last.size:
                print('Такой ячейки не существует')
            else:
                while n > 1:
                    n -= 1
                    if now == None:
                        print('Такой ячейки не существует')
                    last = now
                    now = last.next
                last.next = now.next
    def ndump(self):
        with open('./data.pickle', 'wb') as f:
            pickle.dump(self, f , pickle.HIGHEST_PROTOCOL)
    def __str__(self):
        out = ''
        if self.data == None:
            out += 'Список пуст'
        else:
            n = self
            while (n.next):
                out += str(n.data)
                out += ' '
                n = n.next
            out += str(n.data)
        return out


lis = Node()
for i in range(0,15,2):
    lis.append(i)
print(lis)

data = lis.ndump()
with open("./data.pickle", "rb") as f:
    Copy = pickle.load(f)
Copy.delete(10)
print(Copy)


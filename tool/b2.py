def write_array(array, file_name):
    array = map(lambda x: x + '\n',array)
    with open(file_name, "w") as file:
         file.writelines(array)
write_array(["sunset","verry","beautiful!"],"1.txt")
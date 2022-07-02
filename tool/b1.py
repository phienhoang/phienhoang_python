file = open("/media/phien/data1/tool/test.txt", "w")
file.write(" I see your monster\n")
file.write("I see your pain\n")
file.write("Tell me your problems, i take them away  \n")
file.close()
with open("test.txt", "r") as file:
    for line in file:
        print(line.strip())
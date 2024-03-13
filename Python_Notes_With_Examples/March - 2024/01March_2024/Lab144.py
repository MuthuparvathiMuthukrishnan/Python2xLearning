#give the absolute path of the file location which is present in a different place

path = "/Users/new/PycharmProjects/Parusfirstproject1/Feb - 2024/Feb.txt"
with open(path) as file:
    print(file.read())
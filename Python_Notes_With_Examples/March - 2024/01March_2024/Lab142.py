try:
    with open("TestData",'r') as file: #with is able to wrap the content instead of gettinga a variable and then printing
        content = file.read()
        print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    file.close()
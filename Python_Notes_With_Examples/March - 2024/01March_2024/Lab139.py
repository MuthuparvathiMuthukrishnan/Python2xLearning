#Core Programming + OOPs + Exceptions

def f1():
    print("f1")
def f2():
    f1()
    print("f2")
def f3():
    print("f3")
def main():
    print("this is a main class")
if __name__ == "__main__":
    #here we can mention which is my main function
    #and that will run accourdingly
    f2()
    main()
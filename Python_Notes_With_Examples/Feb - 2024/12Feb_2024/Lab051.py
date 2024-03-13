#Match Case #inbuild condition
#Similar to Switch case
#No need of break in Match case. break command not required in python
num = int(input("Enter the number 1-3 : "))
match num:
    case 1:
        print("You have entered the value 1 ")
    case 2:
        print("You have entered the value 2 ")
    case 3:
        print("You have entered the value 3 ")
    case n:
        print("Out of given range")
print("This is Match case example")

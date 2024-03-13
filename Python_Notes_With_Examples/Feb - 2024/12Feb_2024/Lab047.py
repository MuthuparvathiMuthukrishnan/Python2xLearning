#Continue - alternate of break
for num in range(1,10):
    if num % 2 ==0:
        print(f"Found even number \n {num}")
        continue
    print(f"found odd number \n {num}" ) #if this statement is not there when the code will print only the even number
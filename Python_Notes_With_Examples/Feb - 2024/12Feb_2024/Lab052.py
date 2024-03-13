browser = input("Enter the browser name : ")
match browser:

    case "Google chrome":
        print("You have entered the browser name : Google Chrome")
    case "firefox":
        print("You have entered the browser name : Firefox")
    case "Microsoft edge":
        print("You have entered the browser name : Microsoft edge")
    case _:
        print("Browser not in scope for the testing")
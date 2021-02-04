while True: 
    userName = input("Username: ") 
    password = input("Password: ")
    if userName == 'serif' and password == 'serif': 
        print("correct username and password")
        break
    else:
        print("wrong username and password")
        break

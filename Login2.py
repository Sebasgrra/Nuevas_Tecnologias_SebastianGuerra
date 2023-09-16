Menu = """ 
Menu 
1- Create account......
2- Login.
3- Exit.
"""

while True:

    print(Menu)
    optionmenu = int(input("Chose one opction please: "))
    
    
    if optionmenu == 1 or optionmenu == 2:
        if optionmenu ==1:
            print("Registracion")
            correctuser = input("Register your user name: ")
            correctpassword = int (input("Registe your password, just numbers : "))
            print("Fully complete record")
        elif optionmenu ==2:
            username = input("Write your username or cellphone number: ")
            password = int(input("Write your password: "))
            captcha = int(input("How much is 9.5 + 90.5? "))
            if (correctuser == username or username == "31234567") and password == correctpassword and captcha == 100:
                
             print("Successful login")
            else:
              print("No login")
        else:
            print("Choose a valid number")
    elif optionmenu == 3:
        print("THANKS, program was closed")
        break  
    else:
        print("Please chose a valud number")


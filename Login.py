correctuser = input("Register your user name: ")
correctpassword = int (input("Registe your password, just numbers : "))


username = input("Write your username or cellphone number: ")
password = int(input("Write your password: "))
captcha = int(input("How much is 9.5 + 90.5? "))

if (correctuser == username or username == "31234567") and password == correctpassword and captcha == 100:
    print("Successful login")
else:
    print("No login")

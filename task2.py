#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
Pw = "12345"
Us = "admin"
print("===========")
while True:
    a = input("\nUsername: ")
    if a == Us:
        b=input("Password: ")
        if b == Pw:
            break
    else:
        print("Access denied")

print("Access Granted!")
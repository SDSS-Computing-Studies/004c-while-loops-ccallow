##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Acces denied
"""

Pw = "12345"
Us = "admin"
print("===========")
while:
    a = input("\nUsername: ")
    if a == Us:
        b=input("Password: ")
        if b == Pw:
            break
    else:
        print("Access denied")

print("Access Granted!")
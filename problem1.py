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
import math
import time

count =0

Pw = "12345"
Us = "admin"
print("===========")
while count<3:
    count=count +1
    a = input("Username: ").strip()
    if a == Us:
        b=input("Password: ").strip()
        if b == Pw:
            print("Access granted")
            break
while count ==3:
    print("Access denied")
    break
    


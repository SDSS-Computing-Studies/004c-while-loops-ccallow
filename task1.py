#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
import time
import random

count = 0
print("========================")
print("Let's count to 20 by 2s!")
print("========================")
while True:
    count = count + 2
    n =str(count)
    print(n)
    if count == 20:
        break
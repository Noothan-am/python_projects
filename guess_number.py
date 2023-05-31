import random
import math 

def randomNum():
    num = random.random()
    newnum = math.trunc((num*10)%10)
    print(newnum)
    return newnum
while True:
    number = int(input("enter the number"))
    if (number == randomNum()):
        print(f"correct number is {number}")
        break

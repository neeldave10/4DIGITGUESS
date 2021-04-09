from time import sleep
import random
n=random.randint(1000,9999)
print(n)
n1=int(input("enter a four digit number"))
print(n1)
unit=n1%10
ten=(n1/10)%10
hun=(n1/100)%10
tho=n1/1000
print(unit)
print(ten)
print(hun)
print(tho)

unit1 = n % 10
ten1 = (n / 10) % 10
hun1 = (n / 100) % 10
tho1 = n / 1000
print(unit1)
print(ten1)
print(hun1)
print(tho1)

if(tho1==tho):
    print("R");sleep(0.5)
elif(tho1 == unit or tho1==ten or tho1==hun):
    print("y");sleep(0.5)
else:
    print("B");sleep(0.5)

if(hun==hun1):
    print("R");sleep(0.5)
elif(hun==unit1 or hun==ten1 or hun==tho1):
    print("y");sleep(0.5)
else:
    print("B");sleep(0.5)

if(ten==ten1):
    print("R");sleep(0.5)
elif(ten==unit1 or ten==hun1 or ten==tho1):
    print("y");sleep(0.5)
else:
    print("B");sleep(0.5)

if(unit==unit1):
    print("R");sleep(0.5)
elif(unit==ten1 or unit==hun1 or unit==tho1):
    print("y");sleep(0.5)
else:
    print("B") ;sleep(0.5)









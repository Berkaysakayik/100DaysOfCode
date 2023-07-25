import time


a  = "100DaysOfCode"
aa = "#100DAYSOFCODE-5.DAYS"
b = len(a)

print(aa)

for i in a:
    print("*", end="")

print("")

for i in range(0,b):
    for x in range(0,i+1):
        time.sleep(0.07)
        print(a[x],end="")
    print("\r")

for i in range(b-1,0,-1):
    for x in range(i):
        time.sleep(0.07)
        print(a[x],end="")
    print("\r")

for i in a:
    print("*", end="")

print("")
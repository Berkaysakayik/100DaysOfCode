
x, y = input ("Enter two values(Boys, Girls): ").split()
print ("Number of boys: ", x)
print ("Number of girls: ", y)


x, y, z = input ("Enter three values(Totals, Boys, Girls): ").split()
print ("Total numbers of students: ", x)
print ("Number of boys is: ", y)
print ("Number of girls is: ", z)


a, b = input("Enter two values(a, b): ").split()
print ("First number is {} and second number is {}!".format(a, b))



x = list(map(int, input("Enter multiple values: ").split()))
print ("List of students: ", x)


x = [int(x) for x in input("Enter multiple value(x,yzx,xc,etc(but int)): ").split(",")]
print ("Number of list is: ", x)
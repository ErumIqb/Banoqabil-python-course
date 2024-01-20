# Erum Iqbal
# Mid Term Examination
# Q.1 Write a python program to do arithmatic operations addition and division.
 
a = int(input("Enter the number:" ))
b = int(input("Enter the number:" ))
sum = a + b
print("The sum of",a,"+",b,"is",sum)

a = int(input("Enter the number:" ))
b = int(input("Enter the number:" ))
division = a / b
print("division: ",a,"/",b,"=",division)

a = int(input("Enter the number:" ))
b = int(input("Enter the number:" ))
power = a ** b
print("Power:",a,"**",b,"=",power)

a = int(input("Enter the number:" ))
b = int(input("Enter the number:" ))
fld = a // b
print("Floor Division:",a,"//",b,"=",fld)

# Q.2 Write a Python program to find the area of triangle.

b = int(input("Enter the base of the triangle:" ))
h = int(input("Enter the height of the triangle:" ))
area = 1/2 * b * h
print("The area of the triangle is :",area)

# Q.3 Write the Python program to convert Celsius to Fahrenheit.

c = int(input("Enter temprature in Celsius:" ))
f = (9/5 * c) + 32
print("37 degrees Celsius is equal to",f,"degrees Fahrenheit")


# Q4. Write the Python program that return all datatypes that we discussed in the class.

a = 10
print(a)
print("The data type of",a,"is",type(a))

b = 10.5
print(b)
print("The data type of",b,"is",type(b))

d = True
print(d)
print("The data type of",d,"is",type(d))

e = [1,2,3,4,5]
print(e)
print("The data type of",e,"is",type(e))

a = (1,2,3,4,5)
print(a)
print("The data type of",a,"is",type(a))

a = {1,2,3,4,5}
print(a)
print("The data type of",a,"is",type(a))

x = 'Hello World'
print(x)
print("The data type of",x,"is",type(x))
#TASK 1

r=float(input("Input the radius of the circle:"))
print("The radius of the circle is :",r)
area=float(22/7*r*r)

print("The area of the circle with radius ",r," is :",area)


#TASK 2
import os
file=input("Input the filename:")
print("The file is:"+file)

x=os.path.splitext(file)

file_name=x[0]
file_extension=x[1]

print("The filename is:",file_name)
print("The file extension is:",file_extension)

if(file_extension==".py"):
    print("The entered file is a python file")
else:
    print("The entered file is not a python file")

    

#If else if and else in python

if 2 > 2:
    print("hello")
elif 3 == 3:
    print("gone")
else:
    print("done")

print("                  ")

#loops in python
list = [1,2,3,4,5,6]

#for loop
for item in list:
    print(item) 


print("while loop:")
#while loop
i = 1
while i < 5: 
    print(i) 
    i= i + 1

print("for in range:")

#for loop in range method
for pieces in range(0,10,2):
    print(pieces)

#list comprehension using for loop
print("list comprehensio:")
x = [1,2,3,4]
square = [num**2 for num in x]
print(square)


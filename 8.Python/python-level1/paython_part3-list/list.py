firstList = [1,2,3] # list of numbers
secondList = ["dog","cat","cow","hen"] # list of string with name of domestic animals.

thirdList = ["hi",5,10.2,True]#list of mixed data types.

print(firstList)
print(secondList)
print(thirdList)


#using len() to find the lenght of the list
print(len(firstList))
print(len(secondList))
print(len(thirdList))

#slicing in list
print(firstList[1:])
print(secondList[:3])
print(thirdList[1:3])


#Reassignment in list
print("Befor reassignment :")
print(firstList)
print("After reassignment:")
firstList[0]= 5
print(firstList)

#using append() in list
print("Befor using append()")
print(secondList)
secondList.append("cocks")
print("After using append()")
print(secondList)



#using extend() in list
fourthList = [5.5,False,35,"bye"]

thirdList.extend(fourthList)
print(thirdList)

#using pop() to remove the last element of the list
item = thirdList.pop()

print(thirdList)
print(item)


#using reverse() to  reverse the list
secondList.reverse()
print(secondList)

#using sort() in list
secondList.sort()
print(secondList)

#list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[2] for row in matrix]
print(first_col)
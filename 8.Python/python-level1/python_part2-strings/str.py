#Basics
'hello'
"hello"


#Indexing
myString = 'abcdefg'
print(myString[3])



#slicing
myString = 'abcdefg'
print(myString[1:])

myString = 'abcdefg'
print(myString[:3])

myString = 'abcdefg'
print(myString[2:4])


#Basic Methods
up = myString.upper()
print(up)

low = myString.lower()
print(low)

cap = myString.capitalize()
print(cap)

sp = myString.split()
print(sp)

nextString = "python"

sp2 = nextString.split()
print(sp2)

spl = nextString.split('t')
print(spl)



#Print formating
fstr = "lis of anime 1st_item: {}, 2nd_item: {}.".format("fire-force","odd-taxi")
print(fstr)
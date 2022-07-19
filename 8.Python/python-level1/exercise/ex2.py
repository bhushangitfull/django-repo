#given a list of integers, return true if the sequence of numbers 1, 2, 3 appears in the list some where

#for example:
#arrayCheck([1,2,3,4,5]) -> True
#arrayCheck([1.2.4.5.6])-> Flase

#Ans:

def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True

    return False

print(arrayCheck([1,4,1,2,3]))


#given a string, return a new string made of every other charachter starting wih the first, so  "hello" yields "hlo"
#stringBits("hello") -> "hlo"
#stringBits("hi") -> "h"

#first simple method
def stringBits(mystring):
    result = mystring[::2]

    return result

print(stringBits("hello"))

#second standard method

def stringMOd(secsstr):
    modstr = ""
    for i in range(len(secsstr)):
        if i%2 == 0:
            modstr = modstr + secsstr[i]

    return modstr

print(stringMOd("brobravo"))
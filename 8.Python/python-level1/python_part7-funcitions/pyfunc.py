#Demo function
def myhello():
    return ("hello")

print(myhello())#function calling with printing

#add function
def addnum(num1,num2):
    if type(num1) == type(num2) == type(1):
        return num1 + num2
    else:
        return("soory it should be a number ")

firstAdd = addnum(1, 2)

print(firstAdd)




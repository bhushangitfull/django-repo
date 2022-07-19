x =  20 # global scope

def firstFunc():
    x = 50  #local scope
    print(x) 

print(x)

firstFunc()
print(x)

#enlosing function locals:

name = "this is the global name"

def greet():
    name = "sammy"

    def hello():
        print("hello"+name)

    hello()

greet()

print(name  )
 

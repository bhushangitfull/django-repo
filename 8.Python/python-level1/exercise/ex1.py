#problem 1
s = "django"

print(s[0])
print(s[5])
print(s[:4])
print(s[1:4])
print(s[4:])
print(s[::-1])

#problem 2

l = [3,7,[1,4,"hello"]]

l[2][2] = "good bye"
print(l)


#Using keys and indexing, grab the 'hello' from the following dictionaries:
d1 = {'simple_key':"hello"}
print(d1['simple_key'])
 
d2 = {'k1':{'k2':"hello"}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])



#use print formatting to print the following string along with the given variables

age = 4
name = "sammy"

print("hello my dog's name is {n} and he is {a} years old".format(n=name,a=age))
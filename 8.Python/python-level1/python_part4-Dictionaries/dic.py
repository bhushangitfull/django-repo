#Dictionary

emp_detail = {'emp-name':"shelly",'emp-salary':20000,'emp-state':"New york"}

#printing whole content of dictionary

print(emp_detail)


#printing specific key value from the dictionary
print(emp_detail['emp-salary'])

#reassignment in dictionary
emp_detail['emp-salary']= 25000
print(emp_detail)

#adding new key in dictionary

emp_detail['emp-lastname']="olson"

print(emp_detail)
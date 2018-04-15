############## Dictionaries {} ###########################
# Dictionaries consists of keys and values

student = {'name': 'John','age':28,'courses':['Maths','Physics']}
print(student)

#output - {'name': 'John', 'age': 28, 'course': ['Maths', 'Physics']}

print(student['name'])
#Output - John
print(student['courses'])
#Output - ['Maths', 'Physics']

#print(student['phone']) # KeyError: 'phone' - phone key doesnt exist

print(student.get('name'))  # Output - John
print(student.get('phone')) # Output - None - by default get method checks for value or key if not present throws None
print(student.get('phone','Not Found')) # Output - Not Found - since we are passing the default message as Not Found

student['phone']= '555-555-5555'
print(student.get('phone','Not Found')) # output - 555-555-5555
print(student)      # Output - {'name': 'John', 'age': 28, 'courses': ['Maths', 'Physics'], 'phone': '555-555-5555'}
student['name'] = 'Jack'
print(student)      # Output - {'name': 'Jack', 'age': 28, 'courses': ['Maths', 'Physics'], 'phone': '555-555-5555'}

#UPDATING multiple values
#student.update({'name':'Jack', 'age':22, 'phone':'999-999-9999'})
print(student)      # Output - {'name': 'Jack', 'age': 22, 'courses': ['Maths', 'Physics'], 'phone': '999-999-9999'}

del student['age']
print(student)      #Output - {'name': 'Jack', 'courses': ['Maths', 'Physics'], 'phone': '999-999-9999'}

student = {'name': 'John','age':28,'courses':['Maths','Physics']}
age = student.pop('age')
print(student)
print(age)
#{'name': 'John', 'courses': ['Maths', 'Physics']}
#28

student = {'name': 'John','age':28,'courses':['Maths','Physics']}

print(len(student)) # 3 keys in the dictionary
print(student.keys())   # dict_keys(['name', 'age', 'courses'])
print(student.values()) # dict_values(['John', 28, ['Maths', 'Physics']])
print(student.items())  # dict_items([('name', 'John'), ('age', 28), ('courses', ['Maths', 'Physics'])])
for key in student:
    print(key)
#name
#age
#courses

for key,value in student.items():
    print(key, value)

# name John
# age 28
# courses ['Maths', 'Physics']

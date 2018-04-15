#String formatting oprions in python
#My name is John and I am 33' - print the same message using different string formattings.

person = {'name': 'John', 'age':23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old'
print(sentence)

sentence='My name is {} and I am {} years old.'.format(person['name'],person['age'])
print(sentence)

# sentence='My name is {0[name]} and I am {1[age]} years old'.format(person,person)
# print(sentence)

# sentence='My name is {0[name]} and I am {0[age]} years old.'.format(person)
# print(sentence)

# l = ['John',23]

# sentence='My name is {0[0]} and I am {0[1]} years old'.format(l)
# print(sentence)

# sentence ='My name is {name} and I am {age} years old.'.format(name='John', age='33')
# print(sentence)

# sentence='My name is {name} and I am {age} years old'.format(**person)
# print(sentence)

# tag = 'hi'
# text = 'This is a headline'
# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)


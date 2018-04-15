for i in range(1,11):
	sentence = 'The value is {}'.format(i)
	print(sentence)
#Output
# The value is 1
# The value is 2
# The value is 3
# The value is 4
# The value is 5
# The value is 6
# The value is 7
# The value is 8
# The value is 9
# The value is 10

# for i in range(1,11):
# 	sentence = 'The value is {:02}'.format(i)
# 	print(sentence)

## Output
# The value is 01
# The value is 02
# The value is 03
# The value is 04
# The value is 05
# The value is 06
# The value is 07
# The value is 08
# The value is 09
# The value is 10

# for i in range(1,11):
# 	sentence = 'The value is {:03}'.format(i)
# 	print(sentence)

# ## Output
# The value is 001
# The value is 002
# The value is 003
# The value is 004
# The value is 005
# The value is 006
# The value is 007
# The value is 008
# The value is 009
# The value is 010


# pi = 3.14159265

# sentence = 'Pi is equal to {:.3f}'.format(pi)
# print(sentence)

# Output -- here .2f is formatting the pi value to two decimal points
# Pi is equal to 3.14

# Output -- here .3f is formatting the pi value to three decimal points
# Pi is equal to 3.142 

# sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
# print(sentence)

#Output
#1 MB is equal to 1,000,000 bytes

# sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)

# #Output
# 1 MB is equal to 1,000,000.00 bytes


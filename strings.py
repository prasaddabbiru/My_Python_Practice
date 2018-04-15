message = 'Hello World'
print(message)

#Output 
#Hello World

message = 'Prasad\'s world' # Here in order to print ' we use '/' so that it prints as the string is
print(message)
#Output 
#Prasad's world

# Insted we can use "Prasad's World" to print the string as it is thats the difference of using single & doule Quotes
message="Prasad's world"
print(message)
#Output 
#Prasad's world

# Multi-Line String

message= """ Prasad's world was a good
cartoon in the 1990s"""
print(message)

#Output
# Prasad's world was a good
#cartoon in the 1990s

message='Hello World'
print(len(message))		# Length of the string i.e 11 characters
print(message[0])		# message[0], 0 index of the message i.e 'H'
print(message[0:5]) 	# prints from '0' index i.e 'H' upto 5th index but not 5th i.e 'o'
print(message[6:])		# prints from index no '6' i.e 'w' thour end of the string i.e 'world'
print(message.lower()) 	# prints lower case i.e 'hello world'
print(message.upper()) 	# prints lower case i.e 'HELLO WORLD'
print(message.count('Hello'))	# prints the count of the string passed i.e Hello count is 1.
print(message.count('l'))		# prints the count of l in the message i.e 3
print(message.find('world'))	# finds the index where the string or word or letter starts i.e 6
print(message.find('Universe'))	# prints negative since the string is not found
print(message.find('l'))
new_message = message.replace('World','Universe')
print(new_message)	#Prints Hello Universe, here the word World is replaced with Universe and assigned the string to Variable new_message
message=message.replace('World','Universe')
print(message)


#######################		Concatenating Strings   ###################################################################

greeting = 'Hello'
name = 'Prasad'

message = greeting + ',' + name + '.Welcome!' # Output - Hello,Prasad.Welcome!
print(message)

message = '{},{}.Welcome!'.format(greeting,name) # Output - Hello,Prasad.Welcome!
print(message)

message= f'{greeting},{name}.Welcome!'	# Output - Hello,Prasad.Welcome!
print(message)



















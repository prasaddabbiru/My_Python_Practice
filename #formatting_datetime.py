#Formatting date time
import datetime
my_date = datetime.datetime(2018, 4, 15, 1, 40, 55)
print(my_date)
#Output
#2018-04-15 01:40:55


sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

#Output
#April 15, 2018

#

sentence= '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} of the year.'.format(my_date)
print(sentence)

#Output
#April 15, 2018 fell on a Sunday and was the 105 of the year.

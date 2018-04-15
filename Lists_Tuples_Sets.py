##############################  Lists ##################################################

courses =['Maths','Pysics','Chemistry','Biology']
print(courses)      #output - ['Maths', 'Pysics', 'Chemistry', 'Biology']

print(len(courses)) #output : 4 (Length of the courses)

print(courses[0])   #output : Maths (Index of the courses i.e index '0' is Maths in courses

print(courses[-1])  #output : Biology (negative indicates from right to left -1 is Biology in this case)

print(courses[1:3]) #output : ['Pysics', 'Chemistry']

courses.append('Art')
print(courses)      #output : ['Maths', 'Pysics', 'Chemistry', 'Biology', 'Art']

courses.insert(0,'CompScience')
print(courses)      #output : ['CompScience', 'Maths', 'Pysics', 'Chemistry', 'Biology', 'Art']

courses_2 = ['Python','Java','AI']
courses.insert(0,courses_2)
print(courses)      #output : [['Python', 'Java', 'AI'], 'CompScience', 'Maths', 'Pysics', 'Chemistry', 'Biology', 'Art']

courses.extend(courses_2)
print(courses)      #output : [['Python', 'Java', 'AI'], 'CompScience', 'Maths', 'Pysics', 'Chemistry', 'Biology', 'Art', 'Python', 'Java', 'AI']

courses.remove(courses_2)
print(courses)      #output : ['CompScience', 'Maths', 'Pysics', 'Chemistry', 'Biology', 'Art', 'Python', 'Java', 'AI']

courses.pop()
print(courses)      #output : ['CompScience', 'Maths', 'Pysics', 'Chemistry', 'Biology', 'Art', 'Python', 'Java']
# pop by default removes last item in the list and returns the value.

popped =courses.pop()
print(popped)       #output : Java ( java has been removed(popped) from list and assigned to popped variabel to return value
print(courses)      #output : ['CompScience', 'Maths', 'Pysics', 'Chemistry', 'Biology', 'Art', 'Python']

courses.reverse()
print(courses)      #output - ['Python', 'Art', 'Biology', 'Chemistry', 'Pysics', 'Maths', 'CompScience']

courses.sort()
print(courses)      #output - ['Art', 'Biology', 'Chemistry', 'CompScience', 'Maths', 'Pysics', 'Python']

num = [12,3,1,2,9,5]
num.sort()
print(num)          #output - [1, 2, 3, 5, 9, 12] - sorted in ascending order

# to print in descending order

num.sort(reverse=True)
courses.sort(reverse=True)
print(num)          #output - [12, 9, 5, 3, 2, 1]

print(courses)      #output - ['Python', 'Pysics', 'Maths', 'CompScience', 'Chemistry', 'Biology', 'Art']

print(sum(num))     #output - 32

print('AI' in courses)  #output - False - since AI is not in list this option is used in conditions or loops
print('Python' in courses)  #output - True

for course in courses:
    print(course)
#Output

# Python
# Pysics
# Maths
# CompScience
# Chemistry
# Biology
# Art

for index,course in enumerate(courses):
    print(index, course)

# Output

# 0 Python
# 1 Pysics
# 2 Maths
# 3 CompScience
# 4 Chemistry
# 5 Biology
# 6 Art


for index,course in enumerate(courses, start=1):
    print(index, course)
#Output

# 1 Python
# 2 Pysics
# 3 Maths
# 4 CompScience
# 5 Chemistry
# 6 Biology
# 7 Art

course_str= " - ".join(courses)
print(course_str)

#Output
# Python - Pysics - Maths - CompScience - Chemistry - Biology - Art

new_list = course_str.split(' - ')
print(new_list)

#Output
#['Python', 'Pysics', 'Maths', 'CompScience', 'Chemistry', 'Biology', 'Art']


##############################  Tuples ###############################################################

# Tuples are immutable means which can't be modified, other than that tuples acts exactly like lists

tuple_1 = ('Python', 'Pysics', 'Maths', 'CompScience', 'Chemistry')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art'  # Throws error since tuple cannot be modified.

##############################  Sets ###############################################################

# Sets are unordered and no duplicate values {}

cs_courses = {'Maths','Geography','History','CompSci'}

print(cs_courses)
#Output - {'Maths', 'Geography', 'History', 'CompSci'} Everytime you run the program it will print in different order

cs_courses = {'Maths','Geography','History','CompSci','Maths'}
print(cs_courses)

# {'Geography', 'CompSci', 'Maths', 'History'} - Maths is duplicate entry which gets removed and prints the list

art_courses = {'Maths','History','Design','Arts'}

print(cs_courses.intersection(art_courses))

#Output - {'Maths', 'History'} - Intersection gives output of items that are common.

print(cs_courses.difference(art_courses))

#{'Geography', 'CompSci'} - Difference gives output of items that are from art_courses

print(cs_courses.union(art_courses))

#{'History', 'Geography', 'Maths', 'Design', 'Arts', 'CompSci'} - combination of art_courses & cs_courses

############################# Notes ###########################################

#Empty Lists
empty_list = []
empty_list = list()

#Empty tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty sets can't be created '{}' will direct to dictionary

empty_set = {} # This creates an empty dictionary not set
empty_set = set() # This creates a set.








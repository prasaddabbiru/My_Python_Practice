marks = {'Prasad':{'English':65,'Maths':55,'Science':68,'Hindi':78},
         'Ravi':{'English':45,'Maths':35,'Science':58,'Hindi':68},
         'Raj':{'English':85,'Maths':75,'Science':78,'Hindi':88},
         }
x = str(input("Enter Candidate name for total marks:"))
if x in marks.keys():
    for i in marks.values():
        print("---: Each Subject Marks below :---\n",marks[x])  ##marks[Key]
        total_marks = marks[x]
        print("Total Marks",sum(total_marks.values()))
        print("---: Each Subject Marks below :---\n",marks[x])
        total_marks = marks[x]
        print(sum(total_marks.values()))
        avg = (sum(total_marks.values())/4)
        print("Average of ", x , " is " , avg)
        break
    


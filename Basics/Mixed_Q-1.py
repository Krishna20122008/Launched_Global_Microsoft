Name = ["Krishna", "Swapnil","Cheryl", "Sarvesh", "Moksh"]

Subject = ("CS", "Maths", "English")

Student_Subject = {"CS", "English", "Maths"}
Student_Subject.add("Biology")
Student_Subject.remove("Maths")

StudentNameMarks = {"Krishna": 100, "Cheryl": 95, "Swapnil": 89, "Sarvesh": 70, "Moksh": 94}

NewStudentName = input("Enter the name of student: ")
Marks = input("Enter the marks of student: ")
Marks = int(Marks)
StudentNameMarks[NewStudentName] = Marks

if(Marks >= 90): Result = ("Excellent")
elif(Marks >= 75 and Marks < 90): Result = ("Very Good")
elif(Marks >= 50 and Marks < 75): Result = ("Good")
else: Result = ("Needs Improvement!")

print(NewStudentName, ": ", Result)
print(Name)
print(Subject)
print(Student_Subject)
print(StudentNameMarks)
student = {"Name": "Krishna", "Age": 18, "Course": "CSE", "City": "Gandhinagar", "Skills": "Python, SQL, C, C++, HTML, AI, DSA"}
print(student["Name"])
print(student["Course"])

student["Experience"] = "5 Years"
student["City"] = "Ahmedabad"
student.pop("Age")

for i in student:
    print(i, "\t")
    print(student[i], "\n")
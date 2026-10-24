Student = {"Name" : "Krishna", "Age" : "18", "Height" : "5'10"}
print(Student["Name"])
print(Student["Age"])
print(Student["Height"])

Student["Hobby"] = "Gaming"
print (Student)

Student.pop("Age")
print(Student);

print(Student.values())
print(Student.items())
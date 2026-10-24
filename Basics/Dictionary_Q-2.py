employee = {"Name": "Krishna", "Department": "AIML", "Salary": 10000000, "Experience": "7 yrs", "Skills": ["Python", "DSA", "ML"]}
print(employee["Name"])
print(employee["Salary"])

employee["Salary"] += (employee["Salary"]) * 10 / 100
employee["Location"] = "Pramukh Pearl"
employee.pop("Experience")

if "Department" in employee: print("Yes")
else: print("No")

print(employee.items())
skills = {"Python", "SQL", "Excel"}
skills.add("Machine Learning")  # Adds single element
skills.update(["Deep Learning", "Power BI"])    # Adds multiple items
skills.remove("Excel")  # removes excel
skills.discard("Java")  # removes java even though it was not even in the set
print(skills)
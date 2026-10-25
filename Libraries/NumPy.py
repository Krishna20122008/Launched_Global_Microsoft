import numpy as np
a = np.array([10,20,40,50])
print(a)

print(a+10)
print(a*10)

marks = np.array([50,48,38,42])
print("The average marks are: ",np.mean(marks))
print("The sum of marks are: ", np.sum(marks))
print("The min of marks are: ", np.min(marks))
print("The max of marks are: ", np.max(marks))

print(np.zeros(5))
print(np.ones(5))
print(np.arange(0,6))
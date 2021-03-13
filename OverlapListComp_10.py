import random as rd

a = rd.sample(range(1,30), 12)
b = rd.sample(range(1,30), 12)

print(a,'\n', b)

matches = [i for i in a if i in b]
print(matches)
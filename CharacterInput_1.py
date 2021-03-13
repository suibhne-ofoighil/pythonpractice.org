#ask for the person's name & age
name = input('Hello World, what is your name? ----- ')
age = input('Hello ' + name + ', what is your age? ----- ')
number = input('How many times to repeat, master? ----- ')

year = 2020
birthYear = year - int(age)
hunderdBDay = birthYear + 100

lst = []

i = 0 
while i < int(number):
    i += 1
    entry = print(name, 'you will be 100 years old in the year:', hunderdBDay)
    lst.append(entry)

count = 0
for entry in lst:
    count +=1

print('Return printed', count, 'times!')
print(lst)

#calculate their birth year
#calculate the year of their 100th birthday

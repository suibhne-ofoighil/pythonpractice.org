with open('happynumbers.txt', 'r') as happynumbers:
    happynumbers = list(map(int,happynumbers.read().split()))

with open('primenumbers.txt', 'r') as primenumbers:
    primenumbers = list(map(int,primenumbers.read().split()))

shared  = [i for i in happynumbers if i in primenumbers]
print(shared)

# happy numbers test
def HappyNumberTest(number):
    happydigits = [x**2 for x in [int(i) for i in str(number)]]
    return(sum(happydigits))

number = input('Enter a number for happy number test ::::: ')
while True:
    entry  = input(':::::')
    if entry or number == 'no': break
    if number == 1: break
    number = HappyNumberTest(number)
    print(number)
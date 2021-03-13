number = input('What number foo? ---- ')
try: topRange = int(number)+1
except:
    print('Enter a number foo. ')
    break

x = list(range(1, topRange))

print(number, 'is divisable by:')

for num in x:
    if int(number) % num == 0:
        print(num)


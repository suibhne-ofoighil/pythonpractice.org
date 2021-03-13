import random as r

def password():
    length = int(input('How long do you want your password? --- '))
    password = ''.join([r.choice('1234567890-=qwerytioup[]]\|}{asdfjgjlh;"zxcvmnbm,.<>/?`~') for i in range(length)])
    return password

print('This is your password:', password())

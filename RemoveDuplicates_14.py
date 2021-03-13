import random as rd

# make a list of random numbers and length

def lster():
    lst = [rd.randint(1,30) for i in range(1,rd.randint(1,30))]
    print(lst)
    return lst

def setter(x):
    sett = []
    for i in x:
        if i not in sett:
            sett.append(i)
        else: continue
    return sett

print(setter(lster()))

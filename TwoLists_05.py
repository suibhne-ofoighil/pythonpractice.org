import random as r


def list_generator():
    length = int(input('How long is this list? (number) --- '))
    ranges = int(input('What is the range of this list? (number) --- '))
    a = [r.randint(1, ranges) for i in range(1, length)]
    return a

listnum = int(input('How many lists do you want? (number) --- '))

def list_maker(listnum, list_generator):
    n = 0 
    while n < listnum: 
        n +=1
        print('list number:', n)
        lst = str(n)
    # for i in lst:
    #     if i not in commons: 
    #         commons.append(i)
    #         print(commons)
    #     else: continue

print(commons)

# for i in lst:
#     for a in i:
#         if a in commons:
#             commons.append(a)
#         else: continue

print('these are the common numbers', commons)


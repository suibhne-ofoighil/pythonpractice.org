import requests as req

url = 'http://www.practicepython.org/assets/Training_01.txt'
headers = {'Accept-Encoding': 'identity'}
r = req.get(url, headers=headers)
x = r.text.split()
lst = []
for i in x: 
    bits = i.split('/')
    if len(bits) > 4: lst.append(bits[2] + '/' + bits[3])
    else: lst.append(bits[2])
    
counter_dict = {x:lst.count(x) for x in lst}
print(counter_dict)

for k,v in counter_dict.items():
    print('type:', k, '| count:', v)

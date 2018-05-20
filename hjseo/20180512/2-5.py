import sys

#1
a = {'name' : '홍길동', 'birth' : 1128, 'age' : 30}

#2
b = dict()
b['name'] = ['python']
b[('a',)] = 'python'
#a[[1]] = ['python'] --> List 객체는 mutable 이므로 dic의 key값으로 사용 X
b[250] = 'python'
print(b)

#3
c = {'A': 90, 'B': 80, 'C': 70}
print(c.get('B'))
del c['B']
print(c)

#4
d = {'A': 90, 'B': 80}
print(d.get('C', 70))

#5
e = {'A': 90, 'B': 80, 'C': 70}
idx = 0
minVal = 0
for key in list(e.keys()): 
    if idx == 0 :
        minVal = e.get(key)
    else :
  	    if minVal > e.get(key):
  	        minVal = e.get(key)
    idx = idx + 1

print('minVal: ',minVal)

#6
dic = {'A': 90, 'B': 80, 'C': 70}
rstArr = []
for key in list(dic.keys()):
    rstArr.append((key, dic.get(key)))

print(rstArr)




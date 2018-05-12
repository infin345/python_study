#1
print('"점프 투 파이썬 문제를 풀어보자"');

#2
print('''Life is Too short
You need Python''')

#3
print((' ' * 24) + 'PYTHON')

#4
num = '881120-1068234'.split('-')
print(num[0], num[1])

#5
pin = '881120-1068234'
print(pin.split('-')[1][0:1])

#6
txt = '1980M1120'
splitter = txt[4]
tmp = splitter + txt[0:4] + txt[5:]
txt = tmp
print(txt)

#7
print((' ' * 24) + "{txt}".format(txt='PYTHON'))

#8
print("Life is too short, you need python".index('short'))

#9
print('a:b:c:d'.replace(':', '#'))

#10
print('#'.join('a:b:c:d'.split(':')))
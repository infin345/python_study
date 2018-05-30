#1
sum = 0
for i in range(1, 100):
	sum = sum + i
print(sum)

#2
sum = 0
for i in range(1, 1000):
	if i % 5 ==0 :
		sum = sum + i
print(sum)

#3
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in list(A):
	sum = sum + i
print(sum / len(A))

#4
datas = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result = {}
for data in list(datas):
	result[data] = datas.count(data)
print(result)

#5
datas = [1, 2, 3, 4, 5]
result = [data * 2 for data in datas if data % 2 == 1]
print(result)

datas = "Life is too short, you need python"
excepts = ['a', 'e', 'i', 'o', 'u']
result = [datas.replace(data, "") for data in excepts if datas.find(data) > 0]
print(result)
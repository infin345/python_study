#1
print(all([1, 2, abs(-3)-3]))
# abs(-3)-3 -> 0(False)

print(chr(ord('a')) == 'a')

#2
data = {}
for i, x in enumerate(['a', 'b', 'c']):
	data[i] = x

print(data)

#3
print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

#4
print(int('0xea', 16))

#5
print(map(lambda x: x * 3, [1, 2, 3, 4]))

#6
data = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(data))
print(min(data))

#7
print(round(17 / 3), 4)

#8
print(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']))
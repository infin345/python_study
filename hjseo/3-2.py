#1
a=100
b=0
while(a > 0):
    b = b + a
    a = a - 1
print(b)

#2
a = 1000
b = 0
while(a > 1):
	if(a % 3 == 0):
		b = b + a
	a = a - 1
print(b)

#3
Ar = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
while(Ar):
	tmp = Ar.pop()
	if(tmp >= 50):
		result = result + tmp
print(result)

#4
a = 1
while(a < 6):
	print("*" * a)
	a = a + 1

#5
a = 7
while(a > 0):
	print("{0: ^10}".format("*" * a))
	a = a - 2
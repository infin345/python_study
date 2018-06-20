
# def sum_many(*args):
# 	print(args)

# result = sum_many(1,2,3)

# a = "100"[2:]
# print(a)
# result = ''.join(['clap' for a in range(1, 101) if str(a) in '369']) or i
# print(result)
# c = ['clap' for i in range(1, 101) if i in '369']
# print(c)
# [
# a = ''.join(['clap' for number in range(1, 101) if number in '369'])
# for i in range(1,101)

# ]

lst = "BD BR CD CN DE EG et FR ID IN ir jp KR MX NG PH PK RU TR US VN"
a = list(filter(lambda x:x.isupper(), lst.split()))

print(a)

a = ''.join(list(map(str.lower, lst)))

print(a)

a = ''.join(map(lambda x: x[0], lst.split()))


print(lst.split())
print(a)

import glob
print(glob.glob('*'))
print(dir(glob)[:17])

globals()



def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam) ##!

scope_test()
print("In global scope:", spam)


def gen():
    yield 10
    yield 20
    yield 30
    return x
print(gen())

a = (i for i in range(-10, 10) if i >= 0)
print(list(a))

def capwords(str):
	result = []
	_tmp = str.split()
	for val in _tmp:
		result.append(val.capitalize())
	return ' '.join(list(result))

print(capwords("abc dEf"))
#1
# str, int "+" oper not possible
try:
	"a" + 1
except TypeError as e:
	print(e)

# length exceed
try:
	a = [1, 2, 3]
	a[3]
except IndexError as e:
	print(e)

#2
# list object has minus index
a = [1, 2, 3]

try:
    result = a[-3]
except:
    print("error")
else:
    print("no error")

#3
# not exception -> go else
result = 3

try:
    result += 1
except:
    result += 2
else:
    result += 3
finally:
    result += 4

print(result)

#4
# (multi exception) occur all except and finally, not else
result = 0
try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
else:
    result += 4
finally:
    result += 5

print(result)
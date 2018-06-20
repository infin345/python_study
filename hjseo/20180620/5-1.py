#1
class Calculator:
	def __init__(self):
		self.value = 0

	def add(self, val):
		self.value += val

cal = Calculator()
cal.add(3)
cal.add(4)

print(cal.value)

#2
class Calculator2:
    def __init__(self, init_value):
        self.value = init_value

    def add(self, val):
        self.value += val

cal = Calculator2(2)
cal.add(3)
cal.add(4)

print(cal.value)

#3
class UpgradeCalculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    def minus(self, val):
    	self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

#4
class MaxLimitCalculator(Calculator):
	def add(self, value):
		self.value += value

		if self.value > 100:
			self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

#5
class ListCalculator:

	def __init__(self, list):
		self.list = list

	def sum(self):
		return sum(self.list)

	def avg(self):
		return sum(self.list) / len(self.list)


cal1 = ListCalculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = ListCalculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())
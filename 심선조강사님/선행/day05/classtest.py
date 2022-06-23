class Calculator:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result
    
    def setdata(self,first,second):
        self.first = first
        self.second = second

# cal1 = Calculator()
# cal2 = Calculator()
# print(cal1.result)
# print(cal2.result)
# print(cal1.add(5))
# print(cal1.add(3))
# print(cal1.result)
# print(cal2.result)

a = Calculator()
print(type(a))
a.setdata(4,2)
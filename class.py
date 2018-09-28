class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("my name is "+self.name+" and my age is " + str(self.age))

p1 = person("Ishi mishi",22)
p1.myfunc()

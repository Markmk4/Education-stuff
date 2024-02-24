class Programmer:
    def __init__(self, name, qual):
        self.name = name
        self.qual = qual
        self.time = 0
        self.salary = 0
        self.money_total = 0
        if self.qual == 'Junior':
            self.salary = 10
        elif self.qual == 'Middle':
            self.salary = 15
        elif self.qual == 'Senior':
            self.salary = 20
    def work(self, runtime):
        self.time += runtime
        self.money_total += runtime * self.salary
        return self.time

    def rise(self):
        if self.qual == 'Junior':
            self.qual = 'Middle'
            self.salary = 15
        elif self.qual == 'Middle':
            self.qual = 'Senior'
            self.salary = 20
        elif self.qual == 'Senior':
            self.salary += 1

    def info(self):
        return self.name, self.qual, self.time, self.money_total


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

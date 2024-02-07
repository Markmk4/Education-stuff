class Triangle:
    def __init__(self, first_side, second_side, third_side):
        self.first_side=first_side
        self.second_side = second_side
        self.third_side = third_side

    def show_correctness(self):
        if (self.first_side<=0 or self.second_side<=0 or self.third_side<=0):
            print("С отрицательными числами ничего не выйдет!")
            exit(1)

    def is_possible(self):
        if (self.first_side<(self.second_side+self.third_side)
            and self.second_side<(self.first_side+self.third_side)
            and self.third_side<(self.second_side+self.first_side)):
            print("Ура, можно построить треугольик!")
        else:
            print("С отрицательными числами ничего не выйдет!")

try:
    s1 = int(input())
    s2 = int(input())
    s3 = int(input())
    triangle1=Triangle(s1,s2,s3)
    triangle1.show_correctness()
except ValueError:
    print("Нужно вводить только числа!")
triangle1.is_possible()

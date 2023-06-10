# import random
# import statistics

# class Human:
#     def __init__(self, name, surname, age, grades):
#         self.name = name 
#         self.surname = surname
#         self.age = age
#         self.grades = grades
#     def __str__(self):
#         return f"Имя {self.name} {self.surname}, возраст {self.age} лет"
#     def greet(self):
#         return (f"Привет меня зовут {self.name} и мне {self.age} лет")
#     def __repr__(self):
#         return self.name
#     def avg_score(self):
#         return statistics.mean(self.grades)

# vasyan = Human("Vasya" , "Vasyanov" , 15, [])
# sergei = Human("Sergey" , "Sergeev", 32,[])
# vanya = Human("Vanya", "Nikitov", 66,[])
# leha = Human("Leha", "Anreev", 13,[])

# lst = [vasyan, sergei, vanya, leha]
# for i in lst:
#     i.grades = [random.randint(1,10) for j in range(10)]

# lst.sort(key= lambda y: y.avg_score())

# print(lst)
# print(vasyan.avg_score())
# print(vasyan)
# print (vasyan.greet())

class Rectandle():
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def get_a_cords(self):
        return [a.x, a.y, b.x, b.y]
    
    def area(self):
        return abs((b.x - a.x)*(a.y - b.y))
    
    def perimetr(self):
        return abs ((b.x - a.x) + (a.y - b.y))*2
    
    
    def has_point(self,point):
        if point.x < max(a.x, b.x) and point.y < max(a.y, b.y) and point.y > min (a.y, b.y) and point.x > min(b.x , a.x):
            return True
        else:
            return False

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Point(1,10)
b = Point(10,1)
tochka = Point(5,5)
tochka_2 = Point(0,0)
pryan = Rectandle(a,b)

print(pryan.area())
print(pryan.has_point(tochka_2))
print(pryan.has_point(tochka))


class Dragon():
    def __init__(self, height, fire_resist, color):
        self.height = height
        self.fire_resist = fire_resist
        self.color = color
    def __eq__(self, other):
        if (self.height == other.height) and (self.fire_resist == other.fire_resist) and (self.color == other.color):
            return True
        else:
            return False
    def __add__(self, other):
        import math
        color2 = min(self.color, other.color)
        height2 = math.floor((self.height + other.height)/2)
        fire_resist2 = max(self.fire_resist, other.fire_resist)
        dr2 = Dragon(height2, fire_resist2, color2)
        return(dr2)
    def __repr__(self) -> str:
        return f'Dragon {self.height}, {self.fire_resist}, {self. color} '
    def str(self):
        return f'Dragon with height {self.height}, danger {self.fire_resist} and color {self.color}'
    def change_color(self):
        new_color = input('Введите новый цвет: ')
        self.color = new_color
        return self
    def __sub__(self, number):
        number = int(input('Введите число: '))
        self.height = self.height - int(self.height / number)
        self.fire_resist = self.fire_resist + self.fire_resist % number
        return self
    def str1(self):
        string = input('Введите строку: ')
        print(string * self.fire_resist)
    
dr = Dragon(69, 5, 'brown')
dr1 = Dragon(69, 5, 'gray')
dr2 = dr+dr1
print(dr, dr1, dr2, sep="\n")




""" 
Класс "Автомобиль" и дочерний класс "Автобус". Экземпляр класса имеет координаты своего положения и угол, описывающий направление движения. 
Он может быть изначально поставлен в любую точку с любым направлением (конструктор), может проехать в выбранном направлении определенное расстояние
и может повернуть, то есть изменить текущее направление на любое другое. 
Реализуйте класс автомобиля, а также класс, который будет описывать автобус. Кроме того, что имеется у автомобиля, у автобуса должны быть поля, содержащие
число пассажиров и количество полученных денег, изначально равные 0. Также должны быть методы "войти" и "выйти", изменяющие число пассажиров. 
Наконец, метод move должен быть предопределен, чтобы увеличивать количество денег в соответствии с количеством пассажиров и пройденным расстоянием.
"""

class Automobile:
    def __init__(self, x, y, ugol1, ugol2):
        self.x = x
        self.y = y
        self.ugol1 = ugol1
        self.ugol2 = ugol2
    
    def drive(self, where_drive, x, y, ugol1, ugol2):
        self.x += where_drive
        self.y = (where_drive^2 + x^2)/ 2
        ugol1 = y/x
        ugol2 = 180 - 90 - ugol1 
        print(x, y, ugol2)

    def change_way(self):
        x -= where_drive
        y = -(where_drive^2 + x^2)/ 2


class Bus(Automobile):
    def __init__(self, x, y, people, money, price):
        self.people = people
        self.money = money

    def comein(self):
        self.people = 0
        self.people += 1
        print(self.people)
    
    def money_count(self):
        self.money = 0
        self.money = self.people
        self.price = money * people
        print(self.price)
        
    def comeout(self):
        self.people -= 1

    def move(self):
        self.price *= where_drive 

mashina1 = Automobile(0, 0)
mashina1.drive(6, 0, 0)
bus1 = Bus(0, 0, 0, 0, 50)
bus1.comein()
        

    



        


""""""
# №19 
# Есть Помидор со следующими характеристиками: Индекс, стадия зрелости(стадии: Отсутстствует, Цветение, Зеленый, Красный). 
# Помидор может: Расти(переходить на след. стадию зрелости), предоставлять информацию о своей зрелости(магический метод __str__). 
# Есть куcт с помидорами, который: Содержит список помидоров которые на нем растут. И может: Расти(добавляя томат), 
# Предоставлять инф-цию о зрелости всех томатов на нем, предоставлять урожай (убирать с себя все красные помидоры). 
# И также есть садовник, который имеет: Имя, Куст, за которым ухаживает. И может:
# Ухаживать за кустом (выводить  информацию о зрелости всех его помидоров), собирать урожай с куста. 

""""""

stages = ['None', 'Growing', 'Green', 'Red']
tomatoes = []

class Tomato:
    global stages, tomatoes
    def __init__(self, index, stage):
        self.index = index
        self.stage = stage
        
    def growth(self):
        ind = stages.index(self.stage)
        if ind < 3:
            self.stage = stages[ind + 1]

    def __str__(self):
        return f'Помидор {self.index}, на стадии {self.stage}'

class Bush:
    def __init__(self, tomatoes):
        self.tomatoes = tomatoes
    
    def add(self, index, stage):
        tomat = Tomato(index, stage)
        tomatoes.append([index, stage])
    
bush = Bush(tomatoes)
print(tomatoes)
bush.add(5, 'Growing')
print(tomatoes)




    
    

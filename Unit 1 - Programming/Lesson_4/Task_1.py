# Задание: Напишем класс Auto, в котором опишем свой автомобиль: пусть у автомобиля можно будет задать максимальную
# скорость, цвет, модель (поля класса). Создать конструктор, в котором по умолчанию цвет - красный, модель - bmv,
# максимальная скорость 200.
#
# Методы: поменять цвет машины, сменить максимальную скорость, вывести характеристики машины на экран, сменить модель.
#
# А затем создать несколько машин, применить к ним любые методы и вывести полученные результаты на экран.

class Auto:
    def __init__(self, color="red", model="BMW", speed=200):
        self.color=color
        self.model=model
        self.speed=speed

    def change_color(self, new_color):
        self.color=new_color
        print("Color is successfully changed")

    def change_speed(self, new_speed):
        self.speed=new_speed
        print("Maximum speed is successfully changed")

    def change_model(self, new_model):
        self.model=new_model
        print("Model is successfully changed")

    def tell(self):
        print("Car is ", self)
        print("Color is " , self.color)
        print("Model is " + self.model)
        print("Maximum speed is " + str(self.speed))

my_auto_1=Auto()
my_auto_2=Auto()
my_auto_1.tell()

new_color="yellow"
new_model="Jeep"
new_speed=180

my_auto_2.change_color(new_color)
my_auto_2.change_model(new_model)
my_auto_2.change_speed(new_speed)

my_auto_2.tell()
my_auto_1.tell()

print('Goodbye!')
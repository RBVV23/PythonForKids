# А теперь преобразовать наши методы для колеса, дворника и салона на новые:
# Заменить одно колесо или несколько
# Заменить один дворник или несколько
# Заменить одно кресло в салоне или несколько
# А также написать метод, который принимает список именованных аргументов с новыми значениями
# и вызывает сеттеры для них.
# Например, если он принимает мотор и коробку передач, то заменить имеющийся мотор на новый и коробку передач тоже.


class Auto:
    def __init__(self, color="red", model="BMW", speed=200, wheels=[17, 17, 19, 19],
                 wipers=['left', 'broken'], seats=['d', 'p', 'p', 'p', 'p'], motor="V8",
                 win=0, transmission="automatic"):
        self.color = color
        self.model = model
        self.speed = speed
        self.wheels = wheels
        self.wipers = wipers
        self.seats = seats

        self._motor = motor
        self._win = win
        self._transmission = transmission

    def change_color(self, new_color):
        self.color = new_color
        print("Color is successfully changed")

    def change_speed(self, new_speed):
        self.speed = new_speed
        print("Maximum speed is successfully changed")

    def change_model(self, new_model):
        self.model = new_model
        print("Model is successfully changed")

    def change_wheel(self, new_wheel, number):
        self.wheels[number] = new_wheel
        print("Wheel #", str(number+1), " is successfully changed")

    def change_wiper(self, new_wiper, number):
        self.wipers[number] = new_wiper
        print("Wiper #", str(number+1), " is successfully changed")

    def change_seat(self, new_seat, number):
        self.seats[number] = new_seat
        print("Seat #", str(number+1), " is successfully changed")

    def get_motor(self):
        return self._motor

    def set_motor(self, new_motor):
        self._motor = new_motor

    def get_win(self):
        return self._win

    def set_win(self, new_win):
        self._win = new_win

    def get_transmission(self):
        return self._transmission

    def set_transmission(self, new_transmission):
        self._transmission = new_transmission

    def tell(self):
        print("Car is ", self)
        print("Color is ", self.color)
        print("Model is " + self.model)
        print("Maximum speed is " + str(self.speed))
        print("Wheels formula is ", self.wheels)
        print("Wipers formula is ", self.wipers)
        print("Seats formula is ", self.seats)
        print("Motor is ", self.get_motor())
        print("Win number is ", self.get_win())
        print("Transmission is ", self.get_transmission())


my_auto_1 = Auto()
my_auto_2 = Auto()
my_auto_1.tell()

new_color = "yellow"
new_model = "Jeep"
new_speed = 180
new_motor = "V6"
new_win = 1
new_transmission = "robot"
new_wheel = 19
new_wiper = "right"
new_seat = 'p+'

my_auto_2.change_color(new_color)
my_auto_2.change_model(new_model)
my_auto_2.change_speed(new_speed)

my_auto_2.change_wheel(new_wheel, 0)
my_auto_2.change_wheel(new_wheel, 1)
my_auto_2.change_wiper(new_wiper, 1)
my_auto_2.change_seat(new_seat, 1)

my_auto_2.set_motor(new_motor)
my_auto_2.set_win(new_win)
my_auto_2.set_transmission(new_transmission)

my_auto_2.tell()

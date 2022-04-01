# У нас уже есть машина! Но нам этого мало. Мы хотим еще и покорять дороги на мотоцикле!
# В этом деле главное безопасность. Нам понадобится защитная экипировка: шлем, наколенники и налокотники.
# Мы создадим классы для шлема, наколенников и налокотников.
# А затем класс защитной экипировки, в котором полями класса будут созданы шлем, наколенники и налокотники.
# *Во всех классах используем метод который перекрашивает вещь, меняет характеристики (например цвет или модель).


class Helmet:
    def __init__(self, model="base", color=""):
        self._model = model
        self.color = color

    def repaint(self, new_color):
        self.color = new_color
        print("Color is successfully changed")

    def get_model(self):
        return self._model

    def set_model(self, new_model):
        self._model = new_model
        print("Model is successfully changed")

    def tell(self):
        print(f'Model of this helmet is {self._model}')
        print(f'This helmet is {self.color}')


class Elbowpad:
    def __init__(self, model="base", color="none"):
        self._model = model
        self.color = color

    def repaint(self, new_color):
        self.color = new_color
        print("Color is successfully changed")

    def get_model(self):
        return self._model

    def set_model(self, new_model):
        self._model = new_model
        print("Model is successfully changed")

    def tell(self):
        print(f'Model of this elbow pad is {self._model}')
        print(f'This elbow pad is {self.color}')


class Kneepad:
    def __init__(self, model="base", color="none"):
        self._model = model
        self.color = color

    def repaint(self, new_color):
        self.color = new_color
        print("Color is successfully changed")

    def get_model(self):
        return self._model

    def set_model(self, new_model):
        self._model = new_model
        print("Model is successfully changed")

    def tell(self):
        print(f'Model of this knee pad is {self._model}')
        print(f'This knee pad is {self.color}')


class Equipment:
    def __init__(self, head=Helmet(), knee=Kneepad(), elbow=Elbowpad()):
        self.head = head
        self.knee = knee
        self.elbow = elbow

    def head_on(self, new_head=Helmet()):
        self.head = new_head

    def knee_on(self, new_knee=Kneepad()):
        self.knee = new_knee

    def elbow_on(self, new_elbow=Elbowpad()):
        self.elbow = new_elbow

    def tell(self):
        print("This Equipment includes:")
        self.head.tell()
        self.knee.tell()
        self.elbow.tell()


my_helmet = Helmet()
my_color = "red"
my_model = "progressive"
your_helmet = Helmet("oldfashion", "blue")
your_kneepad = Kneepad("oldfashion", "blue")
your_elbowpad = Elbowpad("oldfashion", "blue")

your_helmet.tell()
my_helmet.repaint(my_color)
my_helmet.set_model(my_model)

my_elbowpad = Elbowpad("safety", "red")
my_elbowpad.tell()

my_kneepad = Kneepad("safety", "red")
my_kneepad.tell()

print("________________________________________")

my_equipment = Equipment(my_helmet, my_kneepad, my_elbowpad)
my_equipment.tell()

my_equipment.head_on(your_helmet)
my_equipment.knee_on(your_kneepad)
my_equipment.elbow_on(your_elbowpad)
my_equipment.tell()

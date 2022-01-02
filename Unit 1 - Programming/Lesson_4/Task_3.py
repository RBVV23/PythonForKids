#У нас уже есть машина! Но нам этого мало. Мы хотим еще и покорять дороги на мотоцикле!
#В этом деле главное безопасность. Нам понадобится защитная экипировка: шлем, наколенники и налокотники.
#Мы создадим классы для шлема, наколенников и налокотников.
# А затем класс защитной экипировки, в котором полями класса будут созданы шлем, наколенники и налокотники.
#*Во всех классах используем метод который перекрашивает вещь, меняет характеристики (например цвет или модель).


class helmet:
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
        print("Model is successfuly changed")

    def tell(self):
        print("Model of this helmet is", self._model)
        print("This helmet is", self.color)
class elbowpad:
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
        print("Model is successfuly changed")

    def tell(self):
        print("Model of this elbow pad is", self._model)
        print("This elbow pad is", self.color)
class kneepad:
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
        print("Model is successfuly changed")

    def tell(self):
        print("Model of this knee pad is", self._model)
        print("This knee pad is", self.color)

class equipment:
    def __init__(self, head=helmet(), knee=kneepad(), elbow=elbowpad()):
        self.head=head
        self.knee=knee
        self.elbow=elbow

    def head_on(self, new_head=helmet()):
        self.head=new_head
    def knee_on(self, new_knee=kneepad()):
        self.knee=new_knee
    def elbow_on(self, new_elbow=elbowpad()):
        self.elbow=new_elbow

    def tell(self):
        print("This equipment includes:")
        self.head.tell()
        self.knee.tell()
        self.elbow.tell()

my_helmet = helmet()
my_color="red"
my_model="progressive"
your_helmet = helmet("oldfashion", "blue")
your_kneepad = kneepad("oldfashion", "blue")
your_elbowpad = elbowpad("oldfashion", "blue")

your_helmet.tell()
my_helmet.repaint(my_color)
my_helmet.set_model(my_model)

my_elbowpad=elbowpad("safety", "red")
my_elbowpad.tell()

my_kneepad=kneepad("safety", "red")
my_kneepad.tell()

print("________________________________________")

my_equipment=equipment(my_helmet, my_kneepad, my_elbowpad)
my_equipment.tell()

my_equipment.head_on(your_helmet)
my_equipment.knee_on(your_kneepad)
my_equipment.elbow_on(your_elbowpad)
my_equipment.tell()
import codecs
clients = codecs.open('clients.txt', 'r', 'utf-8')
courses = codecs.open('catalog.txt', 'r', 'utf-8')


class COURSE:
    def __init__(self, subject="Сareer guidance", price=int(4500), tutor="Igor A.", pupils=[]):
        self.subject = subject
        self.price = price
        self.tutor = tutor
        self._pupils = pupils
        self.number = len(self._pupils)

    def info(self):
        print(f'Course:\t\t{self.subject}')
        print(f'Tutor:\t\t\t{self.tutor}')
        print(f'Number of pupils:\t{self.number}')
        print(f'Price: {self.price}')

    def _sp_info(self):
        print(f'Course:\t\t{self.subject}')
        print(f'Tutor:\t\t\t{self.tutor}')
        print(f'Number of pupils:\t{self.number}')
        print(f'List of pupils: {self._pupils}')


class CLIENT:
    def __init__(self, id=0, name="Igor", surname="Alekseev", account=int(15000), subject="none"):
        self.id = id
        self.name = name
        self.surname = surname
        self._account = account
        self.subject = subject

    def info(self):
        # print("ID number: " + "\t" + str(self.id))
        print(f'Name:\t\t{self.name}')
        print(f'Surname:\t{self.surname}')
        print(f'Subject:\t{self.subject}')

    def _sp_info(self):
        print(f'ID number:\t{self.id}')
        print(f'Name:\t\t{self.name}')
        print(f'Surname:\t{self.surname}')
        print(f'Subject:\t{self.subject}')
        print(f'Account:\t{self._account}')


def sale(pupil=CLIENT(), course=COURSE()):
    pupil._account = pupil._account - course.price
    pupil.subject = course.subject
    course.number = course.number + 1
    course._pupils.append(pupil.surname)


course_base = list()
client_base = list()

#  "прогрузка" базы курсов
for line in courses:
    words = line.split()
    course = COURSE()
    course.subject = words[0]
    course.price = int(words[1])
    course.number = int(words[2])
    course.tutor = f'{words[3]} {words[4]}'
    course_base.append(course)

i = 0
#  "прогрузка" базы клиентов
for line in clients:
    i = i + 1
    words = line.split()
    student = CLIENT()
    student.id = i
    student.name = words[0]
    student.surname = words[1]
    client_base.append(student)


sale(client_base[0], course_base[1])
sale(client_base[3], course_base[1])

# Создадим строку с фразой “Я у мамы программист” и
# выведем ее на экран сначала в нормальном порядке, а затем в обратном

string = 'Я у мамы программист'

print('Прямой порядок:')
for i in range(len(string)):
    print(string[i])

print('Обратный порядок:')
for i in range(len(string)-1, -1, -1):
    print(string[i])

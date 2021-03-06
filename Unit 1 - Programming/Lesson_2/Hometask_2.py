# Описание: У бананового монстра есть свой запас любимых слов (массив).
# Он любит хоть и монстр, но любит играть. Делает он это так: он выбирает случайное слово
# из своего набора и показывает, сколько в нем букв. При этом он дает 7 попыток его отгадать.
# Он просит пользователя ввести с клавиатуры буквы и если она есть в загаданном слове, то он выводит
# это слово с полученной буквой на своем месте, а если нет, то у пользователя сгорает одна жизнь.

# Задание: Напиши программу, которая будет играть с пользователем по
#  правилам бананового монстра.


from random import randint


massive = [
    'кочерга',
    'молоко',
    'конь',
    'парабола',
    'крест',
    'катастрофа',
    'выбор',
]

print('Привет, я Банановый Монстр и хочу сграть с тобой в одну игру!')

health = 7
N = randint(0, 6)
word = massive[N]
L = len(word)

print(f'Я загадал слово из {L} букв.')
print(word)
print('Отгадай его!')
print()
answer = '*'*L
flag = 0

while health != 0 and flag != 1:
    print(f'Мое слово: {answer}')
    print(f'Количество попыток: {health}')
    print('Твоя буква: ')
    letter = str(input())
    while len(letter) != 1:
        print('Нужно ввести один символ!')
        print('Попробуй еще разок: ')
        letter = str(input())

    if letter in word:
        index = word.find(letter)
        while index != -1:
            answer = answer[:index] + letter + answer[index+1:]
            index = word.find(letter, index+1)
        if word == answer:
            flag = 1
    else:
        print('Такой буквы нет в моем слове!')
        health = health-1

if flag == 1:
    print(f'Правильно, мое слово - {word}')
    print('Поздравляю, ты победил!')
    print(f'Количество оставшихся попыток: {health}')
else:
    print('К сожалению, у тебя не осталось больше попыток - ты проиграл')
    print(f'Мое слово было: {word}')
    print(f'У тебя получилось только: {answer}')

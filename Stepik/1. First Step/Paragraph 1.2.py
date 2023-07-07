# python 3.6.9

'''
Прежде чем запустить программу,
нажмите на кнопку Show input и заранее введите входные данные!
'''

a = int(input())
b = input()
print('a * "b" = {}'.format(a * b))
print('a * b = {}'.format(a * int(b)))
print('a * "b" = {0}; a * b = {1}'.format(format(a * b), a * int(b)))

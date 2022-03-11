# Описание: Робот Ваня начинающий поэт. Но на его планете стихи воспринимают только если строчки написаны задом
# наперед. Ваня хитрец, он берет стихи русских классиков и переворачивает их, чтобы поразить свою возлюбленную Мэри.
# Но ему очень не хочется делать это вручную и он хочет написать программу, которая бы делала это автоматически.
#
# Задание: Написать программу, которая будет читать с одного файла стих, а в другой файл записывать этот стишок задом
#  наперед.

import codecs
file = codecs.open('read.txt', 'r', 'utf-8')

words = []
mega_str=[]
long_str=[]


for line in file:
    print(line)
    words=line.split()
    words.reverse()
    str_inv=''
    for i in range(0, len(words)):
        str_inv=str_inv + words[i] + ' '
    mega_str.append(str_inv)

file.close
mega_str.reverse()

file_out=open('write.txt', 'w')

for word in mega_str:
    print(word)
    file_out.write(word + '\n')

file_out.close

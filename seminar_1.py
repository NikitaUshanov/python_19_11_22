import pandas as pd
import csv
import datetime
import time


# task_1
'''
Напишите программу, которая будет открывать определенный файл CSV и выводить на печать построчно последние 10 строк. 
Если в файле всего 10 и меньше строк, то нужно вывести только первую строчку.
'''

def check_file(path):
    df = pd.read_csv(path)
    if len(df) >= 10:
        print(df.tail())
    else:
        print(df.head(1))

check_file('prices22.csv')


# task_2
'''
Создать текстовый файл File_txt.txt. В него первой строкой записать свою группу, ФИО. 
Вторая строка – четные числа от 0 до 100. Числа должны быть разделены «;».
'''
with open('File_txt.txt', 'w') as text_file:
    text_file.write('Ushanov Nikita, PUOR22-2m \n')

with open('File_txt.txt', 'a') as text_file:
    text_file.write(arr = "; ".join(map(str, list(range(0, 100, 2)))))
 

# task_3
'''
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать
построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
'''
def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
    else:
          print('Параметр "lines" должен быть больше 0!')
            

# task_4
'''
Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
'''
def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
        else:
            return sought_words
        
        
# task_5
'''
Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
– № - номер по порядку (от 1 до 300);
– Секунда – текущая секунда на вашем ПК;
– Микросекунда – текущая миллисекунда на часах.
На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
'''
with open('rows_300.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)

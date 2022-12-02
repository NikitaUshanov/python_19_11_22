import pandas as pd



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


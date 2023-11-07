from Note import *
import os
from datetime import datetime



n1 = Note('f1.csv')
n2 = Note('f2.csv')  
n3 = Note('f3.csv', title = "Title file 3")  
n4 = Note('f4.csv')  
n5 = Note('f5.csv')  
n2.addText('my file;my file;********')
n3.addText('my file 3;my file;********')
n4.addText('my file 4;my file;********')
Note_list = [n1, n2, n3, n4, n5]
print(n1.getDateTime())



while True:
    print("""Возможные команды:\n
        '1' - создать заметку
        '2' - изменить заметку
        '3' - показать список всех заметок
        '4' - удалить заметку
        '5' - вывести список заметок по дате последнего редактирования
        '6' - показать содержимое заметки
        '7' - закончить """)
    k = input()
    if k == '1':
        name = input('Введите название заметки ')
        note = Note(name + '.csv')
        kk = input('Хотите сразу добавить текст? (введите да/нет) ')
        if kk == "да":
            note.addText(input('Введите текст заметки'))
        Note_list.append(note)
    elif k == '2':
        n = input('Введите название заметки ')
        for i in Note_list:
            if i.getNoteName() == n + '.csv':
                i.changeNote()
                i.setDateTime()
    elif k == '3':
        for i in range(len(Note_list)):
            print(f'Заметка № {Note_list[i].getIndex()}: {Note_list[i].getNoteName()} - Последнее изменение - {Note_list[i].getDateTime()}')
        print()
    elif k == '4':
        n = input('Введите название заметки ')
        for i in range(len(Note_list) - 1):
            if Note_list[i].getNoteName() == n + '.csv':
                del Note_list[i]
                os.remove(n + '.csv')
                print(f"Файл {n} удалён.")

    elif k == '5':
        print('Введите нужную дату')
        d = int(input("Число месяца: "))
        m =  int(input("Номер месяца: "))
        y = int(input("Номер года: "))
        print(f'Заметки от {d}.{m}.{y}:')
        for i in Note_list:
            if i.getDateTime().day == d and i.getDateTime().month == m and i.getDateTime().year == y:
                print(f'Заметка № {i.getIndex()}: {i.getNoteName()} - Последнее изменение - {i.getDateTime()}')
        print('-----------------')
    elif k == '6':
        n = input('Введите название заметки ')
        for i in Note_list:
            if i.getNoteName() == n + '.csv':
                print(i.getText())
    elif k == '7':
        break
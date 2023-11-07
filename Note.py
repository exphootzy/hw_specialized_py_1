from datetime import datetime
import csv


index = 1
class Note:
    global index
    def __init__(self, name, title='Title') -> None:
        global index
        self.name = name
        self.Title = title
        self.ind = index
        index += 1
        self.dateTime = datetime.now()

        try:
            self.file = open(self.name, "w")
            self.writer = csv.writer(self.file)
            self.writer.writerow([title])
            self.file.close()
            
        except:
            print('error')
    
    def addText(self, text):
        self.file = open(self.name, "a")
        self.writer = csv.writer(self.file, delimiter=';')
        self.writer.writerow(text.split(';'))
        self.file.close()
    
    def getNoteFile(self):
        return self.file
    
    def getNoteName(self):
        return self.name
    
    def setDateTime(self):
        self.dateTime = datetime.now()
    
    def getDateTime(self):
        return self.dateTime
    
    def getIndex(self):
        return self.ind
    
    def getText(self):
        self.file = open(self.name, "r")
        return self.file.read()
        self.file.close()
    
    def changeNote(self):
        try:
            print('''Команды:
                '1' - добавить текст в конец файла
                '2' - полностью обновить содержимое
                ''')
            k = input()
            if k == '1':
                self.file = open(self.name, "a")
                self.writer = csv.writer(self.file, delimiter=';')
                text = input('Введите текст для добавления через')
                self.writer.writerow([text])
                self.file.close()
            elif k == '2':
                self.file = open(self.name, "w")
                self.writer = csv.writer(self.file, delimiter=';')
                title = input("Введите заголовок: ")
                self.writer.writerow([title])
                self.Title = title
                text = input('Введите текст для добавления через')
                self.writer.writerow([text])
                self.file.close()
                print("Операция прошла успешно")
        except:
            print('error redacting')

        def __str__(self):
            return self.name
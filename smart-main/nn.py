from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction )
from PyQt5.QtGui import QKeySequence

import json
import os

def writeToFile():
    with open("notes.json","w",encoding='utf=8') as file:
        json.dump(notes,file,sort_keys=True)
        
with open("notes.json", "r",encoding='utf=8') as file:
    notes= json.load(file)
    
app = QApplication([])
window = QWidget()
main_width, main_height = 800,600

text_editor= QTextEdit()
text_editor.setPlaceholderText("Введіть текст ....")

list_widget_1 = QListWidget()
list_widget_1.setStyleSheet('background-color: pink;')

list_widget_2 = QListWidget()
list_widget_2.setStyleSheet('background-color: pink;')

text_searcher = QLineEdit()
text_searcher.setPlaceholderText("Введіть текст .... ")
text_searcher.setStyleSheet('background-color: green;')

input_dialog = QLineEdit()
input_dialog.setPlaceholderText("Введіть тег .... ")
input_dialog.setStyleSheet('background-color: green;')

make_note= QPushButton()
make_note.setStyleSheet('background-color: green;')
make_note.setText("Створити замітку")

delete_note= QPushButton()
delete_note.setStyleSheet('background-color: green;')
delete_note.setText("Видалити замітку")

save_note= QPushButton()
save_note.setStyleSheet('background-color: green;')
save_note.setText("Зберегти замітку")

search_for_text =QPushButton()
search_for_text.setStyleSheet('background-color: green;')
search_for_text.setText("Шукати замітку по тексту")

search_for_note =QPushButton()
search_for_note.setStyleSheet('background-color: green;')
search_for_note.setText("Шукати замітку за тегом")

add_to_note = QPushButton()
add_to_note.setStyleSheet('background-color: green;')
add_to_note.setText("Додати до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('background-color: green;')
unpin_to_note.setText("Відкріпити від замітки")

action_theme_btn = QPushButton()
action_theme_btn.setText("Змінити тему на чорну")
action_theme_btn.setStyleSheet("background-color: pink;")

export_as_text = QPushButton()
export_as_text.setText("Конвертувати у txt")

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2= QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1= QVBoxLayout()
col1.addWidget(text_editor)

col2= QVBoxLayout()
col2.addWidget(QLabel("Список питать"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
col2.addWidget(QLabel("Список тегів"))
col2.addWidget(list_widget_2)
col2.addWidget(input_dialog)
col2.addWidget(text_searcher)
col2.addLayout(row2)
col2.addWidget(search_for_note)
col2.addWidget(search_for_text)
col2.addWidget(export_as_text)
col2.addWidget(action_theme_btn)

layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

def change_theme():
    if action_theme_btn.text() == 'Змінити тему на чорну':
        window.setStyleSheet(' background-color:black;color:white;font-size:20px; border: 1px solid white;')
        text_editor.setStyleSheet('background-color:black;color:white;')
        list_widget_1.setStyleSheet(' background-color:black;color:white;')
        list_widget_2.setStyleSheet(' background-color:black;color:white;')
        unpin_to_note.setStyleSheet(' background-color:black;color:white;')
        add_to_note.setStyleSheet(' background-color:black;color:white;')
        make_note.setStyleSheet(' background-color:black;color:white;')
        delete_note.setStyleSheet(' background-color:black;color:white;')
        search_for_note.setStyleSheet(' background-color:black;color:white;')
        search_for_text.setStyleSheet(' background-color:black;color:white;')
        input_dialog.setStyleSheet(' background-color:black;color:white;')
        export_as_text.setStyleSheet(' background-color:black;color:white;')
        save_note.setStyleSheet(' background-color:black;color:white;')
        action_theme_btn.setText('Змінити тему на білу')
    elif action_theme_btn.text() == 'Змінити тему на білу':
        window.setStyleSheet(' background-color:white;color:black;font-size:20px; border: 1px solid black;')
        text_editor.setStyleSheet('background-color:white;color:black;')
        list_widget_1.setStyleSheet(' background-color:white;color:black;')
        list_widget_2.setStyleSheet('background-color:white;color:black;')
        unpin_to_note.setStyleSheet('background-color:white;color:black;')
        add_to_note.setStyleSheet('background-color:white;color:black;')
        make_note.setStyleSheet('background-color:white;color:black;')
        delete_note.setStyleSheet('background-color:white;color:black;')
        search_for_note.setStyleSheet('background-color:white;color:black;')
        search_for_text.setStyleSheet('background-color:white;color:black;')
        input_dialog.setStyleSheet('background-color:white;color:black;')
        export_as_text.setStyleSheet('background-color:white;color:black;')
        save_note.setStyleSheet('background-color:white;color:black;')
        action_theme_btn.setText('Змінити тему на чорну')

def sergio():
    if action_theme_btn.text() == "Змінити тему на чорну":
        list_widget_1.setStyleSheet("background-color:black; color:red")
        list_widget_2.setStyleSheet("background-color:black; color:red")
        text_editor.setStyleSheet("background-color:black; color:red")
        text_searcher.setStyleSheet("background-color:black; color:red")
        input_dialog.setStyleSheet("background-color:black; color:red")
        make_note.setStyleSheet("background-color:black; color:red")
        delete_note.setStyleSheet("background-color:black; color:red")
        save_note.setStyleSheet("background-color:black; color:red")
        search_for_text.setStyleSheet("background-color:black; color:red")
        search_for_note.setStyleSheet("background-color:black; color:red")
        add_to_note.setStyleSheet("background-color:black; color:red")
        unpin_to_note.setStyleSheet("background-color:black; color:red")
        export_as_text.setStyleSheet("background-color:black; color:red")
        action_theme_btn.setStyleSheet("background-color:black; color:red")
        window.setStyleSheet('background-color: pink; font-size:20px')
        action_theme_btn.setText("Змінити на розовий")
    elif action_theme_btn.text() == "Змінити на розовий":
        list_widget_1.setStyleSheet("background-color:pink; color:red")
        list_widget_2.setStyleSheet("background-color:pink; color:red")
        text_editor.setStyleSheet("background-color:pink; color:red")
        text_searcher.setStyleSheet("background-color:pink; color:red")
        input_dialog.setStyleSheet("background-color:pink; color:red")
        make_note.setStyleSheet("background-color:pink; color:red")
        delete_note.setStyleSheet("background-color:pink; color:red")
        save_note.setStyleSheet("background-color:pink; color:red")
        search_for_text.setStyleSheet("background-color:pink; color:red")
        search_for_note.setStyleSheet("background-color:pink; color:red")
        add_to_note.setStyleSheet("background-color:pink; color:red")
        unpin_to_note.setStyleSheet("background-color:pink; color:red")
        export_as_text.setStyleSheet("background-color:pink; color:red")
        action_theme_btn.setStyleSheet("background-color:pink; color:red")
        window.setStyleSheet('background-color: pink; font-size:20px')
        action_theme_btn.setText("Змінити тему на чорну")
        
    
    

def show_notes():
    global key
    key = list_widget_1.selectedItems()[0].text()
    list_widget_2.clear()
    text_editor.setText(notes[key]["text"])
    list_widget_2.addItems(notes[key]["tag"])

def delete_note_1():
    key= list_widget_1.selectedItems()[0].text()
    if key in notes:
        notes.pop(key)
        list_widget_1.clear()
        list_widget_2.clear()
        list_widget_1.addItems(notes)
        writeToFile()

# def save_note_def():
#     if list_widget_1.currentItem():
#         key = list_widget_1.currentItem().text()
#         new_text_note =text_editor.toPlainText()
#         notes[key]["текст"] = new_text_note
#         writeToFile()

def add_mynote():
    note_name, ok = QInputDialog.getText(window,"Додати нотатку","Назва")
    if note_name and ok:
        list_widget_1.addItem(note_name)
        notes[note_name] = {"text" : " " , "tag" : [ ]}
    writeToFile()
        

def add_mytag():
    key = list_widget_1.selectedItems()[0].text()
    if key in notes:
        tag_name, ok = QInputDialog.getText(window,"Додати тег до нотатки","Назва:")
        if tag_name and ok:
            notes[key]["tag"].append(tag_name)
            writeToFile()
        list_widget_2.clear()
        list_widget_2.addItems(notes[key]["tag"])

def delete_tag():
    key= list_widget_1.selectedItems()[0].text()
    if key in notes:
        current_item = list_widget_2.currentItem()
        if current_item:
            tag_name = current_item.text()
            notes[key]["tag"].remove(tag_name)
            writeToFile()
        list_widget_2.clear()
        list_widget_2.addItems(notes[key]["tag"])
list_widget_1.addItems(notes)
list_widget_1.itemClicked.connect(show_notes)
# delete_note.clicked.connect(delete_note_1)
# save_note.clicked.connect(save_note_def)
make_note.clicked.connect(add_mynote)
add_to_note.clicked.connect(add_mytag)
action_theme_btn.clicked.connect(sergio)

window.setStyleSheet('background-color: yellow; font-size:20px')
window.setLayout(layout_note)
window.resize(main_width,main_height)
window.show()
app.exec_()

def search_note():
    tag = input_dialog.text()
    if search_for_note.text() == 'Шукати замітки за тегом':
        filtered_notes = {}
        for key in notes:
            if tag in notes[key]['теги']:
                filtered_notes[key] = notes[key]
        search_for_note.setText('Скинути пошук')

        list_widget_1.clear()
        list_widget_2.addItems(filtered_notes)
        list_widget_2.clear()
        text_editor.clear()


    elif search_for_note.text() == 'Скинути пошук':
            search_for_note.setText('Шукати замітки за тегом')
            list_widget_1.clear()
            list_widget_1.addItems(filtered_notes)
            list_widget_2.clear()
            text_editor.clear()
            input_dialog.clear()
def search_note_for_text():
    tag = text_editor.text()
    if search_for_note.text() == 'Шукати замітки за текстом':
        filtered_notes = {}
        for key in notes:
            if tag in notes[key]['text']:
                filtered_notes[key] = notes[key]
        search_for_note.setText('Скинути пошук')

        list_widget_1.clear()
        list_widget_2.addItems(filtered_notes)
        list_widget_2.clear()
        text_editor.clear()


    elif search_for_note.text() == 'Скинути пошук':
            search_for_note.setText('Шукати замітки за тегом')
            list_widget_1.clear()
            list_widget_1.addItems(filtered_notes)
            list_widget_2.clear()
            text_editor.clear()
            input_dialog.clear()
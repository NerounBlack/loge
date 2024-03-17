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
    with open ("notes.json", "w") as file:
        json.dump(notes, file, sort_keys=True)

with open("notes.json", "r", encoding = 'utf=8') as file:
    notes = json.load(file)

app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600



text_editor = QTextEdit()
text_editor.setStyleSheet('background-color: red;')
text_editor.setPlaceholderText("Введіть текст")

list_widget_1 = QListWidget()
list_widget_1 

list_widget_2 = QListWidget()
list_widget_2.setStyleSheet('background-color: black;')

text_searcher = QLineEdit()
text_searcher.setPlaceholderText("Введіть текст")
text_searcher.setStyleSheet('background-color: green;')

input_dialog = QLineEdit()
input_dialog.setPlaceholderText("Введіть тег")
input_dialog.setStyleSheet('background-color: green;')

make_note = QPushButton()
make_note.setStyleSheet('background-color: blue;')
make_note.setText("Створити замітку")

delete_note = QPushButton()
delete_note.setStyleSheet('background-color: brown;')
delete_note.setText("Видалити замітку")

save_note = QPushButton()
save_note.setStyleSheet('background-color: orange;')
save_note.setText("Зберегти замітку")

search_for_text = QPushButton()
search_for_text.setStyleSheet('background-color: magenta;')
search_for_text.setText("Шукати замітку по тексту")

search_for_note = QPushButton()
search_for_note.setStyleSheet('background-color: purple;')
search_for_note.setText("Шукати замітку за тегом")

add_to_note = QPushButton()
add_to_note.setStyleSheet('background-color: burgundy;')
add_to_note.setText("Додати до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('background-color: lilac;')
unpin_to_note.setText("Відкріпити від замітки")

action_theme_btn = QPushButton()
action_theme_btn.setStyleSheet('background-color: black;')

export_as_txt = QPushButton()
export_as_txt.setText("Конвертувати txt")

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список питань"))
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
col2.addWidget(export_as_txt)
col2.addWidget(action_theme_btn)

layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)


window.setLayout(layout_note)
window.setStyleSheet('background-color: yellow; font-size:20px')
window.resize(main_width,main_height)
window.show()
app.exec_()

def show_notes():
    global key
    list_widget_1.addItems(notes)
    key = list_widget_1.selectedItems()[0]. text()
    list_widget_2.clear()
    text_editor.setText(notes[key]["текст"])
    list_widget_2.addItems(notes[key]["теги"])

def delete_note_():
    key = list_widget_1.selectedItems()[0].text()
    if key in notes:
        notes.pop(key)
        list_widget_1.clear()
        list_widget_2.clear()
        list_widget_1.addItems(notes)
        writeToFile()

def save_note_def():
    if list_widget_1.currentItem():
        key = list_widget_1.currentItem().text()
        new_text_note = text_editor.toPlainText()
        notes[key]["текст"] = new_text_note
        writeToFile()

def add_mynote():
    note, ok = QInputDialog.getText(window,"Додати нотатку","NAME")
    if note and ok:
        list_widget_1.addItem(note)
        notes[note] = {"текст" : ""  , "теги" : []}
        writeToFile()


list_widget_1.addItems(notes)
list_widget_1.itemClicked.connect(show_notes)
window.setStyleSheet('background-color: yellow; font-size:20px')
delete_note.clicked.connect(delete_note_)
save_note.clicked.connect(save_note_def)
make_note.clicked.connect(add_mynote)






list_widget_1.addItems(notes)
list_widget_1.itemClicked.connect(show_notes)

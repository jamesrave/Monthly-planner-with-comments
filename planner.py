#!/usr/bin/env python3
# Monthly Planner

import tkinter as tk
import tkinter.filedialog as tkFileDialog

# Создание основного окна
root = tk.Tk()
root.title("Monthly Planner")  # Название окна
root.geometry("514x616")  # Размеры окна
root.option_add("*Font", "TkDefaultFont 9")  # Установка шрифта по умолчанию

my_entries = []  # Список для хранения ссылок на поля ввода

# Заголовок
lab = tk.Label(root, text="", font='Arial 10 bold')
lab.grid(column=0, row=0, padx=12, pady=0, sticky='w')

# Поле для имени
name_label = tk.Label(root, text="Name:")  # Метка для имени
name_label.grid(column=0, row=1, padx=12, pady=4, sticky='nw')
name = tk.Entry(root, width='14')  # Поле ввода для имени
name.grid(column=0, row=1, padx=64, pady=1, sticky='nw')
name.focus_set()  # Устанавливаем фокус на поле ввода

# Поле для месяца
mon_label = tk.Label(root, text="Month:")  # Метка для месяца
mon_label.grid(column=0, row=2, padx=12, pady=4, sticky='nw')
mon = tk.Entry(root, width='14')  # Поле ввода для месяца
mon.grid(column=0, row=2, padx=64, pady=(1,18), sticky='nw')

# Метка для раздела "Chores / Duties"
chore_lbl = tk.Label(root, text="Chores / Duties:", fg='#1A1A1A', font=('Arial 10 bold'))
chore_lbl.grid(column=0, row=3, padx=12, pady=4, sticky='w')

# Метки для ежедневных, еженедельных и ежемесячных задач
daily = tk.Label(root, text="Daily:")
daily.grid(column=0, row=4, padx=16, pady=2, sticky='w')

week = tk.Label(root, text="Weekly:")
week.grid(column=0, row=4, padx=187, pady=2, sticky='w')

month = tk.Label(root, text="Monthly:")
month.grid(column=0, row=4, padx=357, pady=2, sticky='w')

# Создание фрейма для хранения полей ввода задач
midframe = tk.Frame(relief='flat')
midframe.grid(column=0, row=5, padx=0, pady=(0, 20), sticky='nw')

# Циклы для создания сетки полей ввода задач
for y in range(3):  # 3 столбца
    for x in range(9):  # 9 строк
        my_entry = tk.Entry(midframe, bd=1, width='16')  # Создаем поле ввода
        my_entry.grid(column=y, row=x, padx=18, pady=2, sticky='w')  # Размещаем на сетке
        my_entries.append(my_entry)  # Добавляем поле в список

# Поле для дополнительного текста
addi = tk.Label(text="Additional:")  # Метка для дополнительного текста
addi.grid(column=0, row=6, padx=18, pady=0, sticky='w')
tex = tk.Text(bd=1, width=58, height='12')  # Текстовое поле
tex.grid(column=0, row=7, padx=18, pady=(2,20), sticky='w')
tex.config(wrap="word")  # Установка обтекания текста по словам
tex.insert('1.0', "No allowance until chores are completed. :)")  # Вставка текста по умолчанию

# Функция очистки полей
def clear_fields(event=None):
    name.delete('0', 'end')
    mon.delete('0', 'end')
    for entry in my_entries:
        entry.delete('0', 'end')
    tex.delete('1.0', 'end')
    name.focus_set()

# Функция сохранения данных в текстовый файл
def save_com(event=None):
    file = tkFileDialog.asksaveasfile(mode='w', defaultextension='.txt',
                                      filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file:
        file.write("\n")
        file.write("Monthly Chores / Duties\n\n\n")
        file.write("Name:    " + (name.get()) + "\n\n")
        file.write("Month:   " + (mon.get()) + "\n\n\n")

        file.write("Daily: ".ljust(28) + "Weekly: ".ljust(28) + "Monthly: ".ljust(28) + "\n\n")

        for i in range(9):
            file.write(my_entries[i].get().ljust(28) + my_entries[i+9].get().ljust(28) + my_entries[i+18].get().ljust(28) + "\n")

        file.write("\n\n")
        file.write("Additional: " + "\n\n")
        data = tex.get('1.0', 'end-1c')
        file.write(data)
        file.close()

# Функция выхода из программы
def exit_com(event=None):
    win = tk.Toplevel()  # Создание нового окна
    win.title("Exit")
    xit = tk.Label(win, text="\n\nAre you sure you want to exit?\n")
    xit.pack()
    ex = tk.Button(win, text="Exit", width=4, command=root.destroy)
    ex.pack(side='left', padx=28, pady=4)
    ex.focus_set()
    ex.bind("<Return>", (lambda event: root.destroy()))
    can = tk.Button(win, text="Cancel", width=4, command=win.destroy)
    can.pack(side='right', padx=28, pady=4)
    win.transient(root)
    win.geometry('240x120')
    win.wait_window()

# Функция отображения информации о программе
def about_com(event=None):
    win = tk.Toplevel()  # Создание нового окна
    win.title("About")
    bout = tk.Label(win, text="""\n\nMonthly Planner\n
Monthly Chores For You and Yours\n
Fail to Plan, Plan to Fail\n\n
Made in Python""")
    bout.pack()
    clo = tk.Button(win, text="Close", width=4, command=win.destroy)
    clo.pack(padx=8, pady=16)
    win.transient(root)
    win.geometry('300x220+638+298')
    win.wait_window()

# Функция для раздела "Troubleshooting"
def trouble_com(event=None):
    win = tk.Toplevel()  # Создание нового окна
    win.title("Troubleshooting")
    trouble = tk.Label(win, justify='left', text="""\n\n
One problem that may occur is the use of
long words/phrases typed in entry fields.
This may force the text in the next column
over, and out of alignment within the columns.\n
Note: This is noticeable only in the saved
text file, not the program itself.\n
To avoid this, use short words in entry fields.\n
The saved text file is formatted in a way
that this shouldn't happen often.

\n\n""")
    trouble.pack()
    cls = tk.Button(win, text="Close", command=win.destroy)
    cls.pack()
    win.transient(root)
    win.geometry('354x360+612+230')
    win.wait_window()

# Создание меню
menu = tk.Menu(root, bd=1, relief='flat')
root.config(menu=menu, bd=2)

# Файл-меню
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File ", menu=filemenu)
filemenu.add_command(label="Clear Fields", command=clear_fields, accelerator="Ctrl+C ".rjust(8))
filemenu.add_command(label="Save As", command=save_com, accelerator="Ctrl+S ".rjust(8))
filemenu.add_command(label="Exit", command=exit_com, underline=1, accelerator="Ctrl+Q ".rjust(8))

# Меню помощи
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help ", menu=helpmenu)
helpmenu.add_command(label="About", command=about_com)
helpmenu.add_command(label="Troubleshooting", command=trouble_com)

# Привязка горячих клавиш
root.bind_all('<Control-c>', clear_fields)
root.bind_all('<Control-s>', save_com)
root.bind_all('<Control-q>', exit_com)

root.protocol("WM_DELETE_WINDOW")  # Обработка закрытия окна
root.mainloop()  # Запуск основного цикла обработки событий

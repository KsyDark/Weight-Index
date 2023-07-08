import tkinter as tk
from tkinter import messagebox

#Главное окно программы
root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry('250x260')
root.title('Индекс веса 1.1')

try:
    root.iconbitmap(r'ves.ico')
except:
    pass

#Виртуальаня картинка для задания размера в пикселях
#pixelVirtual = tk.PhotoImage(width=1, height=1)

#Заголовок программы
lable=tk.Label(root, text='Расчёт коэффициента веса', fg="red", bg="black", font="Atial 14")
lable.pack()

#Ввод данных
lable1=tk.Label(root, text='Ваш рост (м)', fg="black", font="Atial 14")
lable1.pack()

EntryA = tk.Entry(root, width=10, font='Arial 16')
EntryA.pack()

lable2=tk.Label(root, text='Ваш вес (кг)', fg="black",font="Atial 14")
lable2.pack()

EntryB = tk.Entry(root, width=10, font='Arial 16')
EntryB.pack()

lable3=tk.Label(root, text='Результат', fg="black", font="Atial 14")
lable3.pack()

#Вывод результата
EntryC = tk.Entry(root, width=20, font='Arial 16')
EntryC.pack()

def koef(event):
    a = EntryA.get() # берем текст из первого поля
    a = float(a) # преобразуем в число целого типа

    b = EntryB.get() 
    b = int(b)

    result = str(b/(a*a)) # результат переведем в строку для дальнейшего вывода
    EntryC.delete(0, tk.END) # очищаем текстовое поле полностью
    EntryC.insert(0, result) # вставляем результат в начало 

button=tk.Button(root, text='Рассчитать коэффициент веса', fg="black", font="Atial 10")
button.pack()
button.bind("<Button>", koef)
button.place(relx=0.12, rely=0.88)

#Запуск окна справки через Button
def reference():
    messagebox.showinfo("Справка", "Индекс веса 1.1. \n\nВ соответствии с рекомендациями ВОЗ разработана следующая интерпретация показателей:\n\nМенее 15,99 - Выраженный дефицит массы тела\n\n16,00 — 18,49 - Недостаточная (дефицит) масса тела\n\n18,50 — 24,99 - Норма\n\n25,00 — 29,99 - Избыточная масса тела (предожирение)\n\n30,00 — 34,99 - Ожирение первой степени\n\n35,00 — 39,99 - Ожирение второй степени\n\nБолее 40,00 - Ожирение третьей степени (морбидное)")
#Запуск окна справки через F1
def reference1(event):
    messagebox.showinfo("Справка", "Индекс веса 1.1. \n\nВ соответствии с рекомендациями ВОЗ разработана следующая интерпретация показателей:\n\nМенее 15,99 - Выраженный дефицит массы тела\n\n16,00 — 18,49 - Недостаточная (дефицит) масса тела\n\n18,50 — 24,99 - Норма\n\n25,00 — 29,99 - Избыточная масса тела (предожирение)\n\n30,00 — 34,99 - Ожирение первой степени\n\n35,00 — 39,99 - Ожирение второй степени\n\nБолее 40,00 - Ожирение третьей степени (морбидное)")

#Справка
button2=tk.Button(root, text='Справка', fg="black", font="Atial 10", command = reference)
button2.pack()
button2.place(relx=0.36, rely=0.765)

def clear(event):
    EntryA.delete(0, tk.END) # очищаем текстовое поле полностью
    EntryB.delete(0, tk.END) # очищаем текстовое поле полностью
    EntryC.delete(0, tk.END) # очищаем текстовое поле полностью

def exit_root(event):
    root.quit()

#Привязываем кнопку Enter, чтобу запускать Расчёт.
root.bind('<Return>', koef)
#Привязываем кнопку Delete чтобы очищать все строки
root.bind('<Delete>', clear)
#Привязываем кнопку ESC чтобы закрыть окно
root.bind('<Escape>', exit_root)
#Вызов окна справки
root.bind('<F1>', reference1)

root.mainloop()
import time
import asyncio
from tkinter import *

def toggle():
    if toggle_btn.config('relief')[-1] == 'sunken':
        toggle_btn.config(relief="raised")
        toggle_btn.config(background='red')
        toggle_btn.config(text='OFF')
        print('off')    # выключение
    else:
        toggle_btn.config(relief="sunken")
        toggle_btn.config(background='green')
        toggle_btn.config(text='ON')
        print('on')    # включение



def reset():
    print('off')
    for t in range(5, 0, -1):
        root.after(1000, toggle_btn.config(text='OFF {}'.format(t)))
        root.update()
    toggle_btn.config(background='sky blue')
    toggle_btn.config(text='Выключатель')


root = Tk()
root.title("Моя первая графическая программа на Python")
root.geometry("400x250")
root.resizable(width=False, height=False)

label = Label(text="Привет Codeby!", font="12", pady="10")
label.pack()
toggle_btn = Button(text="Выключатель", width=12, relief="raised",background="sky blue", command=toggle)
toggle_btn.pack(pady=5)
btn1 = Button(text="Reset", background="#000000", foreground="#fff", padx="15", pady="2", font="12",command=reset)
btn1.pack()



# asyncio.run(reset())
root.mainloop()
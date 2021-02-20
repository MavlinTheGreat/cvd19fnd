from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import FileDialog, askdirectory
from tkinter.filedialog import askopenfile
from neurpred import neural_pred
from PIL import Image, ImageTk

root = Tk()

root.geometry("1284x724")
root.resizable(False, False)

# Add image file
bg = PhotoImage(file="covid.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

# Create Frame
frame1 = Frame(root)
frame1.pack()


def printt(path):
    c = Canvas(root, width=550, height=300, bg="green")
    c.place(x=85, y=260)
    img = PhotoImage(file=path)
    c.create_image(image=img)


def print_res(res):
    print("changes...", res)
    if res == 1:
        reslabel.config(text="Обнаружен Covid-19")
    if res == 0:
        reslabel.config(text="Программа не обнаружила коронавирусную инфекцию.")

# Кнопка обзора
def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    k = str(filename)
    k = neural_pred(k)
    print_res(k)
    


browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.place(x=619, y=625)

pathlabel = Label(root, height=1, text="File directory")
pathlabel.pack(side=BOTTOM, pady=50)

reslabel = Label(root, height=2, text="")
reslabel.pack(side=RIGHT, padx=250)

root.mainloop()

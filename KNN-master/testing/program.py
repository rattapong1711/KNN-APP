from tkinter import *
from PIL import Image, ImageTk
import KNN

root = Tk()
root.title('KNN Nattaphon & Apiwich & Atid')
root.resizable(width=False, height=False)
frame = Frame(root)
frame.pack()

canvas = Canvas(frame, 
                bg="white", 
                width=960, 
                height=540)
canvas.pack()

# set text
header = Label(canvas, text="KNN APP", bg="white" ,fg="black", font="Inter 36 bold").place(x=25, y=21)

# set form box
body = PhotoImage(file="assets/pic/form.png")
canvas.create_image(800, 280, image=body)
form_header = canvas.create_text(875, 55, text="INPUT", font="Inter 30 bold", fill="white")
K = canvas.create_text(700, 130, text="K", font="Inter 30 bold", fill="white")
SEX = canvas.create_text(705, 190, text="AGE", font="Inter 30 bold", fill="white")
WEIGHT = canvas.create_text(730, 260, text="WEIGHT", font="Inter 30 bold", fill="white")
HEIGHT = canvas.create_text(730, 320, text="HEIGHT", font="Inter 30 bold", fill="white")
# table
table = PhotoImage(file="assets/pic/table.png")
canvas.create_image(300,235, image=table)
# Input state
Input_image_box = PhotoImage(file="assets/pic/input.png")
k = IntVar()
canvas.create_image(895, 120, image=Input_image_box)
input_k = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=k).place(x=845, y=100)

sex = IntVar()
canvas.create_image(895, 190, image=Input_image_box)
input_sex = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=sex).place(x=845, y=170)

weight = IntVar()
canvas.create_image(895, 260, image=Input_image_box)
input_weight = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=weight).place(x=845, y=240)

height = IntVar()
canvas.create_image(895, 330, image=Input_image_box)
input_height = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=height).place(x=845, y=310)

# set result box
# mother
under = PhotoImage(file="assets/pic/mother_result.png")
canvas.create_image(485,450, image=under)
result = PhotoImage(file="assets/pic/under_result.png")
canvas.create_image(485,500, image=result)

output = PhotoImage(file="assets/pic/result.png")
canvas.create_image(650, 495, image=output)
txt = StringVar()
out_put = Label(canvas, width=7, font="Inter 24 bold", background="#ECF4E8", border=0, textvariable=txt).place(x=655, y=470)

def calling_KNN():
    K = k.get()
    SEX = sex.get()
    WEIGHT = weight.get()
    HEIGHT = height.get()
    
    result = KNN.knn(K,SEX, WEIGHT, HEIGHT)
    txt.set(result)
    return result

# result state
button_image = PhotoImage(file="assets/pic/button.png")
click_label = Label(canvas,image=button_image)
button = Button(canvas, image= button_image, command=calling_KNN, border=0, background="white", cursor="hand2")
button.place(x=250, y=460)


root.mainloop()
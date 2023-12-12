import csv
from tkinter import *
import tkinter
import KNN
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title('No.1 APP')
root.resizable(width=False, height=False)
frame = Frame(root)
frame.pack()

canvas = Canvas(frame, 
                bg="white", 
                width=960, 
                height=560)
canvas.pack()

# set text
header = Label(canvas, text="ตารางเปรียบเทียบ สัดส่วนของร่างกาย", bg="white" ,fg="black", font="Inter 20 bold").place(x=450, y=20)

# set form box
body = PhotoImage(file="assets/pic/form.png")
canvas.create_image(200, 260, image=body)
form_header = canvas.create_text(200, 55, text="ใส่ข้อมูล", font="Inter 30 bold", fill="black")
K = canvas.create_text(130, 115, text="เพศ", font="Inter 30 bold", fill="black")
SEX = canvas.create_text(130, 185, text="อายุ", font="Inter 30 bold", fill="black")
WEIGHT = canvas.create_text(105, 255, text="น้ำหนัก", font="Inter 30 bold", fill="black")
HEIGHT = canvas.create_text(105, 325, text="ส่วนสูง", font="Inter 30 bold", fill="black")
# table
table = PhotoImage(file="assets/pic/table.png")
canvas.create_image(665,235, image=table)
# Input state
Input_image_box = PhotoImage(file="assets/pic/input.png")
k = StringVar()
canvas.create_image(290, 120, image=Input_image_box)
input_k = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=k).place(x=220, y=100)

sex = IntVar()
canvas.create_image(290, 190, image=Input_image_box)
input_sex = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=sex).place(x=220, y=170)

weight = IntVar()
canvas.create_image(290, 260, image=Input_image_box)
input_weight = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=weight).place(x=220, y=240)

height = IntVar()
canvas.create_image(290, 330, image=Input_image_box)
input_height = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=height).place(x=220, y=310)

# set result box
# mother
under = PhotoImage(file="assets/pic/mother_result.png")
canvas.create_image(485,470, image=under)
result = PhotoImage(file="assets/pic/under_result.png")
canvas.create_image(485,500, image=result)

output = PhotoImage(file="assets/pic/result.png")
canvas.create_image(650, 495, image=output)
txt = StringVar()
out_put = Label(canvas, width=7, font="Inter 24 bold", background="#ffffff", border=0, textvariable=txt).place(x=655, y=470)
#รับข้อมูลที่ใส่เข้ามา
def calling_KNN():
    K = k.get()
    if (K == "male" or "Male"):
        K = 1
    elif (K == "female" or "Female"):
        K = 0
    SEX = sex.get()
    WEIGHT = weight.get()
    HEIGHT = height.get()
    
    result = KNN.knn([K, SEX, WEIGHT, HEIGHT])
    txt.set(result)
    return result

def open_image():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("all files", "*.*")))

    
    if file_path:
        # Open the image using Pillow (PIL)
        image = Image.open(file_path)
        # Resize the image as needed
        image = image.resize((300, 300))
        # Convert the image to PhotoImage for Tkinter
        tk_image = ImageTk.PhotoImage(image)

        # Create a new window to display the image
        image_window = tkinter.Toplevel(root)
        image_window.title("รูปภาพ")

        # Create a label to display the image in the new window
        image_label = tkinter.Label(image_window, image=tk_image)
        image_label.image = tk_image
        image_label.pack()


# result state
button_image = PhotoImage(file="assets/pic/button.png")
click_label = Label(canvas,image=button_image)
button = Button(canvas, image= button_image, command=calling_KNN, border=0, background="white", cursor="hand2")
button.place(x=250, y=460)

# set button insert image
ImageButton = Button(canvas, text="เปิดรูป", command=open_image, border=1, background="white", cursor="hand2")
ImageButton.place(x=890, y=50)

root.mainloop()
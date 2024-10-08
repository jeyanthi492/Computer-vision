from tkinter import *
from tkinter.ttk import Combobox
from lists import *
from PIL import Image, ImageTk
import random
from avatar_create import avatar_create
from meet_start import meet

flag = 1
def next_window(win2,*ten):
    global flag
    flag = 0
    meet(win2, *ten)

def female_window(win1,cap):
    cap.release()
    def go_to_meet():

         avatar_create(combo_box1.get(), combo_box2.get(), "BLACK", combo_box4.get(), combo_box5.get(),combo_box6.get(), combo_box7.get(), combo_box8.get(), "DEFAULT","BLACK")

         img1 = Image.open("AVATAR_2.png")
         img1 = img1.resize((500, 500))
         tk_img = ImageTk.PhotoImage(img1)
         label.image=tk_img
         label.configure(image=tk_img)
         if flag==1:
          label.after(2,go_to_meet)

    win2 = Toplevel(win1)
    win2.geometry("1400x1000")
    win2.title("FEMALE")

    label = Label(win2)
    label.place(x=50, y=80)

    num1 = StringVar()
    combo_box1 = Combobox(win2, values=list_skin_color, textvariable=num1, width=70)
    combo_box1.place(x=730, y=150)
    num1.set(list_skin_color[random.randrange(0, len(list_skin_color)-3)])

    num2 = StringVar()
    combo_box2 = Combobox(win2, values=list_top_type_girls, textvariable=num2, width=70)
    combo_box2.place(x=730, y=200)
    num2.set(list_top_type_girls[random.randrange(0, len(list_top_type_girls)-6)])

    num4 = StringVar()
    combo_box4 = Combobox(win2, values=list_hair_color, textvariable=num4, width=70)
    combo_box4.place(x=730, y=250)
    num4.set(list_hair_color[random.randrange(0, len(list_hair_color)-5)])

    num5 = StringVar()
    combo_box5 = Combobox(win2, values=list_accessories_type, textvariable=num5, width=70)
    combo_box5.place(x=730, y=300)
    num5.set(list_accessories_type[random.randrange(0, len(list_accessories_type))])

    num6 = StringVar()
    combo_box6 = Combobox(win2, values=list_clothe_type, textvariable=num6, width=70)
    combo_box6.place(x=730, y=350)
    num6.set(list_clothe_type[random.randrange(0, len(list_clothe_type))])

    num7 = StringVar()
    combo_box7 = Combobox(win2, values=list_clothe_graphic_type, textvariable=num7, width=70)
    combo_box7.place(x=730, y=400)
    num7.set(list_clothe_graphic_type[random.randrange(0, len(list_clothe_graphic_type))])

    num8 = StringVar()
    combo_box8 = Combobox(win2, values=list_clothe_color, textvariable=num8, width=70)
    combo_box8.place(x=730, y=450)
    num8.set(list_clothe_color[random.randrange(0, len(list_clothe_color))])



    label1 = Label(win2, text="Skin Color")
    label1.place(x=600, y=150)

    label2 = Label(win2, text="Top type")
    label2.place(x=600, y=200)


    label4 = Label(win2, text="Hair Color")
    label4.place(x=600, y=250)

    label5 = Label(win2, text="Accessories type")
    label5.place(x=600, y=300)

    label6 = Label(win2, text="Cloth type")
    label6.place(x=600, y=350)

    label7 = Label(win2, text="Cloth Graphic Type")
    label7.place(x=600, y=400)

    label8 = Label(win2, text="Cloth Color")
    label8.place(x=600, y=450)




    button1 = Button(win2, text="NEXT", background="red", command=lambda:next_window(win2,combo_box1.get(),combo_box2.get(), "BLACK", combo_box4.get(), combo_box5.get(),combo_box6.get(), combo_box7.get(), combo_box8.get(), "DEFAULT","BLACK"), width=30, height=4)
    button1.place(x=850, y=570)
    go_to_meet()
    win2.mainloop()

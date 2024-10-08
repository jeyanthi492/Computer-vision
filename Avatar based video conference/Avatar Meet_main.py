from tkinter import*
import cv2
from PIL import Image, ImageTk
from male_window import male_window
from female_window import female_window
print("hello1")
cap = cv2.VideoCapture(0)
print("hello2")
def show_frames():
    ret, img = cap.read()
    if ret:
     print("hello3")
     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
     img1 = Image.fromarray(img)
     img1 = img1.resize((500, 500))
     tk_img = ImageTk.PhotoImage(img1)
     label.image = tk_img
     label.configure(image=tk_img)
     label.after(2, show_frames)
    else:
        label.destroy()



win1 = Tk()
win1.geometry("1500x1500")
win1.title("MEET")
label=Label(win1)
label.place(x=100, y=80)
show_frames()


button1=Button(win1, text="MALE", fg="black", bg="red", width=50, height=10, command=lambda: male_window(win1, cap))
button1.place(x=850, y=100)

button2=Button(win1, text="FEMALE", fg="black", bg="red", width=50, height=10, command=lambda: female_window(win1, cap))
button2.place(x=850, y=380)

win1.mainloop()


from tkinter import *
from avatar_create import avatar_create
import cv2
from PIL import Image, ImageTk


cap=cv2.VideoCapture(0)

def meet(win,*ten):
    global ten1,label
    ten1 = ten
    window = Toplevel(win)
    window.title("MEET START")
    window.geometry("1500x1500")
    label = Label(window)
    label.pack()
    img1 = Image.open("AVATAR_2.png")
    img1 = img1.resize((500, 500))
    tk_img = ImageTk.PhotoImage(img1)
    label.image = tk_img
    label.configure(image=tk_img)
    button = Button(window,text="click",command=show,width=20,height=4,background="red")
    button.place(x=600,y=550)
    window.mainloop()




def show():
    def find():
      try:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        mouth=[]
        eyes=[]
        if len(faces)!=0:
         for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            roi_gray_eye = gray[y:int((y + (y + h)) / 2), x:x + w]
            roi_color_eye = img[y:int((y + (y + h)) / 2), x:x + w]

            roi_gray_mouth = gray[int((y + (y + h)) / 2):y + h, x:x + w]
            roi_color_mouth = img[int((y + (y + h)) / 2):y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray_eye)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color_eye, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            mouth = mouth_cascade.detectMultiScale(roi_gray_mouth)
            for (mx, my, mw, mh) in mouth:
                cv2.rectangle(roi_color_mouth, (mx, my), (mx + mw, my + mh), (0, 255, 0), 2)


         if len(mouth) != 0:
             option_mouth_type = "DEFAULT"
         else:
             option_mouth_type = "TWINKLE"
         if len(eyes) != 0:
             option_eyes_type = "SQUINT"
         else:
             option_eyes_type = "CLOSE"
         avatar_create(ten1[0], ten1[1], ten1[2], ten1[3], ten1[4], ten1[5], ten1[6], ten1[7], ten1[8],
                       ten1[9], option_mouth_type, option_eyes_type)
         img1 = Image.open("AVATAR_2.png")
         img1 = img1.resize((500, 500))
         tk_img = ImageTk.PhotoImage(img1)
         label.image = tk_img
         crop = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)

         label.configure(image=tk_img)
         cv2.imshow("crop", crop)
         cv2.waitKey(1)
         if cv2.waitKey(1) & 0xFF == ord("q"):
             cap.release()

         label.after(2, find)


        else:
            find()
      except:
          pass
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    find()




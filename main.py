
from tkinter import * 
from tkinter import ttk, filedialog
from facedetect import detImgFace, detVidFace , detCamFace, cv


def close_win():
    win.destroy()
    
def open_img():
    file = filedialog.askopenfilename()
    detImgFace(file)
    cv.destroyAllWindows()

def open_vid():
    file = filedialog.askopenfilename()
    detVidFace(file)
    
def open_cam():
    detCamFace()
    
    
win = Tk()
win.title("Face Detection")
win.geometry("605x250")
    
label = ttk.Label(win, text="Choose Image or Video or Camera",font=('Poppins bold', 28))
label.place(x=15, y=20)

s = ttk.Style()
s.configure('my.TButton', font=(any, 23))
B1 = ttk.Button(win, text= "Image", command=open_img, style='my.TButton')
B1.place(x=80, y=90)
B2 = ttk.Button(win, text= "Video",command=open_vid, style='my.TButton')
B2.place(x=320, y=90)
B3 = ttk.Button(win, text= "Camera",command=open_cam, style='my.TButton')
B3.place(x=80, y=160)
B4 = ttk.Button(win, text= "Close",command=close_win, style='my.TButton')
B4.place(x=320, y=160)

win.mainloop()


    

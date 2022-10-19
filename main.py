from tkinter import * 
from tkinter import ttk, filedialog
from data.src.infowin import info_win
from data.src.buttons import open_cam, open_img, open_vid
    

win = Tk()
win.title("Face Detection")
win.geometry("645x250+200+200")
win_icon = PhotoImage(file= "data/Img/icon.png")
win.iconphoto(False, win_icon)
win['bg'] = '#798086'

label = ttk.Label(win, text= "Choose Image or Video or Camera", font=('Poppins bold', 28, 'underline', 'bold'))
label.config(background= "#798086")
label.place(x= 15, y= 20)

s = ttk.Style()
s.configure('my.TButton', font= (any, 25))
s.map("my.TButton",
            foreground= [('!active', 'black'), ('pressed', 'red'), ('active', 'black')],
            background= [ ('!active','grey75'), ('pressed', 'aqua'), ('active', 'black')]
    )

B1 = ttk.Button(win, text= "Image", command= open_img, style= 'my.TButton')
B1.place(x= 90, y= 90)

B2 = ttk.Button(win, text= "Video", command= open_vid, style= 'my.TButton')
B2.place(x= 340, y= 90)

B3 = ttk.Button(win, text= "Camera", command= open_cam, style= 'my.TButton')
B3.place(x= 90, y= 160)

B4 = ttk.Button(win, text= "Close", command= win.destroy, style= 'my.TButton')
B4.place(x= 340, y= 160)

info_logo = PhotoImage(file= 'data/Img/info.png')
info = Button(win, image= info_logo, command=lambda: info_win(win), borderwidth= 0, highlightthickness= 0, activebackground= "#798086")
info.place(x= 615 ,y= 220)
win.mainloop()

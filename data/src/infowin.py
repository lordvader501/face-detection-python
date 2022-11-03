from tkinter import * 
from tkinter import ttk
from idlelib.tooltip import Hovertip
import webbrowser

def callback(url):
   webbrowser.open_new_tab(url)

def info_win(win):
    new_win = Toplevel(win)
    new_win.title("About")
    new_win.geometry("445x350")
    new_win.resizable(False, False)
    newwin_icon = PhotoImage(file= "data/Img/about.png")
    new_win.iconphoto(False, newwin_icon)
    new_win['bg'] = '#798086'
    
    
    label = ttk.Label(new_win, text= "FACE DETECTION", font= ('Poppins bold', 20, 'underline', 'bold'))
    label.config(background= "#798086")
    label.place(x= 15, y= 20)
    
    version = ttk.Label(new_win, text= "Version : 1.0",font= ('Poppins bold', 12,'italic','bold'))
    version.config(background= "#798086")
    version.place(x= 35, y= 65)

    frame = Frame(new_win, width= 144, height= 144)
    frame.config(bg= 'blue')
    frame.place(x= 290, y= 10)
    
    img_label = PhotoImage(file= "data/Img/icon.png")
    label_img = Label(frame, image = img_label, cursor= "hand2")
    label_img.bind("<Button-1>", lambda e: callback("http://github.com/lordvader501/face-detection-python"))
    label_img.place(x= 3, y= 3)
    Hovertip(label_img, 'Click here to visit this project repository.')
    
    canvas = Canvas(new_win, width= 445, height= 55, highlightthickness= 0)
    canvas.config(bg= '#798086')
    canvas.place(x= 0, y= 290)
    canvas.create_line(10, 10, 435, 10, fill= "black", width= 1.5)
    canvas.create_line(10, 50, 435, 50, fill= "black", width= 1.5)
    canvas.create_text(75,30,text= 'FOLLOW ME : ',font= ('Poppins bold', 12, 'italic', 'bold'))
    
    github_img = PhotoImage(file= 'data/Img/github.png')
    github = Button(canvas, image= github_img, 
                    command=lambda: callback("http://github.com/lordvader501"), 
                    borderwidth= 0, highlightthickness= 0, cursor= 'hand2',
                    activebackground="#798086"
            )
    github.place(x=140 ,y=15)
    Hovertip(github, 'Github')
    
    linkedin_img = PhotoImage(file= 'data/Img/linkedin.png')
    linkedin = Button(canvas, image= linkedin_img, 
                      command=lambda: callback("https://in.linkedin.com/in/shauryamdubey"), 
                      borderwidth= 0, highlightthickness= 0, cursor= 'hand2',
                      activebackground="#798086"
            )
    linkedin.place(x= 180 ,y= 15)
    Hovertip(linkedin, 'LinkedIn')
    
    twitter_img = PhotoImage(file= 'data/Img/twitter.png')
    twitter = Button(canvas, image= twitter_img, 
                      command=lambda: callback("https://twitter.com/ShauryamDubey"), 
                      borderwidth= 0, highlightthickness= 0, cursor= 'hand2',
                      activebackground="#798086"
            )
    twitter.place(x= 220 ,y= 15)
    Hovertip(twitter, 'Twitter')
    
    new_win.mainloop()
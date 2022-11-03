from tkinter import filedialog
from .camdetect import detCamFace, cvCam
from .imgdetect import detImgFace, cvImg
from .videodetect import detVidFace, cvVideo
import threading as th

def open_img():
    file = filedialog.askopenfilename(title= 'Open Image', filetypes= [("JPEG", '*.jpeg'), ('JPEG', '*.jpg'), ('PNG', '*.png'), ('WebP', '*.webp'), ('All Files', '*.*')])
    if file == '':
        pass
    else:
        try:
            th.Thread(target= detImgFace(file)).start()
        except cvImg.error:
            pass

def open_vid():
    file = filedialog.askopenfilename(title= 'Open Video', filetypes= [('MP4', '*.mp4'), ('AVI', '*.avi'), ('All Files', '*.*')])
    if file == '':
        pass
    else:
        try:
            th.Thread(target= detVidFace(file)).start()
        except cvVideo.error:
            pass
    
def open_cam():
    try:
        th.Thread(target= detCamFace()).start()
    except cvCam.error:
        pass
    
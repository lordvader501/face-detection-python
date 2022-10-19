from tkinter import filedialog
from .facedetect import detImgFace, detVidFace , detCamFace, cv

def open_img():
    file = filedialog.askopenfilename(filetypes= [("JPEG", '*.jpeg'), ('JPEG', '*.jpg'), ('PNG', '*.png'), ('WebP', '*.webp'), ('All Files', '*.*')])
    if file == '':
        pass
    else:
        try:
            detImgFace(file)
            cv.destroyAllWindows()
        except cv.error:
            pass

def open_vid():
    file = filedialog.askopenfilename(filetypes= [('MP4', '*.mp4'), ('AVI', '*.avi'), ('All Files', '*.*')])
    if file == '':
        pass
    else:
        try:
            detVidFace(file)
        except cv.error:
            pass
    
def open_cam():
    detCamFace()
    
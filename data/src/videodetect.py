import cv2 as cvVideo

frameWidth = 820
frameHeight = 200
color = 130, 170, 100
cascade = cvVideo.CascadeClassifier('data/cascade/face_cascade.xml')

def rescale(frame, scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = width, height
    return cvVideo.resize(frame, dim, interpolation= cvVideo.INTER_AREA)

def getBrightness(img, brightness):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255 + brightness
        al_pha = (max - shadow) / 255
        ga_mma = shadow
        cal = cvVideo.addWeighted(img, al_pha,img, 0, ga_mma)
    else:
        cal = img
 
    return cal
    
def empty(a):
    pass

def detVidFace(path):
    cvVideo.namedWindow("Video Settings")
    cvVideo.resizeWindow("Video Settings", frameWidth, frameHeight)
    cvVideo.createTrackbar("scale", "Video Settings", 201, 1000, empty)
    cvVideo.createTrackbar("Neig", "Video Settings", 5, 20, empty)   
    cvVideo.createTrackbar("Min area", "Video Settings", 0, 100000, empty)
    cvVideo.createTrackbar("Brightness", "Video Settings", 220, 325, empty)   
    vid = cvVideo.VideoCapture(path)
    while True:
        vidBrightness = cvVideo.getTrackbarPos("Brightness", "Video Settings")
        ret_vid, vid_cap = vid.read()
        if ret_vid == False:
            break
        vid_cap = rescale(vid_cap, 0.75)
        vid_cap = getBrightness(vid_cap, vidBrightness)
        gray_cap = cvVideo.cvtColor(vid_cap, cvVideo.COLOR_BGR2GRAY) 
        vidscaleVal = 1 + (cvVideo.getTrackbarPos("scale", "Video Settings") / 1000)
        vid_neig = cvVideo.getTrackbarPos("Neig", "Video Settings")
        vid_objects, vid_det = cascade.detectMultiScale2(gray_cap, vidscaleVal, vid_neig)
        for (x, y, w, h) in vid_objects:
            area = w * h
            vidminArea = cvVideo.getTrackbarPos("Min area", "Video Settings")
            if area > vidminArea:
                cvVideo.rectangle(vid_cap, (x, y), (x+w, y+h), color , 2)
        cvVideo.rectangle(vid_cap, (7, 2), (210, 25), (80, 80, 80), -1)
        cvVideo.putText(vid_cap, f'No of Faces : {len(vid_det)}', (10, 20), cvVideo.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 150, 255), 2)
        cvVideo.rectangle(vid_cap, (7, vid_cap.shape[0]-27), (255, vid_cap.shape[0]), (225, 225, 225), -1)
        cvVideo.putText(vid_cap, 'PRESS \'q\' to EXIT!!!', (10, vid_cap.shape[0]-7), cvVideo.FONT_HERSHEY_COMPLEX_SMALL, 1, (30, 30, 30), 1)
        cvVideo.imshow("Video Detection", vid_cap)
        if (cvVideo.waitKey(1) == ord('q') or (cvVideo.getWindowProperty('Video Detection', cvVideo.WND_PROP_VISIBLE) < 1) or (cvVideo.getWindowProperty('Video Settings', cvVideo.WND_PROP_VISIBLE) < 1)):
            if cvVideo.getWindowProperty('Video Detection', cvVideo.WND_PROP_VISIBLE) < 1:
                cvVideo.destroyWindow("Video Settings")
                cvVideo.destroyWindow('Video Detection')
            else:
                cvVideo.destroyWindow('Video Detection')
                cvVideo.destroyWindow("Video Settings")
            break
    vid.release()
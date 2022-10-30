import cv2 as cv
import os


frameWidth = 820
frameHeight = 200
color = 255, 20, 255
cascade = cv.CascadeClassifier('data/cascade/face_cascade.xml')

def rescale(frame, scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = width, height
    return cv.resize(frame, dim, interpolation= cv.INTER_AREA)

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
        cal = cv.addWeighted(img, al_pha,img, 0, ga_mma)
    else:
        cal = img
 
    return cal
    
def empty(a):
    pass

def detImgFace(path):
    cv.namedWindow("Image Settings")
    cv.resizeWindow("Image Settings", frameWidth, frameHeight)
    cv.createTrackbar("scale", "Image Settings", 201, 1000, empty)
    cv.createTrackbar("Neig", "Image Settings", 5, 20, empty)   
    cv.createTrackbar("Min area", "Image Settings", 0, 100000, empty)  
    cv.createTrackbar("Brightness", "Image Settings", 220, 325, empty)   
    while True:
        camBrightness = cv.getTrackbarPos("Brightness", "Image Settings")
        img = cv.imread(path)
        img = getBrightness(img, camBrightness)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
        scaleVal = 1 + (cv.getTrackbarPos("scale", "Image Settings") / 1000)
        neig = cv.getTrackbarPos("Neig", "Image Settings")
        objects, det = cascade.detectMultiScale2(gray, scaleVal, neig)
        for (x, y, w, h) in objects:
            area = w*  h
            minArea = cv.getTrackbarPos("Min area", "Image Settings")
            if area > minArea:
                cv.rectangle(img, (x, y), (x+w, y+h), color , 2)
        cv.rectangle(img, (7, 2), (210, 25), (80, 80, 80), -1)
        cv.putText(img, f'No of Faces : {len(det)}', (10, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        cv.rectangle(img, (7, img.shape[0]-27), (255, img.shape[0]), (225, 225, 225), -1)
        cv.putText(img, 'PRESS \'q\' to EXIT!!!', (10, img.shape[0]-7), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)        
        cv.imshow("Img Detection", img)
        if cv.waitKey(1) & 0xff == ord('q'):
            break



def detVidFace(path):
    cv.namedWindow("Video Settings")
    cv.resizeWindow("Video Settings", frameWidth, frameHeight)
    cv.createTrackbar("scale", "Video Settings", 201, 1000, empty)
    cv.createTrackbar("Neig", "Video Settings", 5, 20, empty)   
    cv.createTrackbar("Min area", "Video Settings", 0, 100000, empty)
    cv.createTrackbar("Brightness", "Video Settings", 220, 325, empty)   
    cap = cv.VideoCapture(path)
    while True:
        camBrightness = cv.getTrackbarPos("Brightness", "Video Settings")
        success, img = cap.read()
        if success == False:
            break
        img = rescale(img, 0.75)
        img = getBrightness(img, camBrightness)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
        scaleVal = 1 + (cv.getTrackbarPos("scale", "Video Settings") / 1000)
        neig = cv.getTrackbarPos("Neig", "Video Settings")
        objects, det = cascade.detectMultiScale2(gray, scaleVal, neig)
        for (x, y, w, h) in objects:
            area = w * h
            minArea = cv.getTrackbarPos("Min area", "Video Settings")
            if area > minArea:
                cv.rectangle(img, (x, y), (x+w, y+h), color , 2)
        cv.rectangle(img, (7, 2), (210, 25), (80, 80, 80), -1)
        cv.putText(img, f'No of Faces : {len(det)}', (10, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        cv.rectangle(img, (7, img.shape[0]-27), (255, img.shape[0]), (225, 225, 225), -1)
        cv.putText(img, 'PRESS \'q\' to EXIT!!!', (10, img.shape[0]-7), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)
        cv.imshow("Video Detection", img)
        if cv.waitKey(40) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
        

def detCamFace():
    cv.namedWindow("Camera Settings")
    cv.resizeWindow("Camera Settings", frameWidth, frameHeight)
    cv.createTrackbar("scale", "Camera Settings", 201, 1000, empty)
    cv.createTrackbar("Neig", "Camera Settings", 5, 20, empty)   
    cv.createTrackbar("Min area", "Camera Settings", 0, 100000, empty) 
    cv.createTrackbar("Brightness", "Camera Settings", 170, 325, empty)   
    cap = cv.VideoCapture(0,cv.CAP_DSHOW)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        camBrightness = cv.getTrackbarPos("Brightness", "Camera Settings")
        success, img = cap.read()
        if success == False:
            break
        cap.set(10, camBrightness)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
        scaleVal = 1 + (cv.getTrackbarPos("scale", "Camera Settings") / 1000)
        neig = cv.getTrackbarPos("Neig", "Camera Settings")
        objects, det = cascade.detectMultiScale2(gray, scaleVal, neig)
        for (x, y, w, h) in objects:
            area = w * h
            minArea = cv.getTrackbarPos("Min area", "Camera Settings")
            if area > minArea:
                cv.rectangle(img, (x, y), (x+w, y+h), color , 2)
        cv.rectangle(img, (7, 2), (210, 25), (80, 80, 80), -1)
        cv.putText(img, f'No of Faces : {len(det)}', (10,20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        cv.rectangle(img, (7, 453), (255, 480), (225, 225, 225), -1)
        cv.putText(img, 'PRESS \'q\' to EXIT!!!', (10, 472), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)
        cv.imshow("Camera Detection", img)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
        
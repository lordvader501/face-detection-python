import cv2 as cv
import os


frameWidth = 820
frameHeight = 200
color = 255, 0, 255
#cascade = cv.CascadeClassifier(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data","cascade","face_cascade.xml"))
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
    cv.namedWindow("Settings")
    cv.resizeWindow("Settings", frameWidth, frameHeight)
    cv.createTrackbar("scale", "Settings", 201, 1000, empty)
    cv.createTrackbar("Neig", "Settings", 5, 20, empty)   
    cv.createTrackbar("Min area", "Settings", 0, 100000, empty)  
    cv.createTrackbar("Brightness", "Settings", 220, 325, empty)   
    while True:
        camBrightness = cv.getTrackbarPos("Brightness", "Settings")
        img = cv.imread(path)
        img = getBrightness(img, camBrightness)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
        scaleVal = 1 + (cv.getTrackbarPos("scale", "Settings") / 1000)
        neig = cv.getTrackbarPos("Neig", "Settings")
        objects, det = cascade.detectMultiScale2(gray, scaleVal, neig)
        for (x, y, w, h) in objects:
            area = w*  h
            minArea = cv.getTrackbarPos("Min area", "Settings")
            if area > minArea:
                cv.rectangle(img, (x, y), (x+w, y+h), color , 2)
                cv.putText(img, f'no of faces : {len(det)}', (10, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)
                
        cv.imshow("Result", img)
        if cv.waitKey(1) & 0xff == ord('q'):
            break



def detVidFace(path):
    cv.namedWindow("Settings")
    cv.resizeWindow("Settings", frameWidth, frameHeight)
    cv.createTrackbar("scale", "Settings", 201, 1000, empty)
    cv.createTrackbar("Neig", "Settings", 5, 20, empty)   
    cv.createTrackbar("Min area", "Settings", 0, 100000, empty)
    cv.createTrackbar("Brightness", "Settings", 220, 325, empty)   
    cap = cv.VideoCapture(path)
    while True:
        camBrightness = cv.getTrackbarPos("Brightness", "Settings")
        success, img = cap.read()
        if success == False:
            break
        img = rescale(img, 0.75)
        img = getBrightness(img, camBrightness)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
        scaleVal = 1 + (cv.getTrackbarPos("scale", "Settings") / 1000)
        neig = cv.getTrackbarPos("Neig", "Settings")
        objects, det = cascade.detectMultiScale2(gray, scaleVal, neig)
        for (x, y, w, h) in objects:
            area = w * h
            minArea = cv.getTrackbarPos("Min area", "Settings")
            if area > minArea:
                cv.rectangle(img, (x, y), (x+w, y+h), color , 2)
                cv.putText(img, f'no of faces : {len(det)}', (10, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)
        cv.imshow("Result", img)
        if cv.waitKey(40) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
        

def detCamFace():
    cv.namedWindow("Settings")
    cv.resizeWindow("Settings", frameWidth, frameHeight)
    cv.createTrackbar("scale", "Settings", 201, 1000, empty)
    cv.createTrackbar("Neig", "Settings", 5, 20, empty)   
    cv.createTrackbar("Min area", "Settings", 0, 100000, empty) 
    cv.createTrackbar("Brightness", "Settings", 220, 325, empty)   
    cap = cv.VideoCapture(0)
    cap.set(4, frameWidth)
    cap.set(3, frameHeight)
    while True:
        camBrightness = cv.getTrackbarPos("Brightness", "Settings")
        success, img = cap.read()
        if success == False:
            break
        cap.set(10, camBrightness)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
        scaleVal = 1 + (cv.getTrackbarPos("scale", "Settings") / 1000)
        neig = cv.getTrackbarPos("Neig", "Settings")
        objects, det = cascade.detectMultiScale2(gray, scaleVal, neig)
        for (x, y, w, h) in objects:
            area = w * h
            minArea = cv.getTrackbarPos("Min area", "Settings")
            if area > minArea:
                cv.rectangle(img, (x, y), (x+w, y+h), color , 2)
                cv.putText(img, f'no of faces : {len(det)}', (10, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)
        cv.imshow("Result", img)
        if cv.waitKey(20) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
        
import cv2 as cv
import os


frameWidth = 640
frameHeight = 480
color = 255,0,255
cascade = cv.CascadeClassifier(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data","cascade","face_cascade.xml"))


def empty(a):
    pass

def detImgFace(path):
    cv.namedWindow("Result")
    cv.resizeWindow("Result", frameWidth, frameHeight)
    cv.createTrackbar("scale","Result",201,1000,empty)
    cv.createTrackbar("Min area", "Result", 0, 100000,empty)        
    while True:
        img = cv.imread(path)
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
        scaleVal = 1 + (cv.getTrackbarPos("scale", "Result") / 1000)
        objects, det = cascade.detectMultiScale2(gray, scaleVal, 6)
        for (x,y,w,h) in objects:
            area = w*h
            minArea = cv.getTrackbarPos("Min area", "Result")
            if area > minArea:
                cv.rectangle(img, (x,y), (x+w, y+h), color , 2)
                cv.putText(img,f'no of faces : {len(det)}',(10,20),cv.FONT_HERSHEY_COMPLEX_SMALL,1,color,1)
                
        cv.imshow("Result", img)
        if cv.waitKey(1) & 0xff == ord('q'):
            break



def detVidFace(path):
    cv.namedWindow("Result")
    cv.resizeWindow("Result", frameWidth, frameHeight)
    cv.createTrackbar("scale","Result",201,1000,empty)
    cv.createTrackbar("Min area", "Result", 0, 100000,empty) 
    cap = cv.VideoCapture(path)
    while True:
        success, img = cap.read()
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
        scaleVal = 1 + (cv.getTrackbarPos("scale", "Result") / 1000)
        objects, det = cascade.detectMultiScale2(gray, scaleVal, 6)
        for (x,y,w,h) in objects:
            area = w*h
            minArea = cv.getTrackbarPos("Min area", "Result")
            if area > minArea:
                cv.rectangle(img, (x,y), (x+w, y+h), color , 2)
                cv.putText(img,f'no of faces : {len(det)}',(10,20),cv.FONT_HERSHEY_COMPLEX_SMALL,1,color,1)
        cv.imshow("Result", img)
        cv.waitKey(20)
        if success == False or 0xff == ord('q'):
            break
        

def detCamFace():
    cv.namedWindow("Result")
    cv.resizeWindow("Result", frameWidth, frameHeight)
    cv.createTrackbar("scale","Result",201,1000,empty)
    cv.createTrackbar("Min area", "Result", 0, 100000,empty) 
    cap = cv.VideoCapture(0)
    cap.set(1,frameWidth)
    cap.set(2,frameHeight)
    while True:
        success, img = cap.read()
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
        scaleVal = 1 + (cv.getTrackbarPos("scale", "Result") / 1000)
        objects, det = cascade.detectMultiScale2(gray, scaleVal, 6)
        for (x,y,w,h) in objects:
            area = w*h
            minArea = cv.getTrackbarPos("Min area", "Result")
            if area > minArea:
                cv.rectangle(img, (x,y), (x+w, y+h), color , 2)
                cv.putText(img,f'no of faces : {len(det)}',(10,20),cv.FONT_HERSHEY_COMPLEX_SMALL,1,color,1)
        cv.imshow("Result", img)
        cv.waitKey(20)
        if success == False or 0xff == ord('q'):
            break
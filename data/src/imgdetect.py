import cv2 as cvImg


frameWidth = 820
frameHeight = 200
color = 130, 170, 100
cascade = cvImg.CascadeClassifier('data/cascade/face_cascade.xml')

def rescale(frame, scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = width, height
    return cvImg.resize(frame, dim, interpolation= cvImg.INTER_AREA)

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
        cal = cvImg.addWeighted(img, al_pha,img, 0, ga_mma)
    else:
        cal = img
 
    return cal
    
def empty(a):
    pass

def detImgFace(path):
    cvImg.namedWindow("Image Settings")
    cvImg.resizeWindow("Image Settings", frameWidth, frameHeight)
    cvImg.createTrackbar("scale", "Image Settings", 201, 1000, empty)
    cvImg.createTrackbar("Neig", "Image Settings", 5, 20, empty)   
    cvImg.createTrackbar("Min area", "Image Settings", 0, 100000, empty)  
    cvImg.createTrackbar("Brightness", "Image Settings", 220, 325, empty)   
    while True:
        imgBrightness = cvImg.getTrackbarPos("Brightness", "Image Settings")
        img = cvImg.imread(path)
        img = getBrightness(img, imgBrightness)
        gray_img = cvImg.cvtColor(img, cvImg.COLOR_BGR2GRAY) 
        imgscaleVal = 1 + (cvImg.getTrackbarPos("scale", "Image Settings") / 1000)
        img_neig = cvImg.getTrackbarPos("Neig", "Image Settings")
        img_objects, img_det = cascade.detectMultiScale2(gray_img, imgscaleVal, img_neig)
        for (x, y, w, h) in img_objects:
            area = w * h
            img_minArea = cvImg.getTrackbarPos("Min area", "Image Settings")
            if area > img_minArea:
                cvImg.rectangle(img, (x, y), (x+w, y+h), color , 2)
        cvImg.rectangle(img, (7, 2), (210, 25), (80, 80, 80), -1)
        cvImg.putText(img, f'No of Faces : {len(img_det)}', (10, 20), cvImg.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 150, 255), 2)
        cvImg.rectangle(img, (7, img.shape[0]-27), (255, img.shape[0]), (225, 225, 225), -1)
        cvImg.putText(img, 'PRESS \'q\' to EXIT!!!', (10, img.shape[0]-7), cvImg.FONT_HERSHEY_COMPLEX_SMALL, 1, (30, 30, 30), 1)        
        cvImg.imshow("Image Detection", img)
        if (cvImg.waitKey(1) == ord('q') or (cvImg.getWindowProperty('Image Detection', cvImg.WND_PROP_VISIBLE) < 1) or (cvImg.getWindowProperty('Image Settings', cvImg.WND_PROP_VISIBLE) < 1)):
            if cvImg.getWindowProperty('Image Detection', cvImg.WND_PROP_VISIBLE) < 1:
                cvImg.destroyWindow("Image Settings")
                cvImg.destroyWindow('Image Detection')
            else:
                cvImg.destroyWindow('Image Detection')
                cvImg.destroyWindow("Image Settings")
            break
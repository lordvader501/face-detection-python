import cv2 as cvCam

frameWidth = 820
frameHeight = 200
color = 130, 170, 100
cascade = cvCam.CascadeClassifier('data/cascade/face_cascade.xml')

def rescale(frame, scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = width, height
    return cvCam.resize(frame, dim, interpolation= cvCam.INTER_AREA)

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
        cal = cvCam.addWeighted(img, al_pha,img, 0, ga_mma)
    else:
        cal = img
 
    return cal
    
def empty(a):
    pass

def detCamFace():
    cvCam.namedWindow("Camera Settings")
    cvCam.resizeWindow("Camera Settings", frameWidth, frameHeight)
    cvCam.createTrackbar("scale", "Camera Settings", 201, 1000, empty)
    cvCam.createTrackbar("Neig", "Camera Settings", 5, 20, empty)   
    cvCam.createTrackbar("Min area", "Camera Settings", 0, 100000, empty) 
    cvCam.createTrackbar("Brightness", "Camera Settings", 170, 325, empty)   
    cap = cvCam.VideoCapture(0,cvCam.CAP_DSHOW)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        camBrightness = cvCam.getTrackbarPos("Brightness", "Camera Settings")
        ret_cam, cam = cap.read()
        if ret_cam == False:
            break
        cap.set(10, camBrightness)
        cam = cvCam.flip(cam, 1)
        gray_cam = cvCam.cvtColor(cam, cvCam.COLOR_BGR2GRAY) 
        camscaleVal = 1 + (cvCam.getTrackbarPos("scale", "Camera Settings") / 1000)
        cam_neig = cvCam.getTrackbarPos("Neig", "Camera Settings")
        cam_objects, cam_det = cascade.detectMultiScale2(gray_cam, camscaleVal, cam_neig)
        for (x, y, w, h) in cam_objects:
            area = w * h
            camminArea = cvCam.getTrackbarPos("Min area", "Camera Settings")
            if area > camminArea:
                cvCam.rectangle(cam, (x, y), (x+w, y+h), color , 2)
        cvCam.rectangle(cam, (7, 2), (210, 25), (80, 80, 80), -1)
        cvCam.putText(cam, f'No of Faces : {len(cam_det)}', (10,20), cvCam.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 150, 255), 2)
        cvCam.rectangle(cam, (7, 453), (255, 480), (225, 225, 225), -1)
        cvCam.putText(cam, 'PRESS \'q\' to EXIT!!!', (10, 472), cvCam.FONT_HERSHEY_COMPLEX_SMALL, 1, (30, 30, 30), 1)
        cvCam.imshow("Camera Detection", cam)
        if (cvCam.waitKey(1) == ord('q') or (cvCam.getWindowProperty('Camera Detection', cvCam.WND_PROP_VISIBLE) < 1) or (cvCam.getWindowProperty('Camera Settings', cvCam.WND_PROP_VISIBLE) < 1)):
            if cvCam.getWindowProperty('Camera Detection', cvCam.WND_PROP_VISIBLE) < 1:
                cvCam.destroyWindow("Camera Settings")
                cvCam.destroyWindow('Camera Detection')
            else:
                cvCam.destroyWindow('Camera Detection')
                cvCam.destroyWindow("Camera Settings")
            break
    cap.release()
    
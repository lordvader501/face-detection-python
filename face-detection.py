import cv2 as cv
import os

# Taking user input of path and checking that path exist or not.
while True:
    path = input("Input PATH >>> ")
    if path == "QUIT":
        break
    if os.path.exists(path):
        img = cv.imread(path)
        break
    else:
        print("File not found.")

cv.imshow('image',img)

cv.waitKey(0)
cv.destroyAllWindows()
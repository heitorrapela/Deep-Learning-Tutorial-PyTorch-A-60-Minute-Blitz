from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11,11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred,50,250)
cv2.imshow("Edges", edged)
cv2.waitKey(0)

(_,cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} contours in this image".format(len(cnts)))

cont = image.copy()
cv2.drawContours(cont, cnts, -1, (0,255,0), 2)
cv2.imshow("Cnt", cont)
cv2.waitKey(0)
import numpy as np
import cv2
from PIL import Image, ImageFilter

class PostProcessing:
   def __init__(self, img):
       self.img = img
       
   def opening(ob):
        #kernel = np.ones((25,25),np.uint8)
        kernel = np.ones((25,25),np.uint8)
        ope = cv2.morphologyEx(ob.img, cv2.MORPH_OPEN, kernel,iterations=1)
        return ope

   def fill_hole(ob):
     ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
     contours, hierarchy = cv2.findContours(ob, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     len_contour = len (contours)
     contour_list = []
     for i in range(len_contour):
        drawing = np.zeros_like(ob, np.uint8)  # create a black image
        img_contour = cv2.drawContours(drawing, contours, i, (255, 255, 255), -1)
        contour_list.append(img_contour)

        out = sum(contour_list)
     return out
   def closing(ob):
        kernel = np.ones((9,9),np.uint8)
        close= cv2.morphologyEx(ob, cv2.MORPH_CLOSE, kernel)
        return close



   def convexHull(ob):
       img = cv2.cvtColor(ob.img, cv2.COLOR_BGR2GRAY)
    # Threshold the image
       ret, thresh = cv2.threshold(img,50,255,0)
        # Find the contours
       contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

       for i in range(len(contours)):
        hull = cv2.convexHull(contours[i])
        cv2.drawContours(ob.img, [hull], -1, (255, 255,255), 2)
        #kernel = np.ones((18,18),np.uint8)
        kernel = np.ones((15,15),np.uint8)
        closing = cv2.morphologyEx(ob.img, cv2.MORPH_CLOSE, kernel)
        return closing


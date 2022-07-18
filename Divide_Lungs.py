import cv2
import numpy as np


        
def Divide_Lungs(img_name,msk_name):

    #n=img_name
    #m=msk_name
    #print(msk)
    #img = cv2.imread('D:/ricord_images_PoprawionyKontrast/'+img_name)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #mskgray = cv2.imread('D:/maski_Covid_ost/'+msk_name)
    #mskgray = cv2.cvtColor(mskgray, cv2.COLOR_BGR2GRAY)
  
    img =img_name
    mskgray= msk_name
    #mskgray = cv2.cvtColor(msk, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(mskgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    c1 = contours[0]
    c2 = contours[1]
    y_1=[]
    y_2=[]
    for i1,i2 in zip(c1,c2): 
        for j1,j2 in zip(i1,i2):
            y_1.append(j1[1])
            y_2.append(j2[1])

    maxxx = max(y_1)
    mini = min(y_1)
    maxxx2 = max(y_2)
    mini2 = min(y_2)

    maxiii=0
    miniii=0
    if (maxxx>=maxxx2):
        maxiii=maxxx
    else:
        maxiii=maxxx2

    if (mini>=mini2):
        miniii=mini2
    else:
        miniii=mini

    dl = maxiii - miniii
    kawal = round(dl/3)
    return [img[miniii:miniii+kawal,:],img[miniii+kawal:miniii+kawal+kawal,:],img[miniii+kawal+kawal:maxiii,:],mskgray[miniii:miniii+kawal,:],mskgray[miniii+kawal:miniii+kawal+kawal,:],mskgray[miniii+kawal+kawal:maxiii,:]]
    #return [mskgray[miniii:kawal,:],mskgray[kawal:kawal*2,:],mskgray[kawal*2:maxiii,:]]
    # cv2.imshow('Plat1',mskgray[miniii:kawal,:])
    # cv2.imshow('Plat2',mskgray[kawal:kawal*2,:])
    # cv2.imshow('Plat3',mskgray[kawal*2:maxiii,:])
    # cv2.waitKey(0)


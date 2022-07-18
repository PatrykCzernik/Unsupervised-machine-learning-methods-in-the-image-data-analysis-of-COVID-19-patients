# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:36:38 2020

@author: Patryk
"""
import png
import os
import pydicom
import numpy as np
from skimage.color import rgb2gray
from PIL import Image 
import SimpleITK as sitk
import cv2

wej = "C:/Users/Patryk/Desktop/pdf_Mag/kod/1/"
#wej="D:/dicom_covid/"
wyj = 'C:/Users/Patryk/Desktop/pdf_Mag/kod/1/'


 
folder = os.listdir(wej)
   
for plik in folder:
    a=plik.split(sep=".")
    #if a[1]=="dcm":
        
        
    #dicom = pydicom.dcmread(os.path.join(wej,plik))
    #ksztalt = dicom.pixel_array.shape
    Im = sitk.ReadImage('C:/Users/Patryk/Desktop/pdf_Mag/kod/1/'+plik)
    Im = sitk.GetArrayFromImage(Im)
            #Piksele = dicom.pixel_array.astype(np.uint8) # Tablica z pikselami
            #Piksele = dicom.pixel_array.astype(np.uint64)
    #Piksele = dicom.pixel_array
    

    Piksele = np.uint8(Im)
 
    Piksele = np.squeeze(Piksele)
    Piksele = cv2.resize(Piksele, (256,256), interpolation = cv2.INTER_AREA)

    #Piksele = Piksele[:,:,0]

            
            #Piksele = Piksele.astype(float)
            #Piksele = Piksele.astype(np.uint16)
    
    #szary = rgb2gray(Piksele)
            
    
                # Teraz konwertuje na typ uint8, czyli 8 odcieni szarosci
    #szary = np.uint8(Piksele)

    
    
                # I  na koncu zapisuje bez strat na jakosci w formacie png
    with open(os.path.join(wyj,plik)+'.png' , 'wb') as png_file:
        pnig = png.Writer(256, 256, greyscale=True)
        pnig.write(png_file, Piksele)
        



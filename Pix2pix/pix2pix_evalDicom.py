import os
import glob
import cv2
import numpy as np
from matplotlib import pyplot
from PIL import Image 
from skimage import io
from keras.models import load_model
from numpy.random import randint
from numpy import dtype, vstack
import SimpleITK as sitk
import pydicom as dicom
import time

model = load_model('8500_gan_150epok.h5')
folder1 = "D:/dicom_Normal_512_PoprKontrast/"
folder = os.listdir(folder1)


for dicoms in folder:

    data = dicom.read_file(folder1+dicoms)

    
    pixel_array = data.pixel_array
   

    img_2d = pixel_array.astype(float)
  
    img_2d_scaled = (np.maximum(img_2d,0) / img_2d.max()) * 255.0
    
    img_2d_scaled = np.uint8(img_2d_scaled)
    pixel_array_rgb = np.stack((img_2d_scaled,)*3, axis=-1)
    image_name = dicoms.split("/")[-1]
    
    test_src_img =  pixel_array_rgb
    test_src_img = (test_src_img - 127.5) / 127.5
    test_src_img = np.expand_dims(test_src_img, axis=0)
    ori_x = test_src_img
    y_pred = model.predict(ori_x)
    save_image_path = f"D:/8500_gan_150epok_dicom_Normal_Popr/{image_name}"
    
    cat_image = np.concatenate(y_pred, axis=0).astype(np.uint8)
    ret,cat_image = cv2.threshold(cat_image,127,255,cv2.THRESH_BINARY_INV)
    dim=(256,256)
 
    cat_image = cv2.resize(cat_image, dim, interpolation = cv2.INTER_AREA)
   
    #cat_image = np.uint16(cat_image)
    data.PhotometricInterpretation = 'RGB'
    data.Rows = 256
    data.SamplesPerPixel = 3
    data.add_new(0x00280006, 'US', 0)
    data.Columns = 256
    #ds.SamplesPerPixel = 3
    data.BitsAllocated = 8
    data.BitsStored = 8
    data.HighBit = 7
    #data.fix_meta_info()
    data.PixelData = cat_image.tobytes()
    
    data.save_as(save_image_path)


  

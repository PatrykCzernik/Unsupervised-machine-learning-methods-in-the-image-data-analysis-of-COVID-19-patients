
import os
import glob
import cv2
from cv2 import CV_16UC1
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


#folder1 = 'D:/ricord_images_PoprawionyKontrast/'
folder1 = "D:/dicom_Normal_512/"
#folder = sorted(glob.glob(os.path.join(folder1, '*.dcm')))
folder = os.listdir(folder1)


for dicoms in folder:

    data_set = dicom.read_file(folder1+dicoms)
    pixel_array = data_set.pixel_array
    Im = pixel_array
    Im_scaled = (np.maximum(Im,0) / Im.max()) * 255.0
    Im_scaled = np.uint8(Im_scaled)

    pixel_array_rgb = np.stack((Im_scaled,)*3, axis=-1)
    image_name = dicoms.split("/")[-1]
    
    test_src_img =  pixel_array_rgb
    test_src_img = (test_src_img - 127.5) / 127.5
    test_src_img = np.expand_dims(test_src_img, axis=0)
    ori_x = test_src_img
    save_image_path = f"D:/dicom_Normal_256_PoprKontrast/{image_name}"
    image_name = dicoms.split("/")[-1]
    cat_image = cv2.equalizeHist(Im_scaled)
    dim=(256,256)
    cat_image = cv2.resize(cat_image, dim, interpolation = cv2.INTER_AREA)
    pixel_array_rgb = np.stack((cat_image,)*3, axis=-1)
    cat_image = np.uint16(cat_image)
    data_set.PhotometricInterpretation = 'MONOCHROME2'
    data_set.Rows = 256
    data_set.SamplesPerPixel =1
    data_set.add_new(0x00280006, 'US', 0)
    data_set.Columns = 256
    data_set.BitsAllocated = 16
    data_set.BitsStored = 16
    data_set.HighBit = 15
    data_set.PixelData =  cat_image.tobytes()
    data_set.save_as(save_image_path)


  

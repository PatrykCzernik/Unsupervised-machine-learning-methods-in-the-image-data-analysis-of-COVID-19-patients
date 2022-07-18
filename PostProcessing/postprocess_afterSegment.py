import cv2
import numpy as np
from PostProcessing import PostProcessing
import os
from skimage import io
import pydicom as dicoms

# Load the image

images = os.listdir('D:/8500_gan_150epok_dicom_Normal_Popr') 
folder ='D:/8500_gan_150epok_dicom_Normal_Popr/'

for name in images:
    #img1 = cv2.imread('D:/8500_gan_150epok_Normal_PoprKontrast/'+name)
    data_set = dicoms.read_file(folder+name)
    #dicom = dicoms.dcmread(os.path.join(images,name))
    img1 = data_set.pixel_array
    img1 = np.uint8(img1)
    post_img =PostProcessing(img1)
    opening= post_img.opening()
    toconvex = PreProcessing(opening)
    convex_hull = toconvex.convexHull()
    closing = PreProcessing.closing(convex_hull)
    filling = PreProcessing.fill_hole(closing)
    filling = np.uint16(filling)
    save_image_path = f"D:/dicom_Normal_PoPostProcessing/{name}"
    data_set.PhotometricInterpretation = 'MONOCHROME2'
    data_set.Rows = 256
    data_set.SamplesPerPixel = 1
    data_set.add_new(0x00280006, 'US', 0)
    data_set.Columns = 256
    data_set.BitsAllocated = 16
    data_set.BitsStored = 16
    data_set.HighBit = 15
    data_set.PixelData = filling.tobytes()
    data_set.save_as(save_image_path)






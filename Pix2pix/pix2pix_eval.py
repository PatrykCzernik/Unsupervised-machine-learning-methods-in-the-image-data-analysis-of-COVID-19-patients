import os
import glob
import cv2
import numpy as np
from matplotlib import pyplot
from PIL import Image 
from skimage import io




from keras.models import load_model
from numpy.random import randint
from numpy import vstack

model = load_model('8500_gan_150epok.h5')

folder1 = 'D:/ricord_images_PoprawionyKontrast/'
folder = os.listdir(folder1)

X=256
Y=256

for x  in  folder:

        
	image_name = x.split("/")[-1]
	
  
	Im = cv2.imread(folder1+x)
	Im = cv2.resize(Im, (X, Y), interpolation = cv2.INTER_NEAREST)
	Im = (Im - 127.5) / 127.5
	Im = np.expand_dims(Im, axis=0)

	ori_x = Im
	
	prede = model.predict(ori_x)
	

	save_image_path = f"D:/8500_gan_150epok.h5/{image_name}"
	

	cat_image = np.concatenate(prede, axis=0)
	
	

	io.imsave(save_image_path, cat_image )

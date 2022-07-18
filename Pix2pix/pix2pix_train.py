import os
import glob
import tensorflow as tf
import cv2
import numpy as np
from matplotlib import pyplot 
from tensorflow.python.keras import backend as K
from keras.backend import set_session
from matplotlib import pyplot as plt


#os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
#export TF_FORCE_GPU_ALLOW_GROWTH=true
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES'] = "0000:02:00.0"

config = tf.compat.v1.ConfigProto()
sess = tf.compat.v1.Session(config=config)
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

#gpus = tf.config.experimental.list_physical_devices('GPU')
#for gpu in gpus:
 #   tf.config.experimental.set_memory_growth(gpu, True)


#config = tf.compat.v1.ConfigProto()
#config.gpu_options.allow_growth = True # Do not occupy all the video memory, allocate on demand
#config.gpu_options.per_process_gpu_memory_fraction = 0.4 #Limit GPU memory usage
#sess = tf.compat.v1.Session(config=config)
#K.set_session(sess) # set session

SIZE_X = 512
SIZE_Y = 512

tar_images = []

for directory_path in glob.glob('/home/pczernik/anaconda3/envs/gpuu/segmentacja/nowy_D/masks/'):
    for img_path in glob.glob(os.path.join(directory_path, "*.png")):
        img = cv2.imread(img_path, 1)       
        img = cv2.resize(img, (SIZE_Y, SIZE_X))
        #img.astype(np.float32)
        tar_images.append(img)
      
tar_images = np.array(tar_images, dtype = np.uint8)

src_images = [] 
for directory_path in glob.glob('/home/pczernik/anaconda3/envs/gpuu/segmentacja/nowy_D/CXR_png/'):
    for mask_path in glob.glob(os.path.join(directory_path, "*.png")):
        mask = cv2.imread(mask_path, 1)       
        mask = cv2.resize(mask, (SIZE_Y, SIZE_X), interpolation = cv2.INTER_NEAREST)  #Otherwise #ground truth changes due to interpolation
        #mask.astype(np.float32)
        src_images.append(mask)
         
src_images = np.array(src_images, dtype = np.uint8)
from pix2pix_model import define_discriminator, generator_UNET, define_gan, train, srednia

image_shape = src_images.shape[1:]
d_model = define_discriminator(image_shape)
g_model = generator_UNET(image_shape)
gan_model = define_gan(g_model, d_model, image_shape)

data = [src_images, tar_images]


def preprocess_data(data):
	
	X1, X2 = data[0], data[1]
	X1 = (X1 - 127.5) / 127.5
	X2 = (X2 - 127.5) / 127.5
	return [X1, X2]

dataset = preprocess_data(data)

from datetime import datetime 


a=train(d_model, g_model, gan_model, dataset, n_epochs=150, n_batch=1) 

g_model.save('4317_gan_150epok_bezAug.h5')
d_real= np.array(srednia(a[0],a[3]))
d_fake = np.array(srednia(a[1],a[3]))
d_total= (d_real+d_fake)/2
gene = srednia(a[2],a[3])
fig, ax1 = plt.subplots()
color = 'tab:green'
ax1.set_xlabel('Liczba epok')
ax1.set_ylabel('Strata dyskryminatora', color=color)
ax1.plot(np.arange(1,a[3]+1), d_total, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  

color = 'tab:blue'
ax2.set_ylabel('Strata generatora', color=color)  
ax2.plot(np.arange(1,a[3]+1), gene, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.savefig('4317_gan_150epok_bezAug.png',dpi=100)






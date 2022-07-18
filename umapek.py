import os  
from radiomics import featureextractor, getTestCase  
import SimpleITK as sitk
import numpy as np, cv2
import cv2
import six
import pandas as pd
from featureTopandas import feature2pd
from MyFeatureToPandas import MyFeatureToPandas
from sklearn.decomposition import PCA
import cv2
import matplotlib.pyplot as plt
from Divide_Lungs import Divide_Lungs
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import plotly.express as px
import umap
import pickle
from PIL import Image
from skimage.color import rgb2gray
PCA_5=pickle.load(open("PCA_calePluca_7komponentow",'rb'))

#Teraz UMAP
fitek = umap.UMAP(n_neighbors=200,n_components=2, min_dist=0.5,init='random', random_state=0)
umapik = fitek.fit_transform(PCA_5)
umap_breast_Df = pd.DataFrame(data = umapik
               , columns = ['UMAP 1', 'UMAP 2'])

h_UMAP = umap_breast_Df.values
Name = "UMAP_calePluca_2komponenty_z_PCA"
pickle.dump(h_UMAP, open(Name, 'wb'))


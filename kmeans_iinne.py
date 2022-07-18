from cProfile import label
import os  
from radiomics import featureextractor, getTestCase  
import SimpleITK as sitk
import numpy as np
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
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN


doKmeans=pickle.load(open("dicom_UMAP_calePluca_2komponenty_z_PCA",'rb'))
normale = doKmeans[0:8782]
covidy = doKmeans[8782:9963]
dbscan = DBSCAN(eps = 0.69, min_samples = 4).fit(covidy) model
labels = dbscan.labels_ 
ciekawe_co = np.unique(labels)

sc=plt.scatter(covidy[:,0], covidy[:,1], c =labels)
plt.legend(*sc.legend_elements(), title='klastry')
plt.title('DBSCAN')
plt.xlabel('UMAP 1')
plt.ylabel('UMAP 2')
plt.show()

kmeans = KMeans(n_clusters=3,precompute_distances='coss',init='random',algorithm='full', max_iter=200, n_init=10, random_state=0)
model = kmeans.fit(covidy)
predicted_values = kmeans.predict(covidy)


filtered_label0 = covidy[predicted_values == 0]
filtered_label1 = covidy[predicted_values == 1]
filtered_label2 = covidy[predicted_values == 2]

plt.scatter(filtered_label0[:,0],filtered_label0[:,1])
plt.scatter(filtered_label1[:,0],filtered_label1[:,1])
plt.scatter(filtered_label2[:,0],filtered_label2[:,1])
sc2=plt.scatter(covidy[:,0], covidy[:,1], c =predicted_values)
plt.legend(*sc2.legend_elements(), title='klastry')
plt.title('Wynik Kmeans')
plt.xlabel('UMAP 1')
plt.ylabel('UMAP 2')
plt.show()








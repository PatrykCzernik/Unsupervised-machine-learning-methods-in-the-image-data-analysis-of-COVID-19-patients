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
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import plotly.express as px
import umap
import pickle



imagePath = os.listdir('D:/wszystkie_obrazy') 
labelPath = os.listdir('D:/wszystkie_maski') 


params = os.path.join(os.getcwd(), "Params.yaml")
resulty=[]
extractor = featureextractor.RadiomicsFeatureExtractor(params)
for img,msk in zip(imagePath,labelPath):

    hm= sitk.ReadImage('D:/wszystkie_obrazy/'+img, sitk.sitkInt16)
    mm= sitk.ReadImage('D:/wszystkie_maski/'+msk, sitk.sitkInt16)


    result = extractor.execute(hm, mm, label=255)
    resulty.append(result)


warto=[]
#df = pd.DataFrame(columns=d[1])
df = pd.DataFrame()
for result in resulty:
   
    res = MyFeatureToPandas(result)
    #warto.append(res)
    df = df.append(res, ignore_index=True)
            

lol=df.values

rowIndex = df.index[0:8782]
rowIndex2 = df.index[8782:9963]
df.loc[rowIndex,'label']='Normal'
df.loc[rowIndex2,'label']='Covid-19'

#lol = lol.transpose()


#Odkomentuj to do PCA

# Scale data

scaled_data=StandardScaler().fit_transform(lol)
#Name = "WszystkieCechy_calePluca"
#pickle.dump(scaled_data, open(Name, 'wb'))



pca = PCA()
pca.fit(scaled_data)
pca_data = pca.transform(scaled_data)
per_var = np.round(pca.explained_variance_ratio_*100,decimals=1)
labels = ['PC'+str(x) for x in range (1,len(per_var)+1)]

pca_data = PCA(n_components=7)
principalComponents_data = pca_data.fit_transform(scaled_data)


# Robie teraz dla 7 komponentow
principal_breast_Df = pd.DataFrame(data = principalComponents_data
             , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4','principal component 5','principal component 6','principal component 7'])
hmmm=principal_breast_Df.values


targets = ['Covid-19','Normal']
colors = ['r','g']

#Teraz UMAP
fitek = umap.UMAP(n_neighbors=200,n_components=7, min_dist=0.5,init='random', random_state=0)
# #Standaryzacja
scaled_dataaa = StandardScaler().fit_transform(lol)
umapik = fitek.fit_transform(scaled_dataaa)
umap_data_Df = pd.DataFrame(data = umapik
              , columns = ['UMAP 1', 'UMAP 2','UMAP 3','UMAP 4','UMAP 5','UMAP 6','UMAP 7'])

h_UMAP = umap_data_Df.values
Name = "UMAP_calePluca_7komponentow"
pickle.dump(h_UMAP, open(Name, 'wb'))




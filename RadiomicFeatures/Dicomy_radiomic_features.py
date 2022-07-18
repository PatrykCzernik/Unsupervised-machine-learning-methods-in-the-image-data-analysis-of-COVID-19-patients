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





imagePath = os.listdir('D:/dicom_WszystkieObrazy') 
labelPath = os.listdir('D:/dicom_WszystkieMaski') 


params = os.path.join(os.getcwd(), "Params.yaml")
resulty=[]
extractor = featureextractor.RadiomicsFeatureExtractor(params)
for img,msk in zip(imagePath,labelPath):

    hm= sitk.ReadImage('D:/dicom_WszystkieObrazy/'+img, sitk.sitkUInt16)
    mm= sitk.ReadImage('D:/dicom_WszystkieMaski/'+msk, sitk.sitkUInt8)
    hm= sitk.GetArrayFromImage(hm)
    mm = sitk.GetArrayFromImage(mm)
    if len(hm.shape)>=3:
        hmm = np.squeeze(hm)
        
    else:
        hmm =hm
    if len(mm.shape)>=3:
        mmm = np.squeeze(mm)
    else:
        
        mmm = mm
    hm = sitk.GetImageFromArray(hmm)
    mm = sitk.GetImageFromArray(mmm)
    result = extractor.execute(hm, mm, label=255)
    resulty.append(result)
 



warto=[]

df = pd.DataFrame()
for result in resulty:
   
    res = MyFeatureToPandas(result)
    #warto.append(res)
    df = df.append(res, ignore_index=True)
            

lol=df.values

rowIndex = df.index[0:8780]
rowIndex2 = df.index[8780:9956]
df.loc[rowIndex,'label']='Normal'
df.loc[rowIndex2,'label']='Covid-19'

#lol = lol.transpose()


#Odkomentuj to do PCA

# Scale data

scaled_data=StandardScaler().fit_transform(lol)
Name = "dicom_WszystkieCechy_bezSkalowania_calePluca"
pickle.dump(lol, open(Name, 'wb'))



#pca = PCA()
#pca.fit(scaled_data)
#pca_data = pca.transform(scaled_data)
#per_var = np.round(pca.explained_variance_ratio_*100,decimals=1)
# labels = ['PC'+str(x) for x in range (1,len(per_var)+1)]
# # plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
# # plt.ylabel('Percentage of Explained Variance')
# # plt.xlabel('Principal Component')
# # plt.title('Scree Plot')
# # plt.show()
#pca_data = PCA(n_components=5)
#principalComponents_dataa = pca_data.fit_transform(scaled_data)
# #per_var_dla2 = np.round(principalComponents_dataa.explained_variance_ratio_*100,decimals=1)
# #dane = (pca_data[0],pca_data[1])
#principal_data_Df = pd.DataFrame(data = principalComponents_dataa
 #             , columns = ['principal component 1', 'principal component 2'])
#daneeee=principal_data_Df.values

# # Robie teraz dla 5 komponentow
#principal_data_Df = pd.DataFrame(data = principalComponents_dataa
 #             , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4','principal component 5'])
#daneeee=principal_data_Df.values

# # Odkomentuj to do PCA



#Name = "dicom_PCA_calePluca_5komponentow"
#pickle.dump(daneeee, open(Name, 'wb'))




# plt.figure(figsize=(10,10))
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=14)
# plt.xlabel('Principal Component - 1',fontsize=20)
# plt.ylabel('Principal Component - 2',fontsize=20)
# plt.title("PCA plot",fontsize=20)
targets = ['Covid-19','Normal']
colors = ['r','g']
# for target, color in zip(targets,colors):
#     indicesToKeep = df['label'] == target
#     plt.scatter(principal_data_Df.loc[indicesToKeep, 'principal component 1']
#               , principal_data_Df.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)
#     #plt.contour([principal_data_Df.loc[indicesToKeep, 'principal component 1']
#      #          , principal_data_Df.loc[indicesToKeep, 'principal component 2']], c =color )
# plt.xlabel('PC1 - {0}%'.format(per_var[0]))
# plt.ylabel('PC2 - {0}%'.format(per_var[1]))
# plt.legend(targets,prop={'size': 15})
# #plt.savefig('PCA_popr.png')
# plt.show()

#Teraz UMAP
fitek = umap.UMAP(n_neighbors=200,n_components=5, min_dist=0.5,init='random', random_state=0)
# #Standaryzacja
scaled_dataaa = StandardScaler().fit_transform(lol)
umapik = fitek.fit_transform(scaled_dataaa)

umap_data_Df = pd.DataFrame(data = umapik
               , columns = ['UMAP 1', 'UMAP 2','UMAP 3','UMAP 4','UMAP 5'])

h_UMAP = umap_data_Df.values
Name = "dicom_UMAP_calePluca_5komponentow"
pickle.dump(h_UMAP, open(Name, 'wb'))


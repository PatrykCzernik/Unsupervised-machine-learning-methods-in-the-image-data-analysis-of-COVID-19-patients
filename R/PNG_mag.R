
setwd('C:/Users/Patryk/Desktop/R_doMagisterki')
library(reticulate)
#py_install("pandas")
#py_install("pickle")
source_python("C:/Users/Patryk/Desktop/mgr/read_pickle.py")
#PCA_2 <- read_pickle_file("dicom_PCA_calePluca_2komponenty")
#PCA_2 <- as.data.frame(PCA_2)
#PCA_2<- cbind(PCA_2,'Label')
#colnames(PCA_2) <- c('PC1 - 52.1%','PC2 - 17.1%','Label')
#PCA_2[1:8781,3]='Normal'
#PCA_2[8782:9957,3]='Covid-19'
#source_python("C:/Users/Patryk/Desktop/mgr/read_pickle.py")
PCA_5 <- read_pickle_file("PCA_calePluca_7komponentow")
PCA_5 <- as.data.frame(PCA_5)
PCA_5<- cbind(PCA_5,'Label')
colnames(PCA_5) <- c('PC1 - 44.3%','PC2 - 13.1%','PC3','PC4','PC5','PC6','PC7','Label')
PCA_5[1:8783,8]='Normal'
PCA_5[8783:9963,8]='Covid-19'
### Teraz UMAPy
UMAP_2 <- read_pickle_file("UMAP_calePluca_2komponenty_z_PCA")
UMAP_2 <- as.data.frame(UMAP_2)
UMAP_2<- cbind(UMAP_2,'Label')
colnames(UMAP_2) <- c('UMAP 1', 'UMAP 2','Label')
UMAP_2[1:8783,3]='Normal'
UMAP_2[8783:9963,3]='Covid-19'
#source_python("C:/Users/Patryk/Desktop/mgr/read_pickle.py")
#UMAP_5 <- read_pickle_file("dicom_UMAP_calePluca_5komponentow")
#UMAP_5 <- as.data.frame(UMAP_5)
#UMAP_5<- cbind(UMAP_5,'Label')
#colnames(UMAP_5) <- c('UMAP 1','UMAP 2','UMAP 3','UMAP 4','UMAP 5','Label')
#UMAP_5[1:8781,6]='Normal'
#UMAP_5[8782:9957,6]='Covid-19'

### Wszystkie cechy
#vector=c()
#for (i in 1:86) {
#  vector[i] = sprintf("V%d",i)
  
#}

#All <- read_pickle_file("dicom_WszystkieCechy_calePluca")
#All<-read_pickle_file("dicom_WszystkieCechy_calePluca")
#All <- as.data.frame(All)
#All<- cbind(All,'Label')
#colnames(All) <- c(vector,'Label')
#All[1:8781,87]='Normal'
#All[8782:9957,87]='Covid-19'



#### COntourploty!!!!!!!!!!!!!!!!!!
library(scDataviz)
test<-PCA_5[,1:2]
test<-as.data.frame(test)
normal_PCA<-PCA_5[which(PCA_5$Label=='Normal'),]
covid_PCA<-PCA_5[which(PCA_5$Label=='Covid-19'),]
normal_PCA2<-normal_PCA[,1:2]
covid_PCA2<-covid_PCA[,1:2]
colnames(normal_PCA2) <- c('PC1 - 44.3%','PC2 - 13.1%')
colnames(covid_PCA2) <- c('PC1 - 44.3%','PC2 - 13.1%')

#normal_PCA2<-PCA_2[which(PCA_2$Label=='Normal'),]
#covid_PCA2<-PCA_2[which(PCA_2$Label=='Covid-19'),]

normal_UMAP2<-UMAP_2[which(UMAP_2$Label=='Normal'),]
covid_UMAP2<-UMAP_2[which(UMAP_2$Label=='Covid-19'),]



#BiocManager::install("scDataviz") 
#library(scDataviz)
contour_PCA_caly<- contourPlot(PCA_5,
                               reducedDim = 'PCA',
                               lowcol = "white",
                               highcol = "black",
                               bins = 350,
                               title='PCA',
                               xlim=c(-20,20),
                               ylim=c(-5,15),
                               subtitle = 'Zdrowi + Covid-19',
                               dimColnames = c("PC1 - 44.3%", "PC2 - 13.1%"),
                               verbose= TRUE)
contour_PCA_caly#+xlim(-20,20)

contour_PCA_Normal <- contourPlot(normal_PCA2,
                                  reducedDim = 'PCA',
                                  lowcol = "greenyellow",
                                  highcol = "green4",
                                  bins = 350,
                                  title='PCA',
                                  xlim=c(-20,20),
                                  ylim=c(-5,15),
                                  subtitle = 'Zdrowi',
                                  dimColnames = c("PC1 - 44.3%", "PC2 - 13.1%"),
                                  verbose= TRUE)

contour_PCA_Normal

par(new=TRUE)
contour_PCA_covid <- contourPlot(covid_PCA2,
                                 reducedDim = 'PCA',
                                 bins = 350,
                                 lowcol = "red",
                                 highcol = "red4",
                                 title='PCA',
                                 subtitle = 'Covid 19',
                                 xlim=c(-20,20),
                                 ylim=c(-5,15),
                                 dimColnames = c("PC1 - 44.3%", "PC2 - 13.1%"),
                                 
                                 verbose= TRUE)
#contour_PCA_covid+xlim(-20,20)
#contour_PCA_covid+ylim(-5,15)
contour_PCA_covid

#cowplot::plot_grid(contour_PCA_Normal, contour_PCA_covid)


contour_UMAP_Normal <- contourPlot(normal_UMAP2,
                                   reducedDim = 'UMAP',
                                   bins = 350,
                                   title='UMAP',
                                   subtitle = 'Zdrowi',
                                   lowcol = "greenyellow",
                                   highcol = "green4",
                                   xlim=c(-20,20),
                                   ylim=c(-5,15),
                                   dimColnames = c("UMAP 1", "UMAP 2"),
                                   verbose= TRUE)

contour_UMAP_covid <- contourPlot(covid_UMAP2,
                                  reducedDim = 'UMAP',
                                  bins = 350,
                                  title='UMAP',
                                  lowcol = "red",
                                  highcol = "red4",
                                  subtitle = 'Covid 19',
                                  xlim=c(-20,20),
                                  ylim=c(-5,15),
                                  dimColnames = c("UMAP 1", "UMAP 2"),
                                  verbose= TRUE)

contour_UMAP_Normal
contour_UMAP_covid

contour_UMAP_caly<- contourPlot(UMAP_2,
                                reducedDim = 'UMAP',
                                lowcol = "white",
                                highcol = "black",
                                bins = 350,
                                title='UMAP',
                                xlim=c(-20,20),
                                ylim=c(-5,15),
                                subtitle = 'Zdrowi + Covid-19',
                                dimColnames = c("UMAP 1", "UMAP 2"),
                                verbose= TRUE)

contour_UMAP_caly
#cowplot::plot_grid(contour_UMAP_Normal, contour_UMAP_covid)


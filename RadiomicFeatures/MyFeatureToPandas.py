import radiomics
import six
from radiomics import featureextractor
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

extractor = featureextractor.RadiomicsFeatureExtractor()

def MyFeatureToPandas(result):

    
    #sub_dict = {}
    valuee = []
    col_names=[]
    for key, value in six.iteritems(result):
        if key.find('lbp-2D') == 0:
            valuee.append(value)
            col_names.append(key)

          
    output = pd.DataFrame.from_dict(valuee).transpose()
    #valuee = np.array(valuee).transpose()

    
    #output = pd.DataFrame.from_dict(sub_dict, orient='index', columns=[index]).transpose()
    
    return output
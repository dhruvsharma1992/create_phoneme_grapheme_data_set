import pandas as pd
import pandas.rpy.common as com
from rpy2.robjects.packages import importr
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()
import numpy as np
r = robjects.r
r.library("randomForest")

def getModelRandomForest(trainingSet,classes,columns):
    df = pd.DataFrame(data=trainingSet, columns=columns)
    X = com.convert_to_r_dataframe(df)
    Y = robjects.FactorVector(classes)
    model = r.randomForest(X, Y,ntree=5)
    return model

def predictRandomForest(testSet,model):
    return 'predictions'
import pandas as pd
import pandas.rpy.common as com
from rpy2.robjects.packages import importr
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()
import numpy as np
#from scikits.statsmodels.tools import categorical
r = robjects.r
r.library("randomForest")
def convert_factor(obj):
    """
    Taken from jseabold's PR: https://github.com/pydata/pandas/pull/9187
    """
    ordered = r["is.ordered"](obj)[0]
    categories = list(obj.levels)
    codes = np.asarray(obj) - 1  # zero-based indexing
    values = pd.Categorical.from_codes(codes, categories=categories,
                                       ordered=ordered)
    return values
def dataFrametoMatrix(df):
    mat = []
    for i in range(len(df[df.keys()[0]])):
        li  =[]
        for key in df.keys():
            li+=[df[key][i]]
        mat+=[li]
    
    return mat

def getModelRandomForest(trainingSet,classes,columns):
    df = pd.DataFrame(data=dataFrametoMatrix(trainingSet), columns=columns)
    df['b']=classes
    #df = r.matrix(trainingSet)
    #X = com.convert_to_r_dataframe(df)
    #X = robjects.DataFrame(trainingSet)
    #Y =  robjects.DataFrame({'character':classes})
    #Y= pd.Series(classes, dtype="category")
    #Y = com.convert_robj(series, True)
    #print np.random.rand(100, 10)
    #Y = com.convert_to_r_dataframe (pd.DataFrame(data=classes, columns=['character']))
    #Y = robjects.FactorVector(classes)
    #print Y
    
    model = r.randomForest(robjects.Formula('b ~ .'), data=df,ntree=5)
    print 'model', type(model),model
    return model
    '''
    trainingSet = pd.get_dummies(np.array(trainingSet)).values.argmax(1)
    classes = pd.get_dummies(np.array(classes)).values.argmax(1)
    rfs = [generate_rf(trainingSet, classes, [], []) for i in xrange(10)]
    rf_combined = reduce(combine_rfs, rfs)
    return rf_combined'''
def predictRandomForest(testSet,model,classes):    
    testSet = pd.DataFrame(data=testSet, columns=classes)
    print testSet
    predictions = r.predict(model,testSet)
    print predictions
    return predictions

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()

def generate_rf(X_train, y_train, X_test, y_test):
    #print X_train
    X_train = vec.fit_transform(X_train).toarray()
    y_train = vec.fit_transform(y_train).toarray()
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    #print "rf score ", rf.score(X_test, y_test)
    return rf

def combine_rfs(rf_a, rf_b):
    rf_a.estimators_ += rf_b.estimators_
    rf_a.n_estimators = len(rf_a.estimators_)
    return rf_a

'''iris = load_iris()
X, y = iris.data[:, [0,1,2]], iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33)
# in the line below, we create 10 random forest classifier models
rfs = [generate_rf(X_train, y_train, X_test, y_test) for i in xrange(10)]
print generate_rf(X_train, y_train, X_test, y_test)
# in this step below, we combine the list of random forest models into one giant model
rf_combined = reduce(combine_rfs, rfs)
# the combined model scores better than *most* of the component models
print "rf combined score", rf_combined.score(X_test, y_test)'''
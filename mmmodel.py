#from sklearn.ensemble import BaggingClassifier
from sklearn.naive_bayes import GaussianNB
#from sklearn.neighbors import KNeighborsClassifier
from dictionary import *
from sqliteCRUD import *
crud_obj = SqliteCRUD(DB_NAME,TABLE_NAME)
factors = []
for key in arpabetClass.keys():    
    if not arpabetClass[key][0] in factors:
        factors += [arpabetClass[key][0]]                    
    if not arpabetClass[key][1] in factors:
        factors += [arpabetClass[key][1] ]  
chr = []
row = crud_obj.cursor.execute('select  distinct character from training_table ;')
for val in row:    
    chr+=[str(val[0])   .encode('ascii', 'ignore') ]           
chr+=['#'] 
models = [ [0], [1], [2], [4], [3], [5],\
          [0,1], [0,2], [0,3], [0,4], [0,5 ],\
          [1,2], [1,3], [1,5], [1,4],\
          [2,3],[2,4],[2,5],\
          [3,4],[3,5],\
          [4,5]]

def getXY(input):
    X = [ x[1:] for x in input]
    Y = [ x[0] for x in input]
    return [X,Y]

def getData(input,li):
    output = [  chr.index(input[6])]
    for index in li:
        if index  <3  :
            output +=[ factors.index( arpabetClass[input[index].lower()][0])]
        else:
            output +=[ factors.index( arpabetClass[input[index].lower()][1]) ]
    return output 


model_file = file('model_score.txt','w')
model_file.close()
for ph in arpabetDict.keys():
    model_file = file('model_score.txt','a')
    ph = ph.upper()
    print ph
    model_file.write(ph)
    #bagging = BaggingClassifier(GaussianNB(), max_samples=0.5, max_features=0.5)    
    crud_obj.cursor.execute('select  "1_before_arp","2_before_arp" ,"3_before_arp" ,"1_after_arp" ,"2_after_arp" ,"3_after_arp" , character from training_table  where arpabet is "'\
                                +str(ph)+'" ORDER BY RANDOM()   ;')                    
    rows = crud_obj.cursor.fetchall()
    training = []        
    for row in rows:
            record = [str(rec).encode('ascii', 'ignore') for rec in row] 
            training+=[record ]
    for model in models:
        print model
        training_set = [ getData(input, model) for input in training]       
        random.shuffle(training_set)
        testing_set = training_set[:int(len(training_set)*0.4)]
        random.shuffle(training_set)
        training_set = training_set[:int(len(training_set)*0.8)]
        [X_train, Y_train] = getXY(training_set)
        [X_test, Y_test] = getXY(testing_set)
        clf = GaussianNB()
        clf.fit(X_train, Y_train)    
        acc = clf.score(X_test,Y_test)
        model_file.write(","+ str(acc) )
    model_file.write("\n")
    model_file.close()
    
    

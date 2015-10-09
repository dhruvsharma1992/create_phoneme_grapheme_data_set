from languagePreProcess import *
import codecs
from os.path import isfile, join
import math
from sqliteCRUD import *
from dictionary import arpabetClass
from numpy import character
crud_obj = SqliteCRUD(DB_NAME, TABLE_NAME)
from RmodulesImpl import *
rf={}

def getMatrix(inputMat):
    n= (int)(math.sqrt(4*len(inputMat)+1)-1)/2
    #print n,len(inputMat)
    matrix =  [[] for i in range(n)]
    for i in range(n): 
        for j in  range(n):
            matrix[j].append(inputMat[n*i+j])
    #matrix[0]=matrix
    error =[ [] for i in range(n)] 
    for i in range(n):
         error[i].append(inputMat[n*n+i])
        
    return [matrix,error]
def getF1score(mat  ):
    
    for i in range(len(mat)):
        print i
        for j in range(len(mat[i])):
            print mat[i][j],
        print
    #return
    count = [] 
    f1=0
    for i in range (len(mat)):
        precision = float( float(mat[i][i])/sum(mat[i]))
        recall = 0
        for j in range(len(mat)):
            recall+=mat[j][i]
        if mat[i][i] ==0:
            recall = 0
        else:
            recall =  float (  float(mat[i][i]) / recall) #aot 
        
        count += [sum(mat[i])]
        if precision == 0 and recall == 0:
            f1 = 0
        else:
            f1 += 2*precision*recall/(precision+recall)*count[i]
        #else:
        print precision, recall, f1, count[i]
    f1 = f1/sum(count)
    print 'F1',f1
#def getF1score(mat):
def train(ph):
    crud_obj.cursor.execute('select arpabet, character,"1_before_arp","2_before_arp" ,"3_before_arp" ,"1_after_arp" ,"2_after_arp" ,"3_after_arp" from training_table where arpabet is "'\
                            +str(ph)+'" ORDER BY RANDOM()  LIMIT 1000 ;')                    
    rows = crud_obj.cursor.fetchall()
    ch_count = {}
    records = []
    ch = []
    for row in rows:
        record = [str(rec).encode('ascii', 'ignore') for rec in row]          
        records += [[ arpabetClass[phoneme.lower()][0] for phoneme in record[2:]]]
        ch += [record[1]] 
        '''if not record[1] in ch_count.keys():
            ch_count[record[1]]=0
        ch_count[record[1]]+=1'''
    
    rf[ph] = getModelRandomForest(records,ch,["1_before_arp","2_before_arp" ,"3_before_arp" ,"1_after_arp" ,"2_after_arp" ,"3_after_arp"])
        #row = crud_obj.cursor.fetchone()
    #print records
    #print ch_count
        
 
def featureSet(i, arp_map): 
        arpabet = str(arp_map[i]) 
        if (i) > 0:
            one_before_arp = str(arp_map[i-1] )
            one_before_chr = str(arp_map[i-1])
        else:
            one_before_arp = '#'
            one_before_chr = '#'

        if (i-1) > 0:
            two_before_arp = str(arp_map[i-2] )
            two_before_chr = str(arp_map[i-2])
        else:
            two_before_arp = '#'
            two_before_chr = '#'

        if (i-2) > 0:
            three_before_arp = str(arp_map[i-3])
            three_before_chr = str(arp_map[i-3])
        else:
            three_before_arp = '#'
            three_before_chr = '#'

        if (i+1) < len(arp_map):
            one_after_arp = str(arp_map[i+1])
            one_after_chr = str(arp_map[i+1])
        else:
            one_after_arp = '#'
            one_after_chr = '#'

        if (i+2) < len(arp_map):
            two_after_arp = str(arp_map[i+2])
            two_after_chr = str(arp_map[i+2])
        else:
            two_after_arp = '#'
            two_after_chr = '#'

        if (i+3) < len(arp_map):
            three_after_arp = str(arp_map[i+3])
            three_after_chr = str(arp_map[i+3])
        else:
            three_after_arp = '#'
            three_after_chr = '#'
        
        toDB_list = []
        toDB_list.append(arpabet)  
        toDB_list.append(one_before_arp)
        toDB_list.append(two_before_arp)
        toDB_list.append(three_before_arp)
        toDB_list.append(one_after_arp)
        toDB_list.append(two_after_arp)
        toDB_list.append(three_after_arp)
        return toDB_list

def classifyPhoneme(phoneme, features): 
    if not phoneme in rf.keys():
        train(phoneme)           
    return predictRandomForest(features, rf[phoneme])


def test():
    with codecs.open(join(join(join("dataset","languages"),"fr"),"IPA_1.txt"),   encoding="UTF-8"   ) as fread:
        for words in fread:
            word_ = []
            word = words.strip()
            length=0        
            while length < len(words.strip()):                
                    rep = word[length:length+2] .encode('utf-8')
                    if rep in ipa.keys():
                        if type(ipa[rep]) is list:
                            word_.append(ipa[rep][0])
                        else:
                            word_.append("_")
                            
                        length +=1                    
                    else:
                        rep = word[length] .encode('utf-8')                    
                        if rep in ipa.keys():           
                            if type(ipa[rep]) is list:                       
                               word_.append(ipa[rep][0])
                            else:
                                word_.append("_")
                        else:
                            rep = word[length] .encode('utf-8') 
                            print  'error',rep,repr(rep),word.encode('UTF-8')
                            word_=[]
                    length += 1 
            word_= (" ").join(word_)
            print "--",word_.split()
            phonemeSet = word_.split()
            character_set = []
            for i in range(len(phonemeSet)):
                print featureSet( i ,phonemeSet)
                character_set += classifyPhoneme(phonemeSet[i],featureSet( i ,phonemeSet))
            #generated_word = "".join(character_set)

train('K')
#print 
 
#print r.dimnames(rf[8])'''

'''tring = robjects.StrVector([str(ch) for ch in range(1,10)])
    
    df = pd.DataFrame(data=np.random.rand(100, 30), columns=["a{}".format(i) for i in range(30)])
    df["b"] = np.random.randint(2, size=100)
    x=[]
    for i in range(0,100):
        if i % 3 == 0:
            x+=['a']
        elif i % 3 == 1:
            x+= ['c']
        else:
            x+=['b']
    
    #print robjects.FactorVector(x)
    X = com.convert_to_r_dataframe(df.drop("b", axis=1))
    Y = robjects.FactorVector(x)
    #print Y,X
    # build rf model
    rf = r.randomForest(X, Y)
    
    # print Mean Decrease Gini and Field names
    print rf.rx("confusion")
    #print rf.rx("confusion")[0]
    #print rf.rx("confusion")[0][:5]
    result = getMatrix(rf.rx("confusion")[0])
    #print result[0]
    getF1score( result[0])'''
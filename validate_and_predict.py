from __future__ import division
from languagePreProcess import *
from copy import deepcopy
from dictionary import *
import numpy
import codecs
from sklearn.naive_bayes import GaussianNB
from dictionary import *
from sqliteCRUD import *
from sklearn.externals import joblib

crud_obj = SqliteCRUD(DB_NAME,TABLE_NAME)
factors = []
linear_model_dict =  joblib.load('linear_model_dict.pkl')
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
def getModelCoefficient():
    score_file = open("model_score.txt","r")
    coeff_mult_dict = {}
    for x in score_file.read().strip().split():
        cff_val = x.split(",")
        coeff_mult_dict[cff_val[0]] = cff_val[1:]
    return coeff_mult_dict
coeff_mult_dict = getModelCoefficient()
#print coeff_mult_dict
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
        toDB_list.append(one_before_arp)
        toDB_list.append(two_before_arp)
        toDB_list.append(three_before_arp)
        toDB_list.append(one_after_arp)
        toDB_list.append(two_after_arp)
        toDB_list.append(three_after_arp)
        toDB_list.append(arpabet)
        return toDB_list
def getXY(input):
    X = [ x[1:] for x in input]
    Y = [ x[0] for x in input]
    return [X,Y]

def getData(input,li):
    #print input,"ooooooooooooooo",len(li)
    output = [  chr.index(input[6])]
    for index in li:
        if index  <3  :
            output +=[ factors.index( arpabetClass[input[index].lower()][0])]
        else:
            output +=[ factors.index( arpabetClass[input[index].lower()][1]) ]
    #print input,"####",output,"@@"
    return output
def getTestData(input,li):
    output=[]
    for index in li:
        if index  <3  :
            output +=[ factors.index( arpabetClass[input[index].lower()][0])]
        else:
            output +=[ factors.index( arpabetClass[input[index].lower()][1]) ]
    #print input,"####",output,"@@"
    return output
from os.path import isfile, join
def getTestSet():
    phonemeSets = []
    with codecs.open(join(join(join("dataset","languages"),"fr"),"IPA_1.txt"),\
                        encoding="UTF-8"   ) as fread:        
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
                                word_=[]
                        length += 1
                word_= (" ").join(word_)
                phonemeSet = word_.split()
                phonemeSets += [phonemeSet]
                break
    return phonemeSets
def getAllModelList(ph):
        ph = ph.upper()
        #print ph
        crud_obj.cursor.execute('select  "1_before_arp","2_before_arp" ,"3_before_arp" ,"1_after_arp" ,"2_after_arp" ,"3_after_arp" , character from training_table  where arpabet is "'\
                                    +str(ph)+'" ORDER BY RANDOM()   ;')
        rows = crud_obj.cursor.fetchall()
        training = []
        for row in rows:
                record = [str(rec).encode('ascii', 'ignore') for rec in row]
                training+=[record ]
        model_collect_list = []
        for model in models:
            training_set = [ getData(input, model) for input in training]
            [X_train, Y_train] = getXY(training_set)
            clf = GaussianNB()
            clf.fit(X_train, Y_train)
            cpy_clf = deepcopy(clf)
            model_collect_list.append(cpy_clf)
        cpy_model_collect_list = deepcopy(model_collect_list)
        linear_model_dict[ph] = {'model':model_collect_list,'Y': sorted(set(Y_train))}
        #return linear_model_dict

def classifyPhoneme(fs_row):
    observation = fs_row[-1].upper()
    #print fs_row
    featureset = fs_row[:-1]
    '''if not fs_row[-1] in linear_model_dict.keys():
        getAllModelList(fs_row[-1])'''
    predict_matrix = [[ 0 for j in xrange(len(models))] for i in xrange(len(linear_model_dict[observation]['Y']))]
    for i in range(len(models)):
    #temp_len = list(range(0,len(fs_row)))
        vect_X_lang = getTestData(featureset,models[i])
        probability_vector = linear_model_dict[observation]['model'][i].predict_proba([vect_X_lang])[0]
        #print probability_vector
        for j in xrange(len(probability_vector)):
            predict_matrix[j][i] =    float(probability_vector[j]) * float(coeff_mult_dict[observation][i])
            #print 'probability_vector',probability_vector[j],'coeff_mult_dict',coeff_mult_dict[observation][i],'mul',(float(probability_vector[j]) * float(coeff_mult_dict[observation][i])), 2*3  
    predict_matrix = [sum(row) for row in predict_matrix]        
    '''print predict_matrix,
    print max(predict_matrix),  
    print predict_matrix.index(max(predict_matrix)),
    print linear_model_dict[observation]['Y'][predict_matrix.index(max(predict_matrix))],   '''     
    return chr[linear_model_dict[observation]['Y'][predict_matrix.index(max(predict_matrix))] ]  

def getFeatureSetListXLang():
    test_list = getTestSet()
    for row in test_list:
        for i in range(0,len(row)):
            fs_row = featureSet(i,row)
            print classifyPhoneme(fs_row)
             #print  fs_row[-1],fs_row,models[i], vect_X_lang]
                
                #print linear_model_dict[observation]['model'][i].predict_log_proba([vect_X_lang]),linear_model_dict[observation]['model'][i].predict([vect_X_lang]),linear_model_dict[observation]['Y']
                #for clf in models_to_fit[fs_row[len(fs_row)-1]]:
                 #   print zip(clf.classes_, clf.predict_proba(fs_row)[0])
                #Manipulate above line to make it fit the need and function parameter
#list of resultant probability modelwise for a given arp
def getArgMaxValue(model_prob_list,coeff_mult_dict,arp):
    consider_list = coeff_mult_dict[arp]
    if len(consider_list) != len(model_prob_list):
        return "X"
    #else:
     #   return sum([x*y for x,y in zip(consider_list,model_prob_list)])
def chooseBestResult(prob_class_list):
    #[[chr,prob],[chr2,prob2]...] returns the best chr according to prob
    max_tup = prob_class_list[0]
    for x in prob_class_list:
        if max_tup[1] > x[1]:
            max_tup = x
    return max_tup[0]

def main():
    '''for x in arpabetDict.keys():
        getAllModelList(x.upper())
    
    joblib.dump(linear_model_dict, 'linear_model_dict.pkl') '''
    #linear_model_dict = joblib.load('linear_model_dict.pkl')
    #print linear_model_dict.keys()
    f=file('output_model.txt','w').close()
    with codecs.open(join(join(join("dataset","languages"),"fr"),"IPA_1.txt"),\
                        encoding="UTF-8"   ) as fread:        
           for words in fread:
                f=file('output_model.txt','a')
    
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
                                word_=[]
                        length += 1
                word_= (" ").join(word_)
                phonemeSet = word_.split()
                character_set = []
                for i in range(0,len(phonemeSet)):
                    fs_row = featureSet(i,phonemeSet)
                    character_set += classifyPhoneme(fs_row)
                
                generated_word = "".join(character_set)
                generated_word = "".join(generated_word.split("#"))
                print generated_word
                 
                f.write(generated_word+"\n")
                
                f.close()    
        
        
    
    
    #getFeatureSetListXLang()
    #print getTestSet()
    #for items , val in getModelCoefficient().iteritems():
    #   print items,val
main()

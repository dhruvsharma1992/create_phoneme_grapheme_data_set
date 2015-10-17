from __future__ import division
from dictionary import *
import numpy
from sqliteCRUD import * 
import pickle
crud_obj = SqliteCRUD(DB_NAME, TABLE_NAME)
hs = []
for key in arpabetDict.keys():
        
        for state in arpabetDict[key]:
            if not state.upper() in hs :
                hs +=[state.upper()]  
    
hs+=['#'] 
sp= [ float(1)/float(len(hs)) for i in xrange(len(hs))]

observation_states = [ ph.upper() for ph in arpabetDict.keys()]
def write_tm():
    
    transition_mat =  [[1 for i in xrange(len(hs))] for i in xrange(len(hs))]
    one_bef = [ len(hs) for i in xrange(len(hs)) ]
    #print 
    crud_obj.cursor.execute('select  "1_before_chr",character, count(*) from training_table   group by  character, "1_before_chr";')              
    rows = crud_obj.cursor.fetchall()
    for row in rows:
                record = [str(rec).encode('ascii', 'ignore') for rec in row]
                try:
                    transition_mat[hs.index(record[0])][hs.index(record[1])]+=  int(record[2])
                    
                    one_bef[hs.index(record[0])]+=int(record[2])
                except ValueError:
                    continue    
    for i in xrange(len(hs)): 
        for j in xrange(len(hs)):
            transition_mat[i][j] = float(transition_mat[i][j])/float(one_bef[i])   
    with open('transition_mat','w') as dump_file:
        pickle.dump(transition_mat,dump_file)

def readTM():
     with open('transition_mat','rb') as dump_file:
         transaction_matrix = pickle.load(dump_file)
         return transaction_matrix
 
def write_em():
    
    emission_mat =  [[0 for i in xrange(len(observation_states))] for i in xrange(len(hs))]
    one_bef = [ 0.1 for i in xrange(len(hs)) ]
    #print 
    crud_obj.cursor.execute('select  character,arpabet,  count(*) from training_table   group by  character  , arpabet')              
    rows = crud_obj.cursor.fetchall()
    for row in rows:
                record = [str(rec).encode('ascii', 'ignore') for rec in row]
                print record
                try:
                    emission_mat[hs.index(record[0])][observation_states.index(record[1])]+=  int(record[2])
                    
                    one_bef[hs.index(record[0])]+=int(record[2])
                except ValueError:
                    print 'valueerror'
                    continue    
    for i in xrange(len(hs)): 
        for j in xrange(len(observation_states)):
            emission_mat[i][j] = float(emission_mat[i][j])/float(one_bef[i])   
    with open('emission_mat','w') as dump_file:
        pickle.dump(emission_mat,dump_file)

def readEM():
     with open('emission_mat','rb') as dump_file:
         emission_matrix = pickle.load(dump_file)
         return emission_matrix
#readTM()
'''write_em()
write_tm()
mat = readEM()
for i in range(len(mat)):
    total = 0
    for j in range(len(mat[i])):
        total+= mat[i][j] 
    print hs[i],total,mat[i]'''

import codecs
from languagePreProcess import *

from os.path import isfile, join
def getTestSet():
    phonemeSets = []
    with codecs.open(join(join(join("dataset","languages"),"fr"),"IPA_1.txt"),\
                        encoding="UTF-8"   ) as fread:
        
           for words in fread:
                word_ = []
                word = words.strip()
                
                #print word.encode('UTF-8')
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
    return phonemeSets

def getword(li):
    return "".join(("".join(li.split(" "))).split("#"))

from sklearn import hmm        
model = hmm.MultinomialHMM(n_components=len(hs))
model._set_startprob(sp)
model._set_transmat(readTM())
model._set_emissionprob(readEM())
fo=file('output.txt','w')
inputs=getTestSet()
for input  in  inputs: 
    input = [observation_states.index(phoneme.upper()) for phoneme in input]
    logprob, output = model.decode( input, algorithm="viterbi")
    print "Input: ", " ".join(map(lambda x: observation_states[x], input))
    output = " ".join(map(lambda x: hs[x], output))    
    print output
    
    fo.write(getword(output)+"\n")
fo.close()
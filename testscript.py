import pickle
import sys
from math import *
from sqliteCRUD import *
from dictionary import *
import sqlite3 as lite
def pickleTester():
    i=0
    with open('testSet','rb') as dump_file:
        try:
            arp_map = pickle.load(dump_file)
            while arp_map:
                i+=1
                for x in arp_map:
                        print i,':',x
            #    print arp_map
                print '_'*60
                arp_map = pickle.load(dump_file)
        except Exception as e:
            print e
        finally :
            print 'file edit completed'

def addProbs(freq_list):
    total_records = sum(int(rec[2]) for rec in freq_list)
    for record in freq_list:
        record[2] = int(record[2])
        record.append(float(record[2])/total_records)
    return
def entropyTester():
    crud_obj = SqliteCRUD(DB_NAME, TABLE_NAME)
    #crud_obj.printTable()
    #freq_list = crud_obj.getFrequencies()
    #print freq_list
    #addProbs(freq_list)
    #print '_'*50
    #print freq_list
    #parameterAnalysis(crud_obj)
    for arp,values in arpabetDict.iteritems():
        for value in values:
            print arp,value
            getEntropyCounts(crud_obj, arp.upper(), value.upper())
def getResultDB():
    conn = lite.connect('result_DB.db')
    cur = conn.cursor()
    return conn,cur
def getEntropyCounts(crud_obj, arp, value):
        result_list = []
        
        try:
            ins_str = ''
            for param_type in ['vowel','consonant','#']:
                for arp_type in ['1_before_arp_type','2_before_arp_type','3_before_arp_type'\
                             ,'1_after_arp_type','2_after_arp_type','3_after_arp_type']:

                    crud_obj.cursor.execute("select count(arpabet) from training_table where \
                    ( \""+arp_type+"\" is '"+param_type+"') and (arpabet is '"+str(arp)+"') and \
                    (character is '"+str(value)+"');")
                    row = crud_obj.cursor.fetchone()
                    if row:
                        record = [str(rec).encode('ascii', 'ignore') for rec in row]
                        print str(record[0]),arp_type,param_type
                        ins_str += "\'"+str(record[0])+"\',"
                        #row = crud_obj.cursor.fetchone()
            ins_query = "INSERT INTO 'result_no_hash' VALUES ("+"'"+arp+"','"+value+"',"\
                  +ins_str.strip(',')+");"
            print ins_query
            pushToResult(ins_query)
        except Exception as e:
            print 'mapping query couldn\'t be executed, exiting ..'
            print e
def pushToResult(ins_query):
    try:
        conn,cur = getResultDB()
        cur.execute(ins_query)
        conn.commit()
    except Exception as e:
        print traceback.format_exc()
        sys.exit(0)
def parameterAnalysis(crud_obj):
    crud_obj.getParameterMapping()
    return
def generateEntropies():
    getProbabilities()
    return

def getProbabilities():
    try:
        conn,cur = getResultDB()
        open("Entropy_list.csv","w").close()
        with open("Entropy_list.csv","w") as f:
            f.write("arpabet,character,1_before,2_before,3_before,1_after,2_after,3_after\n")
        prob_stmt = 'select \"arpabet\",\"character\",(\"1_before_vowel\"/(\"1_before_vowel\"+\"1_before_consonant\"+\"1_before_hash\")) as \'p(1_before_vowel) \',(\"1_before_consonant\"/(\"1_before_vowel\"+\"1_before_consonant\"+\"1_before_hash\")) as \'p(1_before_consonant) \',(\"1_before_hash\"/(\"1_before_vowel\"+\"1_before_consonant\"+\"1_before_hash\")) as \'p(1_before_hash) \',(\"2_before_vowel\"/(\"2_before_vowel\"+\"2_before_consonant\"+\"2_before_hash\")) as \'p(2_before_vowel) \',(\"2_before_consonant\"/(\"2_before_vowel\"+\"2_before_consonant\"+\"2_before_hash\")) as \'p(2_before_consonant) \',(\"2_before_hash\"/(\"2_before_vowel\"+\"2_before_consonant\"+\"2_before_hash\")) as \'p(2_before_hash) \',(\"3_before_vowel\"/(\"3_before_vowel\"+\"3_before_consonant\"+\"3_before_hash\")) as \'p(3_before_vowel) \',(\"3_before_consonant\"/(\"3_before_vowel\"+\"3_before_consonant\"+\"3_before_hash\")) as \'p(3_before_consonant) \',(\"3_before_hash\"/(\"3_before_vowel\"+\"3_before_consonant\"+\"3_before_hash\")) as \'p(3_before_hash) \',(\"1_after_vowel\"/(\"1_after_vowel\"+\"1_after_consonant\"+\"1_after_hash\")) as \'p(1_after_vowel) \',(\"1_after_consonant\"/(\"1_after_vowel\"+\"1_after_consonant\"+\"1_after_hash\")) as \'p(1_after_consonant) \',(\"1_after_hash\"/(\"1_after_vowel\"+\"1_after_consonant\"+\"1_after_hash\")) as \'p(1_after_hash) \',(\"2_after_vowel\"/(\"2_after_vowel\"+\"2_after_consonant\"+\"2_after_hash\")) as \'p(2_after_vowel) \',(\"2_after_consonant\"/(\"2_after_vowel\"+\"2_after_consonant\"+\"2_after_hash\")) as \'p(2_after_consonant) \',(\"2_after_hash\"/(\"2_after_vowel\"+\"2_after_consonant\"+\"2_after_hash\")) as \'p(2_after_hash) \',(\"3_after_vowel\"/(\"3_after_vowel\"+\"3_after_consonant\"+\"3_after_hash\")) as \'p(3_after_vowel) \',(\"3_after_consonant\"/(\"3_after_vowel\"+\"3_after_consonant\"+\"3_after_hash\")) as \'p(3_after_consonant) \',(\"3_after_hash\"/(\"3_after_vowel\"+\"3_after_consonant\"+\"3_after_hash\")) as \'p(3_after_hash) \' from result_no_hash'
        cur.execute(prob_stmt)
        row = cur.fetchone()
        while row:
            getEntropy(str(row[0]).encode('ascii', 'ignore'),str(row[1]).encode('ascii', 'ignore'),row[2:])
            #getEntropy(row)
            row = cur.fetchone()
    except Exception as e:
        print e
    return
def getEntropy(arpabet, character, probs):
    eList = ["1_before","2_before","3_before","1_after","2_after","3_after"]
    j=0
    #print arpabet, character
    temp_line = ''
    for i in range(0,len(eList)):
        #temp_line = temp_line.join(getAccuEnt(probs[j:j+3]))
        accu_ent = getAccuEnt(probs[j:j+3])
        print accu_ent
        temp_line += str(accu_ent)+","
        #print eList[i],getAccuEnt(probs[j:j+3])
        j+=3
    #print arpabet,"->",character,"\n",probs[0:3],type(probs[0:4])
    hash_str = str(arpabet)+","+str(character)+","+temp_line.strip(',')
    print hash_str
    with open("Entropy_list.csv","a") as f:
        f.write(hash_str+"\n")
    return
def getAccuEnt(probList):
    E = float(0)
##    print sum(probList)
##    print probList
    try:
        for x in probList:
            if x == 0:
                #print"found 0"
                raise Exception("got a zero")
            E  += x*log(x,2)
        E = -(E)
    except Exception as e:
        #print "none discovered"
        E = "NONE"
    finally:
        return E
def wrappedRunner():
    try:
        #entropyTester()
        generateEntropies()
    except Exception as e:
        print e
########################

wrappedRunner()

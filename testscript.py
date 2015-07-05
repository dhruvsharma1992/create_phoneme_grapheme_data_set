import pickle
import sys
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
def wrappedRunner():
	try:
		entropyTester()
	except Exception as e:
		print e
########################

wrappedRunner()

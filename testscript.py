import pickle
from sqliteCRUD import *
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
    freq_list = crud_obj.getFrequencies()
    #print freq_list
    addProbs(freq_list)
    print '_'*50
    print freq_list
    parameterAnalysis(crud_obj)
    return
def parameterAnalysis(crud_obj):
    crud_obj.getParameterMapping()
    return
entropyTester()

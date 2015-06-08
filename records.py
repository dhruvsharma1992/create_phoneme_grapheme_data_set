#saransh
from sqliteCRUD import *
from dictionary import *
import pickle
def cleanWord(word):
	try:
		return word[0:word.index('(')]
	except Exception as e:
		return word
def checkCompatibility(wrd,arp):
    #if wrd[0] == arp[0]:
    #    return True
    #else:
        psbl_match = getValueSet(arp)
        if wrd.lower() in psbl_match:
            return True
	    return False
def indexInRange(i, lwrd):
    if i in range(0,len(lwrd)):
        return True
    return False
def checkOneToOneMapping(word,arpabets):
        wrd_mv = 0
        arp_mv = 0
	if True or len(word) == len(arpabets):
		arp_map = []
		j=0
# found possibilty of a simple mapping but will check if multiple map cases exist
		for i in range(len(arpabets)):
						#print arp_map
						if  indexInRange(i+j-arp_mv+wrd_mv+1,word) and checkCompatibility(word[i-arp_mv+j+wrd_mv],arpabets[i]):
							arp_map.append([word[i-arp_mv+j+wrd_mv],arpabets[i]])
						elif  indexInRange(i-arp_mv+j+wrd_mv+2,word) and checkCompatibility(word[i-arp_mv+j+wrd_mv:i-arp_mv+j+wrd_mv+2],arpabets[i]):
							arp_map.append([word[i-arp_mv+j+wrd_mv:i-arp_mv+j+wrd_mv+2],arpabets[i]])
							j=j+1
						elif  indexInRange(i-arp_mv+j+wrd_mv+3,word) and checkCompatibility(word[i-arp_mv+j+wrd_mv:i+j+wrd_mv+3],arpabets[i]):	
							arp_map.append([word[i-arp_mv+j+wrd_mv:i-arp_mv+j+wrd_mv+3],arpabets[i]])
							j=j+2
						elif  indexInRange(i-arp_mv+j+wrd_mv+4,word) and checkCompatibility(word[i-arp_mv+j+wrd_mv:j+i+wrd_mv+3+1],arpabets[i]):
							arp_map.append([word[i-arp_mv+j+wrd_mv:i-arp_mv+j+wrd_mv+3+1],arpabets[i]])
							j=j+3 
						
						else :
						    arp_map.append(['#',arpabets[i]])
						    arp_mv+=1
                    #else:
                        #arp_map.append([word[i+j+wrd_mv:],arpabets[i+arp_mv:]])
                        #print i+j,word
		return True,arp_map
	return False,list()
def toFile(arp_map):
    with open('testSet','ab') as dump_file:
	pickle.dump(arp_map,dump_file)
	return
def fromFile():
    with open('testSet','rb') as dump_file:
        print '________________________Object Dump Received________________________'
        try:
            arp_map_recv = pickle.load(dump_file)
            while arp_map_recv:
                print arp_map_recv
                arp_map_recv = pickle.load(dump_file)
        except Exception as e:
            print e
        finally:
            return
def getCRUDObject():
    TABLE_NAME = 'training_table'
    crud_obj = SqliteCRUD('training.db', TABLE_NAME)
    crud_obj.initiateTable(str("CREATE TABLE "+TABLE_NAME+" ('arpabet' TEXT,'character' TEXT,'arp_type' TEXT,'1_before_arp' TEXT,'2_before_arp' TEXT,'1_after_arp' TEXT,'2_after_arp' TEXT,'1_before_chr' TEXT,'2_before_chr' TEXT,'1_after_chr' TEXT,'2_after_chr' TEXT);"))
    return crud_obj
def pushToDB(toDB, crud_obj):
    try:
        crud_obj.insertIntoTable(toDB)
        #crud_obj.printTable()
        return True
    except Exception as e:
        print 'failed to insert into DB, exiting...'
        print e
        return False

def iterateAndPushToDB(arp_map,crud_obj):
    '''('arpabet','character','arp_type'
        ,'1_before_arp','2_before_arp','1_after_arp'
        ,'2_after_arp','1_before_chr','2_before_chr'
        ,'1_after_chr','2_after_chr');
    '''
    for i in range(len(arp_map)):
        arpabet = str(arp_map[i][1])
        character = str(arp_map[i][0])
        if indexInRange(i-1,arp_map):
            one_before_arp = str(arp_map[i-1][1])
            one_before_chr = str(arp_map[i-1][0])
        else:
            one_before_arp = '#'
            one_before_chr = '#'

        if indexInRange(i-2,arp_map):
            two_before_arp = str(arp_map[i-2][1])
            two_before_chr = str(arp_map[i-2][0])
        else:
            two_before_arp = '#'
            two_before_chr = '#'

        if indexInRange(i+1,arp_map):
            one_after_arp = str(arp_map[i+1][1])
            one_after_chr = str(arp_map[i+1][0])
        else:
            one_after_arp = '#'
            one_after_chr = '#'

        if indexInRange(i+2,arp_map):
            two_after_arp = str(arp_map[i+2][1])
            two_after_chr = str(arp_map[i+2][0])
        else:
            two_after_arp = '#'
            two_after_chr = '#'

        arp_type = str(getCategory(arp_map[i][1]))
        toDB_list = []
        toDB_list.append(arpabet)
        toDB_list.append(character)
        toDB_list.append(arp_type)
        toDB_list.append(one_before_arp)
        toDB_list.append(two_before_arp)
        toDB_list.append(one_after_arp)
        toDB_list.append(two_after_arp)
        toDB_list.append(one_before_chr)
        toDB_list.append(two_before_chr)
        toDB_list.append(one_after_chr)
        toDB_list.append(two_after_chr)
        #print 'arp_map is'
        #print '||',arp_map,'||'
        #print 'inserting into db'
        #print '{{',toDB_list,'}}'
        if not pushToDB(toDB_list,crud_obj):
            return False
    return True

def generateRecords(old_word, arpabets, crud_obj):
    #code
    word = cleanWord(old_word)
    arp_map = []
    check_flag,arp_map = checkOneToOneMapping(word,arpabets)
    if check_flag:
		#toFile(arp_map)
        #print '||',arp_map,'||'
        if iterateAndPushToDB(arp_map,crud_obj):
            print 'success'
        else:
            print 'failed'
    #print word,len(word),arp_map            
    #for arpabet in arpabets:
    #    print "|",arpabet,getCategory(arpabet),getValueSet(arpabet),"|\n"
    return

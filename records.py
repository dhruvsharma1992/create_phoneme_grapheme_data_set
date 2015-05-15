#saransh
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
    if i  <= len(lwrd):
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
def generateRecords(old_word,arpabets):
    #code
    word = cleanWord(old_word)
    arp_map = []
    check_flag,arp_map = checkOneToOneMapping(word,arpabets)
    if check_flag:
		toFile(arp_map)
    print word,len(word),arp_map            
    #for arpabet in arpabets:
    #    print "|",arpabet,getCategory(arpabet),getValueSet(arpabet),"|\n"
    return

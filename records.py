#saransh
from dictionary import *
import pickle
def cleanWord(word):
	try:
		return word[0:word.index('(')]
	except Exception as e:
		return word
def checkCompatibility(wrd,arp):
    if wrd[0] == arp[0]:
        return True
    else:
        psbl_match = getValueSet(arp)
        if wrd in psbl_match:
            return True
    return False
def indexInRange(i,amv,wmv,larp,lwrd):
    if larp <= i+amv:
        return False
    if lwrd <= i+wmv:
        return False
    return True
def checkOneToOneMapping(word,arpabets):
        wrd_mv = 0
        arp_mv = 0
	if len(word) == len(arpabets):
		arp_map = []
# found possibilty of a simple mapping but will check if multiple map cases exist
		for i in range(len(word)):
                    if indexInRange(i,arp_mv,wrd_mv,len(arpabets),len(word)):
                        if checkCompatibility(word[i+wrd_mv],arpabets[i+arp_mv]):
                            arp_map.append([word[i+wrd_mv],arpabets[i+arp_mv]])
                        else:
                            arp_map.append(['#',arpabets[i+arp_mv]])
                            arp_mv+=1
                    else:
                        arp_map.append([word[i+wrd_mv:],arpabets[i+arp_mv:]])
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
    #for arpabet in arpabets:
    #    print "|",arpabet,getCategory(arpabet),getValueSet(arpabet),"|\n"
    return

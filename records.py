#saransh
from dictionary import *
def generateRecords(word,arpabets):
    #code
    for arpabet in arpabets:
        print arpabet,getCategory(arpabet),getValueSet(arpabet)
    return
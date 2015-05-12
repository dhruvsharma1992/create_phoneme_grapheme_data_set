category = { 'vowel':['ah'],\
             'consonant':['k']}
arpabetDict = {'k':['q','ch','c','k','ck']\
    }
def getCategory(arpabet):
    if arpabet in category['vowel']:
        return 'vowel'
    elif arpabet in category['consonant']:
        return 'consonant'

def getValueSet(arpabet):
    return arpabetDict[arpabet]
category = { 'vowel':['ah'],\
             'consonant':['k']}
arpabetDict = {'k':['q','ch','c','k','ck']\
    }
def getCategory(arpabet):
    if arpabet.lower() in category['vowel'] or arpabet.upper() in category['vowel']:
        return 'vowel'
    elif arpabet.lower() in category['consonant'] or arpabet.upper() in category['consonant']:
        return 'consonant'
    else:
        return 'to be added'

def getValueSet(arpabet):
    if arpabet.lower() in arpabetDict:
        return arpabetDict[arpabet.lower()]
    elif arpabet.upper() in arpabetDict :
        return arpabetDict[arpabet.upper()]
    else:
        return 'to be added'
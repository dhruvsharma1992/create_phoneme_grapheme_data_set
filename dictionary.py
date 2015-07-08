category = { 'vowel':['ah','ae','eh','ih','iy','aw','ao','uw','y', 'aa', \
                'ay', 'eh', 'er', 'ey', 'ih', 'ow','uh'],\
             'consonant':['k', 'b', 'd', 'f', 'g', 'jh', 'l', 'm', 'n', \
                'p', 'r' ,'s', 't', 'v', 'w', 'z','ch','dh','hh','zh', 'oy',  'ng','sh','th']}

arpabetDict =   {
                 'aa': ['o', 'a', 'au'], 'iy': ['i', 'e', 'y', 'ea', 'ee', 'ie'], 'ch': ['ch'], 'ae': ['a', 'e', 'ay'], 'eh': ['e', 'ae', 'a'], 'ah': ['e', 'a', 'u', 'i', 'o', 'ou', 'io'], 'ao': ['o', 'au'], 'ih': ['e', 'i', 'y'], 'ey': ['a', 'ai', 'ay', 'e', 'ei'], 'aw': ['ou', 'ow'], 'ay': ['i', 'y'], 'zh': [], 'er': ['er', 'our', 'ur', 'or'], 'ng': ['ng'], 'sh': ['tio', 'sh', 's', 'ch', 'ss'], 'th': ['th'], 'uh': ['o', 'u', 'ou', 'oul'], 'w': ['u', 'w'], 'dh': ['th'], 'y': ['i', 'y'], 'hh': ['h'], 'jh': ['j', 'g'], 'b': ['b', 'be'], 'd': ['d', 'de'], 'g': ['g', 'ge'], 'f': ['ph', 'f'], 'k': ['c', 'q', 'ck', 'k', 'ch'], 'm': ['m', 'me', 'mm'], 'l': ['l', 'le', 'll'], 'n': ['n', 'nn', 'ne'], 'p': ['p', 'pe'], 's': ['ss', 'c', 's', 'ce', 'se'], 'r': ['r', 're'], 't': ['t', 'te', 'tt'], 'oy': ['oy'], 'v': ['v', 've'], 'ow': ['o', 'ow'], 'z': ['s', 'z'], 'uw': ['u', 'ew', 'ou']}

def getCategory(arpabet):
    if arpabet.lower() in category['vowel'] or arpabet.upper() in category['vowel']:
        return 'vowel'
    elif arpabet.lower() in category['consonant'] or arpabet.upper() in category['consonant']:
        return 'consonant'
    else:
        #print 'this character to be added :', arpabet
        #print category['consonant']
        return '#'

def getPos(one_before_arp,two_before_arp,three_before_arp, one_after_arp,two_after_arp,three_after_arp):
    if (one_before_arp == '#' or two_before_arp == '#' or three_before_arp == '#') and  (not one_after_arp == '#') and (not two_after_arp=='#') and (not three_after_arp=='#'):
        return '0'
    elif  (one_after_arp=='#' or two_after_arp == '#' or three_after_arp=='#') and (not one_before_arp == '#') and (not two_before_arp=='#') and (not three_before_arp=='#'):
        return '2'
    else:
        return '1'
    
def getValueSet(arpabet):
    if arpabet.lower() in arpabetDict:
        return arpabetDict[arpabet.lower()]
    elif arpabet.upper() in arpabetDict :
        return arpabetDict[arpabet.upper()]
    else:
        return list() 

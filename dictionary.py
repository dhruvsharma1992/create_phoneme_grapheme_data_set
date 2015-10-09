category = { 'vowel':['ah','ae','eh','ih','iy','aw','ao','uw','y', 'aa', \
                'ay', 'eh', 'er', 'ey','oy',    'ih', 'ow','uh'],\
             'consonant':['k', 'b', 'd', 'f', 'g', 'jh', 'l', 'm', 'n', \
                'p', 'r' ,'s', 't', 'v', 'w', 'z','ch','dh','hh','zh',   'ng','sh','th']}


arpabetDict =   {
                  'aa': ['o', 'a', 'au'],\
                  'iy': ['i', 'e', 'y', 'ea', 'ee', 'ie'],\
                  'ch': ['ch'],  \
                  'ae': ['a', 'e', 'ay'], \
                   'eh': ['e', 'ae', 'a','y','ea'], \
                   'ah': ['e', 'a' , 'u', 'i', 'o', 'ou', 'io','ai','eu' ], \
                   'ao': ['o', 'au'], \
                   'ih': ['e', 'i', 'y'], \
                   'ey': ['a','e', 'ai', 'ay','aie','aye', 'ei','eie','ea'], \
                   'aw': ['ou', 'ow'], \
                   'ay': ['i', 'y','ie'], \
                   'zh': [], \
                   'er': ['er', 'our', 'ur', 'or'], \
                   'ng': ['ng'], \
                   'sh': ['tio', 'sh', 's','c', 'ch', 'ss'], \
                   'th': ['th'], \
                   'uh': ['o', 'u', 'ou', 'oul','oo'], \
                   'w': ['u', 'w'],  \
                   'dh': ['th'], \
                   'y': ['i','e', 'y'], \
                   'hh': ['h'], \
                   'jh': ['j', 'g','ge','dge'], \
                   'b': ['b', 'bb',  'be'], \
                   'd': ['d','ed', 'de'], \
                   'g': ['g', 'ge'], \
                   'f': ['ph', 'f','ff'], \
                   'k': ['c', 'q', 'ck', 'k', 'ch','ke','que','cc'], \
                   'm': ['m', 'me', 'mm'], \
                   'l': ['l', 'le', 'll'], \
                   'n': ['n', 'nn', 'ne','gn'], \
                   'p': ['p', 'pe'], \
                   's': ['c', 's','ss', 'sc', 'ce', 'se'], \
                   'r': ['r', 're'], \
                   't': ['t', 'te', 'tt','tte','ed'], \
                   'oy': ['oy'], \
                   'v': ['v', 've'], \
                   'ow': ['o', 'ow','oa'], \
                   'z': ['s', 'z','ze','se','ss'], \
                   'uw': ['u','w', 'ew', 'ou','ue']}

arpabetClass =   {
                  'aa': ['A','A'],\
                  'iy': ['I','I'],\
                  'ch': ['CHJ','CHJ'],  \
                  'ae': ['E','E'], \
                   'eh': ['E','E'], \
                   'ah': ['A','A'], \
                   'ao': ['O','O'], \
                   'ih': ['I','I'], \
                   'ey': ['E','E'] , \
                   'aw': ['O','O'], \
                   'ay': ['A','E'], \
                   'zh': ['S','S'], \
                   'er': ['A','R'], \
                   'ng': ['N','G'], \
                   'sh': ['S','S'], \
                   'th': ['TH' ,'TH'], \
                   'uh': ['U','U'  ], \
                   'w': ['V','V'],  \
                   'dh': ['TH','TH'], \
                   'y': ['I','I'], \
                   'hh': ['H','H'], \
                   'jh': ['CHJ','CHJ'], \
                   'b': ['B','B'], \
                   'd': ['TD','TD'], \
                   'g': ['G','G'], \
                   'f': ['P','P'], \
                   'k': ['K','K'], \
                   'm': ['MN','MN'], \
                   'l': ['L','L'], \
                   'n': ['MN','MN'], \
                   'p': ['P','P'], \
                   's': ['S','S'], \
                   'r': ['R','R'], \
                   't': ['TD','TD'], \
                   'oy': ['O','Y'], \
                   'v': ['V','V'], \
                   'ow': ['O','O'], \
                   'z': ['S', 'S'], \
                   'uw': ['U','U'],\
                   '#':['#','#']}

ipa = {'a': '',
'c': '',
'e': '',
'f': '',
'g': '',
'h': '',
'i': '',
'j': '',
'k': '',
'l': '',
'm': '',
'n': '',
'o': '',
'p': '',
'q': '',
'r': '',
's': '',
't': '',
'u': '',
'v': '',
'w': '',
'x': '',
'y': '',
'z': '',
'\xe1': '',
'\xe9': '',
'\xed': '',
'\xf0': '',
'\xf1': '',
'\xf3': '',
'\xfa': '',
'\xfc': '',
'\u03b2': '',
'\ufeff': ''}
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

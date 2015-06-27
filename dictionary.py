category = { 'vowel':['ah','ae','eh','ih','iy','aw','ao','uw','y', 'aa', \
                'ay', 'eh', 'er', 'ey', 'ih', 'ow'],\
             'consonant':['k', 'b', 'd', 'f', 'g', 'jh', 'l', 'm', 'n', \
                'p', 'r' ,'s', 't', 'v', 'w', 'z']}
arpabetDict =   {'ao':['o','au','ough'],\
                 'w':['w','v','u'],\
                'aa':['a','o','au'],\
                'iy':['i','e','ee','ea','y'],\
                'uw':['ou','ew','u'],\
                'eh':['e','ae'],\
                'ih':['i','e','y'],\
                'uh':['oul','u','ou','o'],\
                'ah':['u','o','a','e','i','ou'],\
                'ae':['e','a','ay'],\
                'ey':['ai','ei', 'ay','a','e'],\
                'ay':['y','i'],\
                'ow':['o','oa'],\
                'aw':['ow','ou'],\
                'oy':['oy'],\
                'er':['er','our'],\
                'ow':['ow','o'], \
                'p':['p','pe'],\
                'b':['b','be'],\
                'k':['c','k','ch','q','ck'],\
                'l':['l','le','ll'],\
                'd':['d','de'],\
                't':['t','tt','te'],\
                'ch':['ch'],\
                'g':['g','ge'],\
                'jh':['j','g'],\
                'v':['v','w','wh'],\
                'f':['f','ph','ough'],\
                'dh':['dh','th'],\
                'z':['z','s'],\
                'hh':['h'],\
                's':['s','c','ce','se','ss'],\
                'sh':['sh','tio','s','ch'],\
                'th':['th'],\
                'm':['m','me','mm'],\
                'n':['n','ne','nn'],\
                'r':['r','re'],\
                'y':['y','i']
               }


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

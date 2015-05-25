category = { 'vowel':['ah','ae','eh','ih','iy','aw','ao','uw','y' ],\
             'consonant':['k']}
arpabetDict =   {'ao':['o'],\
                 'w':['w','v','u'],\
                'aa':['a','o'],\
                'iy':['e','ee','ea','y'],\
                'uw':['ou','ew','u'],\
                'eh':['e'],\
                'ih':['i'],\
                'uh':['oul','u','ou','o'],\
                'ah':['u','o','a','e','i'],\
                'ae':['e','a','ay'],\
                'ey':['ai','ei', 'ay','a','e'],\
                'ay':['y','i'],\
                'ow':['o','oa'],\
                'aw':['ow','ou'],\
                'oy':['oy'],\
                'er':['er','our'],\
                'ao':['o','ough'],\
                'ow':['ow','o'], \
                'p':['p','pe'],\
                'b':['b','be'],\
                'k':['c','k','ch','q','ck'],\
                'l':['l','le'],\
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
                's':['s','c','ce','se'],\
                'sh':['sh','tio','s'],\
                'th':['th'],\
                'm':['m','me','mm'],\
                'n':['n','ne','nn'],\
                'r':['r','re'],\
                'y':['y']
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
        return list() 

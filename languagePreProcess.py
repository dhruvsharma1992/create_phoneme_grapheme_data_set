from os.path import isfile, join
from os import listdir
import codecs 
dictionary = {}
ipa = {'a': ['AA','Odd'],
 'au': ['AO','AUto'],
 'a\xc9\xaa':  ['AY','fIght'],
 'a\xca\x8a': [ 'AW','nOW'],
 'a\xcb\x90': ['AA HH ','lAst'],
 'b': ['b','Bat'],
 'c': ['CH','CHair'],
 'd': ['D','Dog'],
 'd\xcd\xa1\xca\x92': ['JH','Gin Jeans'],
 'e': ['EY', 'AIlment'],
 'ei': ['EY IY','  dEI'],
 'eu': ['Y UW','EEW'],
 'e\xc9\xaa': ['EY','plAY'],
 'e\xcb\x90': ['EH','EHd'],
 'f': ['F','Foo'],
 'h': ['HH','He'],
 'i\xcb\x90':['IY','sEEn'],
 'i': ['IY','easY'],
 'j': [ 'Y','  Yes'],
 'k': ['K','Key'],
 'k\xca\xb0': ['K',' Cry Cat '],
 'l': ['L','Love'],
 'm': ['M','Mutation'],
 'n': ['N','Na'],
 'o': ['OW','OAt'],
 'o\xc9\xaa': ['OY','tOY'],
 'o\xca\x8a': ['AW','cOW'],
 'o\xcb\x90': ['UH AH', 'bOOHt'],
 'p': ['P','Pur'],
 'p\xca\xb0': ['IH','Pin  '],
 'q':  ['K Hh','Arabic sound'],
 'r':  ['R','Rat'],
 's': ['S','Sat'],
 't': ['T','Tat'],
 't\xca\xb0':  ['T','Top'],
 't\xcd\xa1\xca\x83': ['CH','CHai'],
 'u': ['UW','dO '],
 'u\xcb\x90':  ['UW','OOH'],#tch chair Cech',
 
 'v':  ['V','Victory'],
 'w': ['W' ,'We'],
 'x': ['K','loCH'],
 'y': ['UW','dUE '],
 'y\xcb\x90': ['UW', 'Uber'],
 'z': ['Z','Zoo'],
 '\xc3\xa3':  ['AH','AH nasal'],
 '\xc3\xa6': ['AE'     , 'cAt'],
 '\xc3\xa6\xcb\x90':  ['AE','cAt'],
 '\xc3\xa7':  ['Hh' ,'Hat'],
 '\xc3\xb0':  ['DH','THis'],
 '\xc3\xb5':  ['UW N','UW nasal'],
 '\xc3\xb8':  ['Y UH','pUre'],
 '\xc3\xb8\xcb\x90':  ['Y UH','EEAH'],
 '\xc4\xa9': ['IY IH N','sInto pronounced as seehnto'],
 '\xc5\x8b': ['NG','piNG'],
 '\xc5\x93':  ['AH',' hUn'],
 '\xc5\x93\xcc\x83': ['AH N',' AH nasal'],
 '\xc5\xa9':  ['Y UW N','accU Nasal'],
 '\xc9\x90':  ['AH','Acquires'],
 '\xc9\x90\xcc\x83': ['AH N','shUnt Nasal'],
 '\xc9\x91':  ['AA','Odd'],
 '\xc9\x91\xcb\x90':  ['AA','Arm'],
 '\xc9\x91\xcc\x83':  ['AA N','AA nasal'],
 '\xc9\x92':  ['AO','nOt'],
 '\xc9\x94':   ['AO', 'nOt'],
 '\xc9\x94\xc9\xaa':  ['OY', 'cOIl'],
 '\xc9\x94\xca\x8a':  ['OW', 'bOWler'],
 '\xc9\x94\xcb\x90':  ['AO','sAW'],
 '\xc9\x94\xcc\x83': ['AO N','AO Nasal' ],
 '\xc9\x95':  ['SH','Shade'],
 '\xc9\x99':  ['AH','About'],
 '\xc9\x99\xca\x8a':  ['OW','gO'],
 '\xc9\x9a':     [ 'ER','winnER'],
 '\xc9\x9b':  ['EH','bEd'],
 '\xc9\x9bi': ['EY' ,'survEY'],
 '\xc9\x9bu': ['EY UW',' pEU'],
 '\xc9\x9b\xc9\x99': ['AE ER','thERE British Eng '],
 '\xc9\x9b\xcb\x90':  ['EY HH','mEH'],
 '\xc9\x9b\xcc\x83':   ['EY N','EY nasal'],
 '\xc9\x9c':  ['AH','bUd'],
 '\xc9\x9c\xcb\x90': ['AH','bIRd British Eng. '],
 '\xc9\x9d': ['ER',' bIRd American Eng.'],
 '\xc9\x9f':  ['JH','Jail'],
 '\xc9\xa1':   ['G','Go'],
 'g':['G','Go'],
 '\xc9\xa3': ['G',' GHost'],
 '\xc9\xa4': ['AO','hOrn'],
 '\xc9\xa5': ['HH UW','HUit'],
 '\xc9\xa6': ['HH','Hat'],
 '\xc9\xa7': ['CH','Chair'],
 '\xc9\xa8': ['IH','sIt'],
 '\xc9\xaa': ['IH','cIty '],
 '\xc9\xaa\xc9\x99': ['IH R','clEAR'],
 '\xc9\xab': ['L','piLl'],
 '\xc9\xaf': ['Y UW','nEW'],
 '\xc9\xaf\xcb\x90': ['Y UW','nEW'],
 '\xc9\xb1': ['M','Material'],
 '\xc9\xb2':  ['N Y', 'caNYon'],
 '\xc9\xb4': ['N', 'Nat'],
 '\xc9\xb5': ['OY','tOY'],
 '\xc9\xb8':   ['F UH','fu japanese'],
 '\xc9\xba': ['R IH','rih japanese'],
 '\xc9\xbb': ['R','Run'],
 '\xc9\xbe': ['T','beTTer'],
 '\xca\x80':  ['R','aiR'],
 '\xca\x81': ['R','aiR'],
 '\xca\x82': ['SH','SHade'],
 '\xca\x83': ['Sh','Sure'],
 '\xca\x89': ['UW', 'parachUte'],
 '\xca\x89\xcb\x90': ['UH','fUll'],
 '\xca\x8a': ['UH','pUt' ],
 '\xca\x8b': ['W','Wang'],
 '\xca\x8c': ['AH','rUn'],
 '\xca\x8cu': ['AW','cOW'],
 '\xca\x8c\xcb\x90': ['AH','sUn'],
 '\xca\x8e': ['IY AH','vILLa spanish'],
 '\xca\x8f': ['UW','glUE'],
 '\xca\x90': ['ZH','seiZure'],
 '\xca\x91': ['ZH JH','SZHimat '],
 '\xca\x92': ['ZH','seiZure'],
 '\xca\x9d': ['IY Y','EEY'],
 '\xce\xb2': ['V','V generally after AA'],
 '\xce\xb8': ['TH','THing'],
 '\xe1\xba\xbd': ['EY N', 'EY nasal'],
 '\xef\xbb\xbfi': ['IY',' EasY'],
  '\xef\xbb\xbf': [' ',' '],
}

def main():
    with codecs.open(join(join("dataset","languages"),"ipa.txt"),   encoding="UTF-8"   ) as fread:
        y,n=0,0
        nlist = []
        #print ipa.keys()
        for words in fread:
            word = words.strip()
            print word, ipa[word.encode('utf-8')]    [0]#, "(", ipa[word.encode('utf-8')] [1],")",""
            'print word'
            #print word
            '''length = 0
            while length < len(word):
                
                rep = word[length:length+2] .encode('utf-8')
                if rep in ipa.keys():
                    #print rep, "1",
                    y+=1
                    length +=1
                    print rep,ipa[rep][0]
                else:
                    rep = word[length] .encode('utf-8')
                    
                    if rep in ipa.keys():
                        
                        print rep,ipa[rep][0]
                        #print rep, "1",
                        y+=1
                        
                        
                    else:
                        rep = word[length] .encode('utf-8') 
                        #print  rep , "0",
                        n+=1
                        #if not rep in nlist:
                         #   print word,rep
                            #print  rep,repr(rep),word.encode('UTF-8')
                length += 1'''
            #print    
    
    #print y,n,nlist

    i,l=0,0
    '''for key in ipa.keys():
        print key,repr(key)
        try:
            if  len(ipa[key][1]) == 0:
                i+=1
            else:
                l+=1 
        except:
            print 'ERROR'
    print l,i'''
#main()

#for key in ipa.keys():
    #print key,",", ipa[key][0]
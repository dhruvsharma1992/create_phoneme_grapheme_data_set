from records import *

fw = file("notinserted.txt","a") #OP
fwmap = file("notinsertedmap.txt",'a')
from os import listdir
from os.path import isfile, join
onlyfiles = [ f for f in listdir("dataset/logios") if isfile(join( "dataset/logios" ,f)) ]
#open('testSet','w').close()
crud_obj = getCRUDObject()
onlyfiles=['wordsLogios.txt']
for INPUT_FILE in onlyfiles: 
    with open(join( "dataset/logios" ,INPUT_FILE)) as fread:
        for line in fread:
            if len(line.split())>2:
                word=line.split()[0]
                arpabets = line.split()[1:]
               # print word,arpabets
                value = generateRecords(word, arpabets, crud_obj)
                
                print INPUT_FILE,word,value[0]
                if value[0]==False:
                    fw.write(line)
                    
                    fwmap.write(word+" "+ str(value[1])+"\n")

fw.close()
fwmap.close()

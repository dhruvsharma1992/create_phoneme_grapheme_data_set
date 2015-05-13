from records import *

INPUT_FILE = "wordsLogios.txt" #OP
open('testSet','w').close()
with open(INPUT_FILE) as fread:
    for line in fread:
        word=line.split()[0]
        arpabets = line.split()[1:]
       # print word,arpabets
        generateRecords(word,arpabets)

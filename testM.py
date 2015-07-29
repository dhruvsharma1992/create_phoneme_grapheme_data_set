import random
from dictionary import arpabetDict
from dictionary import arpabetClass
from dictionary import getCategory
from getProbability import SqliteCRUD

TABLE_NAME = 'training_table'
DB_NAME = 'training.db'
crudObj = SqliteCRUD(DB_NAME, TABLE_NAME)
def cursorToDictionary(row, cases):
    input = {}
    for i in range(len(category)):
        if 'after_arp' in category[i]  and not 'type' in category[i]:
            if cases == 0:
                input[category[i]]=arpabetClass[row[i].lower()][0]
            else:
                input[category[i]]= row[i]
        elif 'before_arp' in category[i] and not 'type' in category[i]:
            if cases == 0:
                input[category[i]]=arpabetClass[row[i].lower ()][1]
            else:
                input[category[i]]= row[i] 
        else:
            input[category[i]]= row[i] 
    return input

for arpabet in arpabetClass.keys( ):
    
    import csv,os
    cursor = crudObj.returnCursor().execute('select * from training_table where arpabet = '+ '"'+arpabet.upper()+'" ')#and position="2"'     )
    category = ["arpabet","character" ,"arp_type","1_before_arp","2_before_arp","3_before_arp","1_after_arp","2_after_arp","3_after_arp","1_before_chr","2_before_chr","3_before_chr","1_after_chr","2_after_chr","3_after_chr","1_before_arp_type","2_before_arp_type","3_before_arp_type","1_after_arp_type","2_after_arp_type","3_after_arp_type","position","word"            ]
    
    output=[]
    for row in cursor:    
        input = cursorToDictionary(row,0)  # 0-> Sanskrit 1-> Raw         
        output +=[input ]
    #output =  random.sample( output , (int)((len(output))*0.75))  to downsample 
    with open(os.path.join(os.path.dirname(__file__), arpabet+'.csv'), 'wb') as csvfile:        
        fieldnames = ["character"]
        fieldnames +=["2_before_arp"]
        fieldnames +=[ "2_before_arp"]
        fieldnames +=[ "3_before_arp"]
        fieldnames +=["1_after_arp"] 
        fieldnames +=[ "2_after_arp"] 
        fieldnames +=[ "3_after_arp"]
        fieldnames +=[ 'position']
        ''' add '#' infront of fields to ignore'''
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() 
        for o in output:   
            o = { k: o[k]  for k in fieldnames  }          
    #print len(input)
            writer.writerow(o) 
#rahul
#author saransh
import string
import random
import traceback
import sys
import sqlite3 as lite
TABLE_NAME = 'training_table'
DB_NAME = 'training.db'

class SqliteCRUD:
    def __init__(self, db_name, table_name):
        try:
            self.db_name = db_name
            self.table_name = table_name
            self.connection = lite.connect(str(self.db_name))
            self.cursor = self.connection.cursor()
        except Exception as e:
            print 'couldn\'t create DB, Exiting'
            print e
            print traceback.format_exc()
            sys.exit(0)

    def initiateTable(self, table_descriptor):
        try:
            if self.__checkTable():
                return

            self.cursor.execute(str(table_descriptor))
            self.connection.commit()
        except Exception as e:
            print 'couldn\'t create table, exiting'
            print e
            print traceback.format_exc()
            sys.exit(0)

    def insertIntoTable(self, insert_list):
        if True or self.__checkTable():
            try:
                if True or self.__redundancyCheck(insert_list):
                    insert_query = self.__convertIntoQuery(insert_list)
                    self.cursor.execute(insert_query)
                    self.connection.commit()
            except Exception as e:
                print 'couldn\'t execute query. exiting'
                print traceback.format_exc()
                print e
                sys.exit(0)
        else:
            print 'table doesn\'t exist'
            print 'insert query was not executed'
            return

    def __redundancyCheck(self, insert_list):
        table_param = ['"arpabet"', '"character"', '"arp_type"'\
        , '"1_before_arp"', '"2_before_arp"', '"1_after_arp"'\
        ,'"2_after_arp"', '"1_before_chr"'\
        ,'"2_before_chr"','"1_after_chr"','"2_after_chr"']
        #proud of the folowing statement B-)
        map_list = ' and '.join(str(ele) for ele in [str(x[0]+' = \''+x[1]+'\'') for x in zip(table_param,insert_list)])
        #print map_list
        try:
            self.cursor.execute("SELECT COUNT(*) FROM "+ str(self.table_name) +" WHERE "+map_list)
            rows = self.cursor.fetchone()
            if int(str(rows)[1:-2]) > 0:
                print "0",
                return False
            else:
                print "1",
                return True
        except Exception as e:
                print 'couldn\'t complete redundancy check, exiting ...'
                print e
                sys.exit(0)
    def __checkTable(self):
        try:
            self.cursor.execute("SELECT * FROM "+str(self.table_name))
        except Exception as e:
            return False
        return True

    def __convertIntoQuery(self, insert_list):
        '''INSERT INTO table_name
        VALUES('arpabet','character','arp_type'
        ,'1_before_arp','2_before_arp','1_after_arp'
        ,'2_after_arp','1_before_chr','2_before_chr'
        ,'1_after_chr','2_after_chr');
        '''
        extrct_str = ','.join(str('\''+str(x)+'\'') for x in insert_list)
        pre_extrct_str = 'INSERT INTO '+str(self.table_name)+' VALUES('
        insert_query = pre_extrct_str+extrct_str+');'
        #print 'insert query generated is', insert_query
        return insert_query

    def printTable(self):
        self.cursor.execute('SELECT * FROM '+str(self.table_name))
        rows = self.cursor.fetchall()
        print '_______', self.table_name, '________'
        for row in rows:
            for ele in row:
                print str(ele),
            print'\n'
        print '__________________________________'
        return

    def purgeTable(self):
        return

        '''
        Main section
        '''
    def getFrequencies(self):
        try:
            self.cursor.execute('select arpabet,character,count(arpabet) from training_table group by arpabet,character')
            rows = self.cursor.fetchall()
            freq_list = []
            for row in rows:
               freq_list.append([str(x).encode('ascii','ignore') for x in row])
            return freq_list
        except Exception as e:
            print 'couldn\'t fetch frequencies'
            print e
            sys.exit(0)
    def getParameterMapping(self):
        param_map = dict()
        try:
            self.cursor.execute('select * from training_table order by arpabet,character;')
            row = self.cursor.fetchone()
            arg_dict = dict()
            while row:
                record = [str(rec).encode('ascii', 'ignore') for rec in row]
                print record
                self._checkAndInsertToMapping()
                row = self.cursor.fetchone()
        except Exception as e:
            print 'mapping query couldn\'t be executed, exiting ..'
            print e
    def getProbability(self,character,arpabet):
        category = ["arpabet","character" ,"arp_type","1_before_arp","2_before_arp","3_before_arp","1_after_arp","2_after_arp","3_after_arp","1_before_chr","2_before_chr","3_before_chr","1_after_chr","2_after_chr","3_after_chr","1_before_arp_type","2_before_arp_type","3_before_arp_type","1_after_arp_type","2_after_arp_type","3_after_arp_type","position","word"            ]
        cursor = self.cursor.execute('select * from training_table where arpabet ="'+ arpabet+'" and character="'+character+'"     ')
        one_before,total={},0
        for i in range(3,22):
            one_before[category[i]]={}
        for rows in cursor: 
            for i in range(3,22):
                if not rows[i] in one_before[category[i]]:   
                    one_before[category[i]][rows[i]] =1
                else:
                    one_before[category[i]][rows[i]]+=1 
        return one_before
    
    
    def getDistinct(self,arpabet):

        cursor = self.cursor.execute('select distinct character from training_table where arpabet="'+arpabet+'"')
        return [arp[0] for arp in cursor] 
            #print arp
    
    def getArpabetDistrib(self,arpabet):
        category = ["arpabet","character" ,"arp_type","1_before_arp","2_before_arp","3_before_arp","1_after_arp","2_after_arp","3_after_arp","1_before_chr","2_before_chr","3_before_chr","1_after_chr","2_after_chr","3_after_chr","1_before_arp_type","2_before_arp_type","3_before_arp_type","1_after_arp_type","2_after_arp_type","3_after_arp_type","position","word"            ]
        characters=self.getDistinct(arpabet)
        one_before,total,initMap={},{},{}
        for ch in characters:
            initMap[ch]=0 
            total[ch]=0
        for i in range(3,22):
            one_before[category[i]]={}
        for character in characters:
            cursor = self.cursor.execute('select * from training_table where arpabet ="'+ arpabet+'" and character="'+character+'"     ') 
            for rows in cursor: 
                total[character]+=1
                for i in range(3,22):
                    if not rows[i] in one_before[category[i]]:   
                        one_before[category[i]][rows[i]] =initMap.copy()
                        one_before[category[i]][rows[i]][character] = 1
                    else:
                        one_before[category[i]][rows[i]][character]+=1
        for cat in one_before:
            for arp in one_before[cat]:
                for ch in one_before[ cat][arp]:
                    #print one_before[cat][arp][ch],(float)(one_before[cat][arp][ch])/(float)(total[ch])
                    one_before[cat][arp][ch]= (float)(one_before[cat][arp][ch])/(float)(total[ch]) 
        one_before['total']=total
        #print total,initMap 
        return one_before
    

def main():
    crud_obj = SqliteCRUD(DB_NAME, TABLE_NAME)
    entropy={}
    from pprint import pprint
    import json 
    #pprint(crud_obj.getProbability("C","SH"))
    result=crud_obj.getArpabetDistrib("SH")
    print json.dumps(result) 
def freq_test():
   '''select arpabet,character,count(arpabet) from training_table group by arpabet,character''' 
   crud_obj = SqliteCRUD(DB_NAME, TABLE_NAME)
   crud_obj.printTable()
   freq_list = crud_obj.getFrequencies()
   print freq_list
main()
#freq_test()

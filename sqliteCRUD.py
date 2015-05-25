#rahul
#author saransh
import random
import traceback
import sys
import sqlite3 as lite


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
        if self.__checkTable():
            try:
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
        ,'1_after_chr','2_after_chr'
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


def main():
    TABLE_NAME = 'training_table'
    crud_obj = SqliteCRUD('training.db', TABLE_NAME)
    crud_obj.initiateTable(str("CREATE TABLE "+TABLE_NAME+" ('arpabet' TEXT,'character' TEXT,'arp_type' TEXT,'1_before_arp' TEXT,'2_before_arp' TEXT,'1_after_arp' TEXT,'2_after_arp' TEXT,'1_before_chr' TEXT,'2_before_chr' TEXT,'1_after_chr' TEXT,'2_after_chr' TEXT);"))
    crud_obj.printTable()

    to_be_inserted = []
    for x in range(11):
        to_be_inserted.append(random.choice(['A', 'AH', 'Q', 'QW', 'P', 'I', 'AH', 'LO', 'X']))
    crud_obj.insertIntoTable(to_be_inserted)
    crud_obj.printTable()
main()

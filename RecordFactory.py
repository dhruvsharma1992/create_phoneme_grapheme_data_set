def getArpabetType(arp):
	arpabet_vowel_list = ["AH","AE","EH","IH","IY","AW","AO","UW","Y","UW"]
	if arp in arpabet_vowel_list:
		return 'vowel'
	else:
		return 'consonant'
class RecordFactory:
	def __init__(self,file_name,word_delimit):
		self.file_name = file_name
		self.word_delimit = word_delimit
		self.arp_map = self.loadMapping()
		return
	def loadMapping(self):
		with open(self.file_name) as fbuf:
			record_buf = []
			arp_map = []
			for line in fbuf:
				lexeme = str(line.split()[0])
				if lexeme[0] == self.word_delimit:
					#print "found new word"
					#print len(record_buf)
					if len(record_buf) != 0:
						#print "record buf inserted into dict",record_buf
						
						arp_map.append(record_buf[:])
						#print arp_map
						#print record_buf,"||\n"
					del record_buf[:]	
					map_word = ""
					#print record_buf[:]
					#print lexeme
					#if lexeme.find("(") == -1:
					#	map_word = lexeme[1:]
					#else:
					#	map_word = lexeme[1:lexeme.find("(")]
					continue
				mapped_arpabet = line.split()[1]
				#print lexeme,mapped_arpabet
				record_buf.append([lexeme,mapped_arpabet])
			return arp_map
	def printMapping(self):
		print "______MAPPING LIST______"
		for mapping in self.arp_map:
			print mapping
			print '_'*50
	def getInsertQuery(self):
		for record in self.arp_map:
			#print record
			insert_query_dict = dict.fromkeys([
			'arpabet',
			'character',
			'arp_type',
			'1_before',
			'2_before',
			'1_after',
			'2_after',
			])
			for i,entry in enumerate(record):
				print "record : ",record
				print "i : ",i
				insert_query_dict['arpabet'] = str(entry[1])
				insert_query_dict['character'] = str(entry[0])
				insert_query_dict['arp_type'] = getArpabetType(str(entry[1]))
				insert_query_dict['1_before_arp'] = record[i-1][0] if (i-1 >= 0) else '*' 
				insert_query_dict['2_before_arp'] = record[i-2][0] if (i-2 >= 0) else '*' 
				insert_query_dict['1_after_arp'] = record[i+1][0] if (i+1 < len(record)) else '*' 
				insert_query_dict['2_after_arp'] = record[i+2][0] if (i+2 < len(record)) else '*' 
				insert_query_dict['1_before_char'] = record[i-1][1] if (i-1 >= 0) else '*' 
				insert_query_dict['2_before_char'] = record[i-2][1] if (i-2 >= 0) else '*' 
				insert_query_dict['1_after_char'] = record[i+1][1] if (i+1 < len(record)) else '*' 
				insert_query_dict['2_after_char'] = record[i+2][1] if (i+2 < len(record)) else '*' 
			for key,item in insert_query_dict.iteritems():
				print key,":",item
			print "_"*50
rcrd_obj = RecordFactory("map_ref.txt",">")
rcrd_obj.printMapping()
rcrd_obj.getInsertQuery()

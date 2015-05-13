import pickle
i=0
with open('testSet','rb') as dump_file:
    try:
        arp_map = pickle.load(dump_file)
        while arp_map:
            i+=1
            for x in arp_map:
                    print i,':',x
        #    print arp_map
            print '_'*60
            arp_map = pickle.load(dump_file)
    except Exception as e:
        print e
    finally :
        print 'file edit completed'

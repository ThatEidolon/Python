from hashlib import md5
import sys


def passcrack(pass_hash):
    for i in range(1001):#try 1-1000
        m = md5()
        m.update(str(i))
        test_hash = m.hexdigest()
        if (test_hash != pass_hash):
            print "Failed: %s\t%s" % (test_hash, pass_hash)
        else:
            print "Success: %d" % i
            return

m=md5()
m.update(str(sys.argv[1]))
passcrack(m.hexdigest())

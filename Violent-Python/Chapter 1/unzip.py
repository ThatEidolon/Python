import zipfile
from threading import Thread
import optparse
def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print '[+] Found password ' + password + '\n'
	except:
		return

def main():
	parser = optparse.OptionParser(usage = "usage: %prog " + "-f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest='zname', type='string', help='specify zip file')
	parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname
	zFile = zipfile.ZipFile(zname)
	passfile = open(dname)
	for line in passfile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()

if __name__ == '__main__':
	main()

		

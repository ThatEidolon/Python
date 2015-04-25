import crypt
def testPass(cryptPass):
	salt = cryptPass[0:11]
	print "[+] Salt: " + salt
	dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')  
		cryptword = crypt.crypt(word,salt)
		print "[+] Hash value: " + cryptword 
		if (cryptword == cryptPass) :
			print "[+] Found password: "+word+"\n"
			return
	print "[-] Password not found.\n"
	return

def main():
	passfile = open('shadow.txt')
	for line in passfile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Cracking password for: "+user
			testPass(cryptPass)

if __name__ == "__main__":
	main()


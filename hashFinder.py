import hashlib
import argparse		 # command line arguments
import sys

ALGO_LIST = {1:'sha512',2:'sha256',3:'md5',4:'sha1',
			5:'sha224',6:'sha384',7:'sha3_224',8:'sha3_256',
			9:'sha3_384',10:'sha3_512',11:'shake_128',
			12:'shake_256',13:'blake2b',14:'blake2s'}
ALGO_LIST_FUNC = {1:hashlib.sha512(),2:hashlib.sha256(),3:hashlib.md5(),4:hashlib.sha1(),
			5:hashlib.sha224(),6:hashlib.sha384(),7:hashlib.sha3_224(),8:hashlib.sha3_256(),
			9:hashlib.sha3_384(),10:hashlib.sha3_512(),11:hashlib.shake_128(),
			12:hashlib.shake_256(),13:hashlib.blake2b(),14:hashlib.blake2s()}
banner =''
hashAlgosAvailable = '''
[+] List of Hashing Algorithms\n
  1) sha512      2) sha256       3) md5
  4) sha1        5) sha224       6) sha384
  7) sha3_224    8) sha3_256     9) sha3_384
 10) sha3_512   11) shake_128   12) shake_256
 13) blake2b    14) blake2s
'''
def algoToNum(hashAlgo):
	rev = {ALGO_LIST[x]:x for x in ALGO_LIST}
	return rev.get(hashAlgo)

	
def calculateHashFunction(filePath, hashAlgo, hashAlgoNum, hashCheckValue):
	if(hashAlgoNum and int(hashAlgoNum) in range(1,15,1)):
		pass
	else:
		hashAlgoNum = algoToNum(hashAlgo)
		if(not hashAlgoNum):
			print('[x] Wrong Hashing Algorithm prvided!')
			exit(0)

	print("[+] Selected Algorithm: ",ALGO_LIST[hashAlgoNum])
	print('[+] File provided: ',filePath)
	fileHash = ALGO_LIST_FUNC.get(hashAlgoNum)
	f = open(filePath,"rb")
	for byte_block in iter(lambda: f.read(4096),b""):	# blocks of 4K 
		fileHash.update(byte_block)
	f.close()
	finalHashValue = fileHash.hexdigest()
	print('[+] Hash value of file: \n'+str(finalHashValue))

	if(hashCheckValue):
		print('[+] Hash value provided to check: \n'+str(hashCheckValue))
		if( str(finalHashValue) == str(hashCheckValue) ):
			print('[+] Both hashes matched ! ')
		else:
			print('[X] Both hashes NOT matched ! ')
			print('[-] check for any typos')


def main():
	print(banner)
	parser = argparse.ArgumentParser(description = "[#] Hash Finder [#]")
	parser.add_argument("-l", "--list", help="Display list of hashing algorithms", action='store_true')
	parser.add_argument("-f", "--file", help="any file; -f <File path>", dest='fpath')
	parser.add_argument("-t","--hash-type", help="type of Hashing Algorithm", dest='hashType')
	parser.add_argument("-n","--hash-numb", help="type of Hashing Algorithm number", dest='hashTypeNumb')
	parser.add_argument("-c","--check-value", help="Hash value to check", dest='hashCheckValue')

	#parser.add_argument('_postIdUrl', nargs='?', help="value of PostID/postUrl", type=str)
		
	# nargs = '*' for all arguments as list
	# nargs='?' for optional argument
	args = parser.parse_args()

	if len(sys.argv) == 1:
		parser.print_help()

		
	if(args.list):
		print(hashAlgosAvailable)
		exit(0)
	
	if(not args.fpath):
		print('[x] No file or file path prvided!')

	elif(not args.hashType and not args.hashTypeNumb):
		print('[x] No Hashing Algorithm prvided!')
		print('[-] Select from the list: ')
		print(hashAlgosAvailable)

	else:
		calculateHashFunction(args.fpath, args.hashType, args.hashTypeNumb, args.hashCheckValue)
		
	


if __name__ == "__main__":
	main()

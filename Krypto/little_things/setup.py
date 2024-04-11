#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
import math
# from secret import flag

# Utility functions
def chunks(l : list, n : int):
	"""Yield successive n-sized chunks from l."""
	for i in range(0, len(l), n):
		yield l[i:i + n]

# Encryption Methods

def encrypt1(message : bytes, key):
	return pow(bytes_to_long(message), key.e, key.n)

# get the e-th root of ciphertext
def decrypt1(ciphertext : int, key):
	return long_to_bytes(ciphertext ** (1 / key.e))

def encrypt2(message : bytes, key):
	r = 440207993569202145226583596168668480279612819965794541699444606998884126327457148126985393713331187326269759129786151827315472662545169229810947283583185940188753204507272015410292547991341421865580434571907487831150551894581100517979422062705719326708845893428059355370710948150227146186294791368354716644074593401065391186346804909062169792789820494220878930621918113842522702840719980702035210790221375054988484360489658798914894297868096164068410349956337623656160859441076123257680687409511415929920760564728135223020626088404535712263440453673827848602042008666139187037894104559208209842699418459046227548274369494390325913146860043311029683073260582295749123383864290580535513555624777329124481863968842759997800343985031020803958083752044340070928621625315960187682219676298491723091409452028712084469300912870666232227855276035007617694078713741109322804779068398754913109357219461822870410839177245857661666072743515936844588884933042735358697038815104339349515893292336683598862297813136372910247113611321570981701692485394194808371648912273085184798875264734186133928625551638315540870469114902162342732282838097849696596328601119607487566568239039051073511095284994830149350910188968078336841520356458362003852374562021
	return pow(bytes_to_long(message) * r, key.e, key.n)

def encrypt3(message : bytes, key):
	bytelength = int(math.floor(math.log2(key.n))) // 8
	msg = message + b'\x00' * (bytelength - len(message))
	return pow(bytes_to_long(msg), key.e, key.n)

def encrypt4(message : bytes, key):
	bytelength = int(math.floor(math.log2(key.n))) // 8
	msg = message * (bytelength // len(message))
	return pow(bytes_to_long(msg), key.e, key.n)

def encrypt5(message : bytes, key):
	bytelength = int(math.floor(math.log2(key.n))) // 8
	msg = b'\xff' * (bytelength - len(message)) + message
	return pow(bytes_to_long(msg), key.e, key.n)

# Actual code
messages = [x for x in chunks(flag.encode(), len(flag) // 5 + 1)]

key = RSA.importKey(open('pubkey.pem','r').read())

encryptors = [encrypt1,encrypt2,encrypt3,encrypt4,encrypt5]

for i in range(5):
	print(encryptors[i](messages[i], key))

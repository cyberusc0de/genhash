
# Include standard modules 
import argparse 
import sys 
import hashlib


# function to convert values to md5 hash 
def convert_to_md5(x): 
	hash_object = hashlib.md5(x.encode())
	md5_hash = hash_object.hexdigest() 
	return md5_hash

# function to convert values to sha1 hash 
def convert_to_sha1(x): 
	hash_object = hashlib.sha1(x.encode())
	sha1_hash = hash_object.hexdigest() 
	return sha1_hash

# function to convert values to sha224 hash 
def convert_to_sha224(x): 
	hash_object = hashlib.sha224(x.encode())
	sha224_hash = hash_object.hexdigest() 
	return sha224_hash

# function to convert values to sha256 hash 
def convert_to_sha256(x): 
	hash_object = hashlib.sha256(x.encode())
	sha256_hash = hash_object.hexdigest() 
	return sha256_hash

# function to convert values to sha384 hash 
def convert_to_sha384(x): 
	hash_object = hashlib.sha384(x.encode())
	sha384_hash = hash_object.hexdigest() 
	return sha384_hash

# function to convert values to sha512 hash 
def convert_to_sha512(x): 
	hash_object = hashlib.sha512(x.encode())
	sha512_hash = hash_object.hexdigest() 
	return sha512_hash

# code banner 
def banner(): 
	print("""
  ____            _   _           _
 / ___| ___ _ __ | | | | __ _ ___| |__
| |  _ / _ \ '_ \| |_| |/ _` / __| '_ \\
| |_| |  __/ | | |  _  | (_| \__ \ | | |
 \____|\___|_| |_|_| |_|\__,_|___/_| |_|
""")
	print("[*] A tool to generate a hashed wordlist ")
	print("[*] such as MD5, SHA1 etc and its corresponding value")
	print("[*] Tool developed by @zidelnet")
	print("------------------------------------------------------")
	
banner()
print("""
Sample Example: Generate MD5 Hash wordlist 
# python genhash.py --hash MD5 --start 1111 --end 9999
# python genhash.py --hash SHA256 --start 1111 --end 5555
""")

# Define the program description 
text = "Generate hashed and plain wordlist to brute-force OTP and password during a web application attack"

# Initiate the parser with a description 
parser = argparse.ArgumentParser(description=text)
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-L", "--list", help="show available hash", action="store_true")
parser.add_argument("--hash", help="set the hash type")
parser.add_argument("--start", type=int, help="the start value of the wordlist")
parser.add_argument("--end", type=int, help="the end value of the wordlist")

# Read arguments from the command line
args = parser.parse_args()

# available hash type 
upper_list = ["MD5","SHA1","SHA224","SHA256","SHA384","SHA512"]
hash_list_available = [i.lower() for i in upper_list]+upper_list 

# check if no argument is given 
if len(sys.argv) <= 1: 
    print("[!] You have not specified any argument")
    sys.exit()

# Check for --version or -V
if args.version:
    print("genhash version 1.0")

# display the available hash type 
if args.list:
	print("[*] Available hash")
	for i in upper_list:
		print(f"--hash {i}")

# check for --hash 
if args.hash:
	if args.hash not in hash_list_available:
		print("[!] The hash selected is not available")
		sys.exit() 
	selected_hash = (args.hash).lower()

if args.start:  
	START_ = args.start 

if args.end: 
	END_ = args.end 


try: 
	# generate sequencial numbers 
	number_list = list(range(START_, END_+1,1))

	if selected_hash == 'md5': 
		# convert the generated sequencial numbers into md5 hash 
		hash_list = [convert_to_md5(str(i)) for i in number_list]

	if selected_hash == 'sha1': 
		# convert the generated sequencial numbers into sha1 hash 
		hash_list = [convert_to_sha1(str(i)) for i in number_list]
	
	if selected_hash == 'sha224': 
		# convert the generated sequencial numbers into sha224 hash 
		hash_list = [convert_to_sha224(str(i)) for i in number_list]
	
	if selected_hash == 'sha256': 
		# convert the generated sequencial numbers into sha256 hash 
		hash_list = [convert_to_sha256(str(i)) for i in number_list]
	
	if selected_hash == 'sha384': 
		# convert the generated sequencial numbers into sha384 hash 
		hash_list = [convert_to_sha384(str(i)) for i in number_list]
	
	if selected_hash == 'sha512': 
		# convert the generated sequencial numbers into sha512 hash 
		hash_list = [convert_to_sha512(str(i)) for i in number_list]

	# convert both list into a dictionary 
	full_list = {hash_list[i]:number_list[i] for i in range(len(number_list))}

	print(f"[+] {selected_hash}-clear-text-list.txt successfully created, containing only the clear text")
	print(f"[+] {selected_hash}-list.txt successfully created, containing only the {selected_hash} hashes")
	print(f"[+] {selected_hash}-full-list.txt successfully created containing both the {selected_hash} Hash the corresponding string value")

	# write the clear-text list into a file 
	with open(selected_hash+"-clear-text.txt","w") as f: 
		for x in number_list: 
			f.write(x+"\n")

	# write the md5 hash list into a file 
	with open(selected_hash+"-list.txt","w") as f: 
		for i in hash_list: 
			f.write(i+"\n")

	# write the full-list into a file 
	with open(selected_hash+"-full-list.txt","w") as f: 
		for i,j in full_list.items(): 
			f.write("{} : {}\n".format(i,j))

except NameError: 
	pass 
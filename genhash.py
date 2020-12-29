
# Include standard modules 
import argparse 
import sys 
import hashlib

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
	print()
	
banner()
# Define the program description 
text = "A tool to generate any type of hashed wordlist for brute forcing password during a web application attack"
# python genhash.py  --hash MD5 --start 1111 --end 9999
# python genhash.py -h MD5 -s 1111 -e 99999
# python genhash.py --list

# Initiate the parser with a description 
parser = argparse.ArgumentParser(description=text)
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-L", "--list", help="show available hash", action="store_true")
parser.add_argument("-H", "--hash", help="set the hash type")
parser.add_argument("--start", type=int, help="the start value of the generator")
parser.add_argument("--end", type=int, help="the end value of the generator")
#parser.add_argument("")
#parser.parse_args()

# Read arguments from the command line
args = parser.parse_args()

# available hash type 
hash_list_available = ["MD5","SHA1"]

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
	for i in hash_list_available:
		#print(i)
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

# generate sequencial numbers 
number_list = list(range(START_, END_,1))

if selected_hash == 'md5': 
	# convert the generated sequencial numbers into md5 hash 
	hash_list = [convert_to_md5(str(i)) for i in number_list]

if selected_hash == 'sha1': 
	# convert the generated sequencial numbers into md5 hash 
	hash_list = [convert_to_md5(str(i)) for i in number_list]

# convert both list into a dictionary 
full_list = {hash_list[i]:number_list[i] for i in range(len(number_list))}

print(f"[+] {selected_hash}-list.txt created containing only the {selected_hash} Hash")
print(f"[+] full-list.txt created containing both the {selected_hash} Hash the corresponding string value")

# write the md5 hash list into a file 
with open(selected_hash+"-list.txt","w") as f: 
	for i in hash_list: 
		f.write(i+"\n")

#write the full-list into a file 
with open("full-list.txt","w") as f: 
	for i,j in full_list.items(): 
		f.write("{} : {}\n".format(i,j))

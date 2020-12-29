
# Include standard modules 
import argparse 
import sys 
import hashlib

# available hash type 
hash_list = ["MD5","SHA1"]

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
parser.add_argument("--start", help="the start value of the generator")
parser.add_argument("--end", help="the end value of the generator")
#parser.add_argument("")
#parser.parse_args()

# Read arguments from the command line
args = parser.parse_args()

# check if no argument is given 
if len(sys.argv) <= 1: 
    print("[-] You have not specified any argument")
    sys.exit()

# Check for --version or -V
if args.version:
    print("genhash version 1.0")

# display the available hash type 
if args.list: 
    print("--hash MD5\n--hash SHA1")

# check for --hash 
if args.hash:
    selected_hash = args.hash

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
	
# function to convert values to md5 hash 
def convert_to_md5(x): 
	hash_object = hashlib.md5(x.encode())
	md5_hash = hash_object.hexdigest() 
	return md5_hash 
	
banner() 


	
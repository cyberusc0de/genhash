# Import hashlib library 
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
	
# function to convert values to md5 hash 
def convert_to_md5(x): 
	hash_object = hashlib.md5(x.encode())
	md5_hash = hash_object.hexdigest() 
	return md5_hash 
	
banner() 

	
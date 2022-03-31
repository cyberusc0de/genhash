## genhash
Developed by @yemilesky 

This tool was designed to test web application using only hashing algorithm in order to brute forcing password during a web application penetration test. It is a good practice to salt user's password before storing them in the database.

It can generate different hashes and plain wordlist to brute-force OTP and password during a web application attack

NOTE: Ensure to use python3 
``` 
$ git clone https://github.com/yemilesky/genhash.git
$ cd genhash
$ python genhash.py -h 
```

```
$ python genhash.py -h 
  ____            _   _           _
 / ___| ___ _ __ | | | | __ _ ___| |__
| |  _ / _ \ '_ \| |_| |/ _` / __| '_ \
| |_| |  __/ | | |  _  | (_| \__ \ | | |
 \____|\___|_| |_|_| |_|\__,_|___/_| |_|

[*] A tool to generate a hashed wordlist
[*] such as MD5, SHA1 etc and its corresponding value
[*] Tool developed by @yemilesky")
------------------------------------------------------
Sample Example: Generate MD5 Hash wordlist 
$ python genhash.py --hash MD5 --start 1111 --end 9999
$ python genhash.py --hash SHA256 --start 1111 --end 5555
```
```
optional arguments: 
  -h, --help                  show this help message and exit 
  -v, --version               show program version 
  -L, --list                  show available hash
  --hash HASH                 set the hash type 
  --start START               the start value of the wordlist 
  --end END                   the end value of the wordlist 
```
The tool generates three files 
1. *-clear-text-list.txt: Clear text generated wordlist that can be used to brute-force OTP and password  
2. *-list.txt: The hashed wordlist that can also be used to brute-force OTP and password 
3. *-full-list.txt: A full list consisting the hashes selected and the corresponding value, there is no need to crack the hash again. 

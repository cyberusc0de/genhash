## genhash
Developed by @zidelnet 

This tool was designed to test web application using only hashing algorithm in order to brute forcing password during a web application penetration test. It is a good practice to salt user's password before storing them in the database.

NOTE: Ensure to use python3 
``` 
$ git clone https://github.com/zidelnet/genhash.git
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
[*] Tool developed by @zidelnet")
------------------------------------------------------
Sample Example: Generate MD5 Hash wordlist 
$ python genhash.py --hash MD5 --start 1111 --end 9999
```
```
optional arguments: 
  -h, --help                  show this help message and exit 
  -v, --version               show program version 
  -L, --list                  show available hash
  --hash HASH                 set the hash type 
  --start START               the start value of the generator 
  --end END                   the end value of the generator 
```

The full-list.txt consist of the hashes and the corresponding value, there is no need to crack the hash again. The other wordlist can be used for the brute forcing. 

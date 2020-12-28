# pyHashFinder
Python Script used to find Hash values (sha256, MD5...) for various files and compare.

# Usage
```
$ python3 hashFinder.py

usage: hashFinder.py [-h] [-l] [-f FPATH] [-t HASHTYPE] [-n HASHTYPENUMB] [-c HASHCHECKVALUE]

[#] Hash Finder [#]

optional arguments:
  -h, --help              show this help message and exit
  -l, --list              Display list of hashing algorithms
  -f FPATH, 
          --file FPATH  
                          any file; -f <File path>
  -t HASHTYPE, 
          --hash-type HASHTYPE
                          type of Hashing Algorithm
  -n HASHTYPENUMB, 
          --hash-numb HASHTYPENUMB
                          type of Hashing Algorithm number
  -c HASHCHECKVALUE, 
          --check-value HASHCHECKVALUE
                          Hash value to check
                          
[+] List of Hashing Algorithms

  1) sha512      2) sha256       3) md5
  4) sha1        5) sha224       6) sha384
  7) sha3_224    8) sha3_256     9) sha3_384
 10) sha3_512   11) shake_128   12) shake_256
 13) blake2b    14) blake2s
```
## Example
```
$ python3 hashFinder.py -f Ubuntu20amd64.iso -t sha256
or
$ python3 hashFinder.py -f Ubuntu20amd64.iso -n 2

output:
[+] Selected Algorithm:  sha256
[+] File provided:  Ubuntu20amd64.iso
[+] Hash value of file:
d2f15015d1dd9687e76adca0cc1033d0a2440ae91a85b191bb9bfa179a031f33

```

#!/usr/bin/python3.5
#
#	Template for password hashsum generator.
#
#	Idea is to fill 'programlist' -list with programs that are in use, and
#	link hashsum type, so that it won't be nesessary to remember
#	hashsum <-> program relation by heart.
#
#	As a bonus, this program generates password-hash from
#	promted password and hashsum related to the program
#	which is selected.
#
#	Author Joel Lappalainen

import hashlib

programlist = { 'workplace-sql':'sha256',
		'my-weak-sql':'md5'	}

print("Programs to create password hashsum for")
for i in programlist:
	print(i)

selector = input("Write program name: ")
hashsum=programlist[selector]

passwd = input("Write password to hash: ")
passwd = passwd.encode()

hash_object1 = getattr(hashlib, hashsum)
hash_object2 = hash_object1(passwd)
hex_dig = hash_object2.hexdigest()

print(hex_dig)

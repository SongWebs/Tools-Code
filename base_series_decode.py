# This program will help you to decode the code of Base Series 
# Writen by SongWebs
# SongWebs@outlook.com

import os
import base64
import base58
import base91

f = 1
except_tip = "The code cannot be decode by "
str_base = {
	"base16" : "", 
	"base32" : "", 
	"base64" : "", 
	"base58" : "", 
	"base91" : ""
	}

os.system("cls")
print("*"*20,"Starting","*"*20)

while  f:
	s = input("Input your code here:\n")
	if s != "":
		try:
			str_base["base16"] = base64.b16decode(s)
		except:
			print(except_tip, "base16.")
		try:
			str_base["base32"] = base64.b32decode(s)
		except:
			print(except_tip, "base32.")
		try:
			str_base["base64"] = base64.b64decode(s)
		except:
			print(except_tip, "base64.")
		try:
			str_base["base58"] = base58.b58decode(s)
		except:
			print(except_tip, "base58.")
		try:
			str_base["base91"] = base91.decode(s)
		except:
			print(except_tip, "base91.")

		print("-"*20, "Decode result:", "-"*20)
		
		for key, value in str_base.items():
			if value != "":
				print(str(key), ":    ", str(value)) 

		print("-"*20, "Decode finish", "-"*20)
		print()

		f = 0
	else:
		print("Your input is invalid!!! Please retry ...")
		f = 1

print("*"*20,"End","*"*20)
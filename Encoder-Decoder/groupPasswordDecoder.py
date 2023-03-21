# This Python program will help you decode the group password
# Writen by SongWebs
# SongWebs@outlook.com
# Example：s = "bE0veldtTDs7NzlTe3hzbSFYSj5Sa2U6eyQ4NyVrI3FvWFU6Qls7QlVK"， key = "589164"

s = input("Please input the Cypher:")
key = input("Please input the key:")
pwd = []
out = ""

i = 0
length = 6

while i < len(s):
	if i+length > len(s):
		length = len(s) - i
	pwd.append(s[i:i+length])
	i = i + length

# print (pwd)

for p in pwd:
	for c_i in range(len(p)):
		out += chr(ord(p[c_i])^int(key[c_i]))

print(out)

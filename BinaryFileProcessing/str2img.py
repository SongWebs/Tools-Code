import os
import struct

txt_file = open("./me}.txt", "r")
txt = txt_file.read()
txt_list = []
i = 0
while i < len(txt):
	# temp = "0x" + txt[i:i+2]
	temp = txt[i:i+2]
	txt_list.append(temp)
	i = i + 2
print (txt_list)
output = open("flag.png", "wb")
for i in txt_list:
	output.write(bytes().fromhex(i))
	print(bytes().fromhex(i))
output.close()
txt_file.close()


'''
# Litters from lower to Upper

	for j in range(len(temp)):
		if ord(temp[j]) > ord('a') and ord(temp[j]) < ord('z'):
			temp[j] = temp[j] - 32
'''
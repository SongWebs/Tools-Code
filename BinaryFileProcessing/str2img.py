import os
import struct

# 打开名为“me.txt”的文本文件，并读取其中的内容
txt_file = open("./me}.txt", "r")
txt = txt_file.read()

# 将读取的内容按照每两个字符一组的方式拆分为一个列表（txt_list）
txt_list = []
i = 0
while i < len(txt):
	# temp = "0x" + txt[i:i+2]
	temp = txt[i:i+2]
	txt_list.append(temp)
	i = i + 2
print (txt_list)

# 使用Python的bytes().fromhex()方法将每个十六进制字符串转换为相应的二进制数据，并将其写入一个名为“flag.png”的文件中
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
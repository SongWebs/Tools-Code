# This Python program will help you decode the group password
# Writen by SongWebs
# SongWebs@outlook.com

print("*"*40)
s = input("Just give me the HEX string: \n")

def separator():

	global s
	cut1 = ' ,'
	cut2 = ', '
	cut3 = ','
	cut4 = ' '

	if cut1 in s:
		s = s.split(cut1)
		return 1
	elif cut2 in s:
		s = s.split(cut2)
		return 2
	elif cut3 in s:
		s = s.split(cut3)
		return 3
	elif cut4 in s:
		s = s.split(cut4)
		return 4
	return 0

form1 = "\\\\u"
form2 = "0x"

separator()

if form1 in s:
	if not separator():
		s = s.replace("\\\\u", " 0x")
		separator()
		s = s[1:len(s)]
	else:
		s = s.replace("\\\\u", "0x")

#print(s)

s = list(map(lambda x: chr(int(x, 16)),s))

print("\n","*"*40)
print("The HEX String was Converted:")
for i in s:
	print(i, end="")
print("\n")
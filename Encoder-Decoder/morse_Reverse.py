s = input("input the MORSE code: \n")
morse = ""
for i in range(len(s)):
	if s[i] == "-":
		morse += "."
	elif s[i] == ".":
		morse += "-"
	else:
		morse += s[i]

for i in morse:
	print(i,end="")
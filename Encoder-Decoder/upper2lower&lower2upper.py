s = input("Just input a Fucking String: ")
s1 = []
for i in range(len(s)):
	if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
		s1.append(ord(s[i]) + ord('A') - ord('a'))
	elif ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
		s1.append(ord(s[i]) + ord('a') - ord('A'))
	else:
		s1.append(ord(s[i]))

print(s1)
s1 = list(map(lambda x: chr(int(x)),s1))

for i in s1:
	print (i,end="")
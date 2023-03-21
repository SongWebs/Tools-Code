import hashlib

s="0fe750"
def count_md5(strings):
    md5=hashlib.md5(strings.encode('utf-8'))
    ret=md5.hexdigest()
    return ret
for i in range(1,1000000):
    key=count_md5(str(i))
    if key[0:6]==s:
        print(str(i))
# !/usr/bin/env python
# -*- coding: utf_8 -*-
# Author: 蔚蓝行
# http://www.cnblogs.com/duanv
e = input("请输入要解密的字符串\n")
elen = len(e)
field=[]
for i in range(2,elen):
            if(elen%i==0):
                field.append(i)

for f in field:
    b = int(elen / f)
    result = {x:'' for x in range(b)}
    for i in range(elen):
        a = i % b;
        result.update({a:result[a] + e[i]})
    d = ''
    for i in range(b):
        d = d + result[i]
    print ("分为\t"+str(f)+"\t"+"栏时，解密结果为：  "+d)
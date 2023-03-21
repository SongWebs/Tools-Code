file_name = input("Input the img_file name: ")
input_img = open(file_name, 'rb')
img_all = input_img.read()
ss = img_all[::-1]
output = open('trueFlag.png', 'wb')
output.write(ss)
input_img.close()
output.close()
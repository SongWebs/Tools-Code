# This Python 3.X program will help you convert the txt file to image file
# Writen by SongWebs
# Mailbox: SongWebs@outlook.com

# Import the PIL lib 
from PIL import Image

# Read the txt file to string
file_txt = open("pixel.txt", "r")
str_pix = file_txt.read().split("\n")

width, height = 0, 0

# Get the width and height of the image
for i in str_pix:
	if int(i.split(" ")[0]) > width:
		width = int(i.split(" ")[0])
	if int(i.split(" ")[1]) > height:
		height = int(i.split(" ")[1])

# Output the width and height
print ("Width: ", width, " Height: ", height)
img = Image.new("RGB", (width,height))

# Write pixel to new image file: 
# pixTuple(R, G, B, A)
# x -> width, y -> height, R -> red, G -> green, B -> blue, A -> transparency
for i in str_pix:
	x = int(i.split(" ")[0])
	y = int(i.split(" ")[1])
	R = int(i.split(" ")[2])
	G = int(i.split(" ")[3])
	B = int(i.split(" ")[4])
	pixTuple = (R, G, B, 0)
	img.putpixel((x-1, y-1), pixTuple)

# Save the image file
img.save("output.png")
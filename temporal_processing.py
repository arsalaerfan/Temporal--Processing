'''
Author: Erfanullah Arsala and Joel Terran
Date: 10/1/19
CST205
Code summary:

Created a final image variable that made a new white image with the same demensions as the pictures.
I used a nested loop to get the data of the pixels for each image at the exact same coordinates, added all of it to the empty list, sorted the empty
list. After getting the median of all that pixel data, I put on the plain white background
image and save it as a png file outside my loops.

'''
import glob
from PIL import Image
import math

#open each image seperatly
pic1 = Image.open("1.png")
pic2 = Image.open("2.png")
pic3 = Image.open("3.png")
pic4 = Image.open("4.png")
pic5 = Image.open("5.png")
pic6 = Image.open("6.png")
pic7 = Image.open("7.png")
pic8 = Image.open("8.png")
pic9 = Image.open("9.png")
pic10 = Image.open("10.png")
pic11 = Image.open("11.png")

#make new picture with same demonsions to hold the final picture
finalImage = Image.new('RGB',(pic1.width, pic1.height),'white')

#empty list to hold the median filtered data from all images
big_pixel_list = [pic1.getpixel((0,0))]*11

#loop through each image and get data for all images at the exact
#point and append it to the empty list, sort it, then get median.
for x in range(pic1.width):
	for y in range(pic1.height):
		#get pixel data for each image
		pixel = pic1.getpixel((x,y))
		big_pixel_list[0]=pixel
		pixel = pic2.getpixel((x,y))
		big_pixel_list[1]=pixel
		pixel = pic3.getpixel((x,y))
		big_pixel_list[2]=pixel
		pixel = pic4.getpixel((x,y))
		big_pixel_list[3]=pixel
		pixel = pic5.getpixel((x,y))
		big_pixel_list[4]=pixel
		pixel = pic6.getpixel((x,y))
		big_pixel_list[5]=pixel
		pixel = pic7.getpixel((x,y))
		big_pixel_list[6]=pixel
		pixel = pic8.getpixel((x,y))
		big_pixel_list[7]=pixel
		pixel = pic9.getpixel((x,y))
		big_pixel_list[8]=pixel
		pixel = pic10.getpixel((x,y))
		big_pixel_list[9]=pixel
		pixel = pic11.getpixel((x,y))
		big_pixel_list[10]=pixel
		#after appending the data from each image we sort it data
		big_pixel_list.sort()
		#put all new pixel data on the plain white image we created above
		finalImage.putpixel((x,y),big_pixel_list[5])

#save all data as a new image with all the median pixel data from every image
finalImage.save("finalPic.png")



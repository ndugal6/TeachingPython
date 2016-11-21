from PIL import Image

img = Image.open("me_cancun.jpg")
print(img.size)
print(img.format)
print(img.getdata())
for pixel in iter(img.getdata()):
    print(pixel)
#Starting cordinates w/ origin at top left (100,100) (100 to the right then 100 down) (300, 375)
area = (100,100, 300, 375)
cropped_img = img.crop(area)
cropped_img.show()
#img.show()

#Copying an image
nephew = Image.open("me_ReidCrestedButte.jpg")
agrChristmas = Image.open("me_christmas.jpg")

area2 = (100, 100, 451, 451)
agrChristmas.paste(nephew,area2)
agrChristmas.show()
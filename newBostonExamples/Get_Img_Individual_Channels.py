from PIL import Image

# nephew = Image.open("me_ReidCrestedButte.jpg")
meUS = Image.open("me_UintaSummit.jpg")
meCA = Image.open("me_90MilePaddleCORvr.jpg")
#show  its rgb file
# print(nephew.mode)

r, g, b = meUS.split()
r2, g2, b2 = meCA.split()
#r.show()
# g.show()
# b.show()


new_img = Image.merge("RGB", (r, g, b))
new_img.show()

new_img2 = Image.merge("RGB", (g, b, r))
new_img2.show()


#Mixing the two photos rgb values creates an entirely new picture. Pretty cool
new_img3 = Image.merge("RGB", (r2, g, b2))
new_img3.show()

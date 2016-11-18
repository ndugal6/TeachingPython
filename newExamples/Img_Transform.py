from PIL import Image

grizzly = Image.open("Me_30DaysInWoodsReturn.jpg")

square_griz = grizzly.resize((250,250))
flip_griz = grizzly.transpose(Image.FLIP_LEFT_RIGHT)
spin_griz = grizzly.transpose(Image.ROTATE_90)

square_griz.show()
flip_griz.show()
spin_griz.show()


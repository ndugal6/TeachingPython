from PIL import Image
from PIL import ImageFilter


me = Image.open("me_UintaSummit.jpg")
black_white = me.convert("L")
black_white.show()

blur_me = me.filter(ImageFilter.BLUR)
blur_me.show()

detail = me.filter(ImageFilter.DETAIL)
detail.show()

edges = me.filter(ImageFilter.FIND_EDGES)
edges.show()

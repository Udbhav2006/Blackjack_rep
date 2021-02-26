from PIL import Image

im = Image.open('spaceship.jpg')
new_im = im.resize((700,700))
new_im.show()
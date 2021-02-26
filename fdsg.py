from PIL import Image

im = Image.open('Cards_pics/Ace of spades.png')
im.thumbnail((100,100))
im.save('Cards_pics/Ace of spades.png')
im.show()
from PIL import Image
import os

# im = Image.open('Cards_pics/2 of clubs.png')
# im.thumbnail((100,100))
# im.save('Cards_pics/2 of clubs.png')
# im.show()

# obj = os.scandir('D:/Udbhav/Blackjack_rep/Cards_pics')
# for pic in obj:
#     im = Image.open(pic.path)
#     im.show()

im = Image.open('table.jpg')
im.thumbnail((1300,700))
im.save('table.jpg')
im.show()
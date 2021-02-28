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
a = Image.open('big_back.jpg')
card = Image.open('Cards_pics/Ace of spades.png/')
q = Image.open('Cards_pics/Queen of clubs.png')
d = [card,q]
im = a.copy()
im.thumbnail((1300,650))
i = 1
for each in d:
    im.paste(each, (i,1))
    i+=82
im.show()
print(im.size)


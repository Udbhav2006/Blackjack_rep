import os
from PIL import Image

# for pic in os.scandir('D:/Udbhav/Blackjack_rep/Num pics'):
#     back_im = Image.open('big_back_no_text.jpg')
#     back_im_copy = back_im.copy()
#     num = 2
#     num_im = Image.open(f'Num pics/{num}.png')
#     # num_im.thumbnail((500,500))
#     back_im_copy.paste(num_im)
#     back_im_copy.show()

for pic in os.scandir('Cards_pics'):
    im = Image.open(pic.path)
    a = im.resize((200,200))
    # a.show()
    # im.show()
    print(a.size)
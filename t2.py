from PIL import Image,ImageEnhance
import os
img1 = Image.open('13.jpg')
img1.save('13.pdf')
img1.show()

max_size = (250,250)
img1.thumbnail(max_size)
img1.save('1.jpg')

for item in os.listdir():
    if item.endswith('.jpg'):
        img1 = Image.open(item)
        filename,extension = os.path.splitext(item)
        img1.save(f'{filename}.pdf')


enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(10).save('i.jpg')
# brightness
#color
#contras

#blur guassian 



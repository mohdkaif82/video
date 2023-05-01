from PIL import Image, ImageDraw
import requests
# from moviepy.editor import *
from PIL import ImageFont
def img_create(text):
# create a new image
# image = Image.new('RGB', (500, 500), color='white')
    img_text_size=len(text)*18
    image = Image.new('RGBA', (img_text_size, 100), (255, 255, 255, 0))


    # create a new ImageDraw object
    draw = ImageDraw.Draw(image)

    # set the Hindi font
    hindi_font = ImageFont.truetype('TiroDevanagariHindi-Regular.ttf', size=50)
    # draw Hindi text on the image
    draw.text((0, 30),text, font=hindi_font, fill='white')

    # save the image
    image.save('media/images/hinditext/hindi_text.png')
    

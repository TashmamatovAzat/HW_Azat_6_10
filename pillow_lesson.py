from PIL import Image, ImageDraw, ImageFont

image = Image.open('jelly.png')

# cropped_image = image.crop((0, 80, 200, 400))
#
# cropped_image.save('pil_results/jelly_cropped.png')

# rotated_image = image.rotate(180)
#
# rotated_image.save('pil_results/jelly_rotated.png')

# text_image = ImageDraw.Draw(image)
# text = 'This is Codify property'
# font = ImageFont.truetype('arial.ttf', size=32)
# text_image.text((20, 20), text, font=font)
# image.save('pil_results/jelly_text.png')

# image.convert('RGB').save('pil_results/jelly_to_jpeg_format.jpeg', format='jpeg')

# image = image.resize((200, 200))
#
# image.save('pil_results/jelly_hard_resize.png')
#
# w, h = image.size
#
# new_width = 300
#
# new_height = int(new_width * h / w)
#
# image = image.resize((new_width, new_height))
#
# image.save('pil_results/jelly_resize_by_width.png')

w, h = image.size

new_height = 240

new_width = int(w / h * new_height)

image = image.resize((new_width, new_height))

image.save('pil_results/jelly_resize_by_height.png')

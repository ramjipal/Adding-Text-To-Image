from PIL import Image, ImageDraw, ImageFont
#open the file and assign into image variable
orig_img = Image.open("manwithguitar.jpg")
#select image font and size
title_font = ImageFont.truetype("Freehand-Regular.ttf", 500)
#Rendring text
input_text = "Alone with Nature"
#convert image into editable format
editable_img = ImageDraw.Draw(orig_img)
#rendring the image
editable_img.text((20,20), input_text, (255,215,0), font = title_font)
#export the result
orig_img.save("result.jpg")
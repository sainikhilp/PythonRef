
from PIL import Image

mac = Image.open('my_computer_img.jpg')



print(mac.size)
print(mac.format_description)
top_cropped_mac=mac.crop((0,0,100,100))
bottom_cropped_mac=mac.crop((0,150,100,200))


mac.show()
top_cropped_mac.show()
bottom_cropped_mac.show()

mac.resize((400,200))

mac.show()

rotated_mac=mac.rotate(90)
rotated_mac=mac.show()

#controls the transparency of the images
#alpha value can last from 0 to 255


mac.putalpha(128)

#for saving the image
mac.save("transparent_mac.png")

#you can paste one image over the other by using the following method
#image.paste(image to be pasted, allignment,mask)
#example
#mac.paste(red,(0,0),red)
#this indicates that a image called red will be pasted over mac 
# which will be alligned at the left top corner(0,0) 
#mask will usually be same as the image itself


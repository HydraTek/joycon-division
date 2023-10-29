from PIL import Image, ImageFilter, ImageOps, ImageDraw

def concatImg(im1,im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0,0))
    dst.paste(im2, (0, im1.height))
    return dst
def label(im, label):
    I1 = ImageDraw.Draw(im)
    I1.text((28, 36), label)
    return 




 # Open Image
src = 'imgSrc/health254.jpg' # Default img src
snc = 'imgSinc/test.jpg' # Default output
ans = input('Do you want to use the default image [Y]/n')
if ans == 'n':
   src = 'imgSrc/' + input('imgSrc/')
while True:
   
   try:
       image = Image.open(src)
   except IOError as err:
       print(err)
       src = 'imgSrc/' + input('Image failed to open, try again: imgSrc/')
   else:
       break


#modified = base.filter(ImageFilter.BLUR())

# Sharpen Image
image = image.convert('L') # Grayscale
image = ImageOps.invert(image) # Invert image

# Resize
scale = 5
image = image.resize((image.size[0] * scale, image.size[1] * scale), Image.Resampling.LANCZOS)
image = image.filter(ImageFilter.EDGE_ENHANCE)
image = image.filter(ImageFilter.ModeFilter(5))
image = image.filter(ImageFilter.SHARPEN)
#thresh = 160
#x = lambda a : 0 if a < thresh else 255
#image = image.point(x)


image.save(snc)

# Invert

# Save Image

    
print('End Program')


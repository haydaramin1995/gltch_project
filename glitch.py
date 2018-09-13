# glitch, goal is to remove all the blue in one file

from PIL import Image
from PIL import ImageDraw

# REQUIRES: img is a valid instance of Image class
# DOES: sorts through pixels in image, if in blue range we don't make it white
# TAKES: O(N^2) each call
# RETURNS: img that has been processed
def make_blue(img, lowerBound, upperBound):
    assert(lowerBound > -1)
    assert(upperBound < 257)
    draw = ImageDraw.Draw(img)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x,y))
            bluePixel = pixel[1]
            if(bluePixel > lowerBound and bluePixel < upperBound):
                bluePixel = bluePixel - 20
                draw.point((x,y), fill=(pixel[0],pixel[2],bluePixel,255) )
    return img

def main():
    name = raw_input("enter jpg filepath: ")
    name = name.rstrip()
    im = Image.open(name)
    sub_im = Image.open(name)
    sub_im = make_blue(sub_im, 55, 100)
    sub_im.show()
    im.show()

if __name__ == "__main__":
    main()

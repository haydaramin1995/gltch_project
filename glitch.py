# glitch, goal is to remove all the blue in one file

from PIL import Image
from PIL import ImageDraw

# REQUIRES: img is a valid instance of Image class
# DOES: sorts through pixels in image, if in blue range we don't make it white
# TAKES: O(N^2) each call
# RETURNS: img that has been processed
def make_blue(img, lowerBound, upperBound):
    assert(lowerBound < upperBound)
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


# TODO: test to see which image files we can open with it
# REQUIRES: N/A
# DOES: opens an image file (jpeg) and returns an image
# RETURNS: an Image object
def open_file():
    name = raw_input("enter jpg filepath: ")
    name = name.rstrip()
    im = Image.open(name)
    return im


# DOES: displays(prints) the opptions for the display function
def display_options():
    print("d - display this menu again")
    print("o - open image file for processing")
    print("s - save image to file ")
    print("r - run a filter on the image")
    print("q - quit shell")


# REQUIRES: N/A
# DOES: acts as driver of program, displays a menu of options
# lets user select and execute any of them
# RETURNS: n/a
def display():
    file_sucsessfully_opened = False
    image_to_process = Image
    display_options()
    user_choice = raw_input("$ ")
    while(True):
        if(user_choice == "o" or user_choice == "open" or user_choice == "O"):
            image_to_process = open_file()
            file_sucsessfully_opened = True
        if(user_choice == "s" or user_choice == "save" or user_choice == "S"):
            image_path_name = raw_input("Enter the name of the image save ? ")
            image_to_process.save(image_path_name)
        if(user_choice == "r" or user_choice == "run" or user_choice == "R"):
            if(file_sucsessfully_opened):
                print("blue filter:")
                run_input = raw_input(" processing: ")
                if(run_input == 'b'):
                    make_blue(image_to_process, 10, 140)
                    image_to_process.show()
            else:
                print("yo homie I am p sure u haven't opened a file so do that first")
        if(user_choice == "q" or user_choice == "quit" or user_choice == "Q"):
            break
        if(user_choice == "d" or user_choice == "display" or user_choice == "D"):
            display_options()
        user_choice = raw_input("$ ")


def main():
    display()


if __name__ == "__main__":
    main()

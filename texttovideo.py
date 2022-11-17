#!python

#Makes a slideshow out of an imput document. Document must be broken up into lines and each line put into an array. Put your document in  a raw text format and play with regex. Put that list in doc.py. Hymn to Pan by Aleister Crowely provided as an example. Then run texttovideo.py. Dependent on imagemagick wand and ffmpeg.

#import the document to be made into  video
import doc as script

#import os to run ffmpeg scripts at end.
import os

#import wand moduals
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import math

# frame counter
n = 0

#total number of frames
length = len(script.ls)

#main
print("Starting...")

#for each line in the script
for i in script.ls:
    #prevent empty string, making white space instead
    if i == "":
        i = " "
    #magic code I copied from a tutorial
    with Drawing() as draw:
        with Image(width = 1920, height = 1080, background = Color('black')) as image:
            draw.font = 'Roboto-black'
            draw.font_size = 72
            draw.gravity='center'
            draw.stroke_color='white'
            draw.text(0,0, i)
            draw(image)
            
            #make file name
            var = "img" + f"{n:04d}" + ".png"
            #render image
            image.save(filename = var)
            print("rendered image " + var + " of " + str(length))
            #add to count
            n = n+1

#finish up
print("rendering video...")
os.system("ffmpeg -f image2 -framerate 0.33 -i img%04d.png -s 1920x1080 out.avi")
print("cleaning up")
os.system("rm *.png")
print("done!")

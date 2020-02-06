#import statements

from math import*
#uses the Pillow library to import the image
from PIL import Image


imageName = input("Enter image name: ")
img = Image.open(imageName)
print("Image succesfully opened.")
width, height = img.size

#Daltonization algorithm for Deutaronopic patients
for i in range(3):
   for x in range(width):
      for y in range(height):
          oldValue = img.getpixel( (x,y) )

          oldRed = oldValue[0]
          oldGreen = oldValue[1]
          oldBlue = oldValue[2]

          longValue = (17.8824*oldRed) + (43.5161*oldGreen) + (4.11935 * oldBlue)
          medValue = (3.45565*oldRed) + (27.1554*oldGreen) + (3.86714 * oldBlue)
          shortValue = (0.0299566*oldRed) + (0.184309 *oldGreen) + (1.46709  * oldBlue)

          longValue = (1*longValue) + (0*medValue) + (0 * shortValue)
          medValue = (0.494207*longValue) + (0*medValue) + (1.24827 * shortValue)
          shortValue = (0*longValue) + (0 *medValue) + (1  * shortValue)

          newRed = (0.0809444479 * longValue) + (-0.130504409 * medValue) + (0.116721066 * shortValue)
          newGreen = (-0.0102485335 * longValue) + (0.0540193266 * medValue) + (-0.113614708 * shortValue)
          newBlue = (-0.000365296938 * longValue) + (-0.00412161469 * medValue) +(0.693511405 * shortValue)

          newRed = oldRed - newRed
          newGreen = oldGreen - newGreen
          newBlue = oldBlue - newBlue

          newRed = (1.0 * newRed) + (0.7 *newGreen) + (0.0 * newBlue)
          newGreen = (0.0 * newRed) + (0.0 *newGreen) + (0.0 * newBlue)
          newBlue = (0.0 * newRed) + (0.7 *newGreen) + (1.0 * newBlue)

          newRed = int(ceil(newRed + oldRed))
          newGreen = int(ceil(newGreen + oldGreen))
          newBlue = int(ceil(newBlue + oldBlue))

          img.putpixel((x,y), (newRed, newGreen, newBlue))

print("Succesfully corrected image.")
img.save("correctedImage.jpg")
print("Succesfully saved image.")

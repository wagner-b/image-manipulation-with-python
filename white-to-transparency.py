# BSD 3-Clause License
#
# Copyright (c) 2021, Wagner Bertholdo Burghausen
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# This is a simple Python program to replace the white color of an image
# with 100% transparency.
# Note: to run this script you need the python package 'pillow' installed

from PIL import Image

print('Type the exact name of the image with the extension (like .png or .jpg)')
print('Remember that the image needs to be in the same folder you are now')
user_input = input('Image name: ')

img = Image.open(user_input)

# Convert the pixels to RGBA format
img = img.convert('RGBA')

# Get the color of all pixels
pixels = img.getdata()

# create a new list to store the new values for the pixels
new_data = list()

print()
print('Type the threshold value of the darkness / brightness you want to use')
print('It needs to be an integer between 0 and 255')
print('The higher the value, the closest it is to white')
print('Suggested values: between 100 and 240, but it depends on your image')
print('You can try different values until you get the desired result')
threshold = int(input('Value: '))
print()

# This loop appends only the darker pixels to the new list,
# and replaces the brighter pixels with 100% transparency
for pixel in pixels:

    if pixel[0] > threshold and pixel[1] > threshold and pixel[2] > threshold:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(pixel)


# Put the new pixels into the image and save it
img.putdata(new_data)
new_image = input('Type the name for the new image: ')
img.save(new_image + '.png')

# Close the image
img.close()
print('Done.')

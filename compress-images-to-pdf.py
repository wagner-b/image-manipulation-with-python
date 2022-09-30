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


# Python script to create a single compressed PDF file from a set of images

# You need to put all images in a single folder, in the same directory
# in which this script will be executed.

# Rename all images in (alphabetical or numeric) order for the merging process.
# All images should be of the same extension (e.g. all png or all jpg)

# The images will be compressed and saved with a different name, and then
# the new compressed images will be merged into one pdf file.

# Each image will be a page of the PDF file, with the size of an A4
# paper sheet in portrait mode, without margins.

# The images will be compressed to less than 1/3 of their original file size
# (bytes), while still maintaining most of the original image quality.

# The python packages pillow and fpdf are required for this script to work!

###############################################

import os
from sys import platform
from fpdf import FPDF


# Function definition

def compress_images(image_paths_list, fpath, image_type):
    """
    This function opens all images in a specified folder, and
    then compresses them and saves them in a new folder called
    'compressed_images', inside the specified folder.

    Required input variables:

    `image_paths_list`: A list of strings with the complete paths of all
    the images to be compressed.

    `fpath`: A string indicating the complete path of the folder
    which contains all the images that will be compressed.

    `image_type`: A string indicating the extension type of the images
    (e.g. '.png' or '.jpg')

    This function will create compressed images with 1/2 (half) of
    the image resolution scale, and with less than 1/3 (one third)
    of the original image file size (bytes), while preserving most
    of the image quality.

    If you need even smaller image files, you could reduce the
    the value of the 'quality' parameter, though this would lower
    the image quality.
    """

    from os import mkdir
    from PIL import Image
    from sys import platform

    # Creating the compressed_images folder
    # Windows uses the backward slash (\), other systems use the forward slash (/)
    if platform.startswith('win'):
        mkdir(fpath + '\\compressed_images')
    else:
        mkdir(fpath + '/compressed_images')

    for i in range(len(image_paths_list)):
        pic = Image.open(image_paths_list[i])
        w, h = pic.size
        new_w, new_h = w//2, h//2
        new_pic = pic.resize((new_w, new_h), Image.ANTIALIAS)


        if platform.startswith('win'):
            new_pic.save(fpath + '\\compressed_images' +
                         f"\\compressed_image_{i+1:04d}" + image_type,
                         optimize=True, quality=90)
        else:
            new_pic.save(fpath + '/compressed_images' +
                         f"/compressed_image_{i+1:04d}" + image_type,
                         optimize=True, quality=90)

    print("All images were compressed and saved!")
    if platform.startswith('win'):
        print(f"The compressed JPG images were saved in {fpath}\\compressed_images")
    else:
        print(f"The compressed JPG images were saved in {fpath}/compressed_images")
    print()

###############################################

# Get user input

print('The folder containing the images to be merged needs to be in')
print('the same directory this script is being executed.') 
print('Rename the images in order for the merging process.')
print()

folder = input('Type the exact name of the folder containing the images: ')
fpath = os.path.abspath(folder)
print()

pdf_name = input('Type the name for the PDF file that will be generated: ') + '.pdf'
print()

image_type = input('Type the extension of your images (e.g. png, jpg): ')
image_type = '.' + image_type
print()

###############################################

# Main script

if os.path.exists(fpath):

    # Creating the list with the paths of the image files
    # Windows uses backward slash (\), other systems use forward slash (/)
    if platform.startswith('win'):
        image_list = [f"{fpath}\\{image}" for image in os.listdir(fpath)
                      if image.endswith(image_type)]
    else:
        image_list = [f"{fpath}/{image}" for image in os.listdir(fpath)
                      if image.endswith(image_type)]

    image_list.sort()

    print('Compressing and saving images, please wait...')
    print()

    compress_images(image_list, fpath, image_type)

    # Creating a list with only the newly created compressed images
    if platform.startswith('win'):
        compressed = [f"{fpath}\\compressed_images\\{image}" for image in
                      os.listdir(fpath + '\\compressed_images')]
    else:
        compressed = [f"{fpath}/compressed_images/{image}" for image in
                      os.listdir(fpath + '/compressed_images')]

    compressed.sort()

    print('Creating the PDF file, please wait...')
    print()

    pdf = FPDF()
    for image in compressed:
        pdf.add_page()
        pdf.image(image, 0, 0, 210, 297)
        # 210 and 297 are the dimensions of an A4 size sheet.

    # Save the pdf file
    pdf.output(pdf_name, "F")

    if platform.startswith('win'):
        print(f"Done. The PDF file was saved as {os.path.abspath('')}\\{pdf_name}.")
    else:
        print(f"Done. The PDF file was saved as {os.path.abspath('')}/{pdf_name}.")

else:
    print(f"folder {folder} not found.")
    print('Check if the name of the folder is correct (case sensitive).')
    print('The folder needs to be in the same directory of this script.')


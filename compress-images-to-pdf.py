# BSD 3-Clause License
#
# Copyright (c) 2021-2023, Wagner Bertholdo Burghausen
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


# This is a Python script to create a single PDF file from a set of images

# Rename all images in (alphabetical or numeric) order for the merging process.
# All images should be in the same folder, with the same extension
# (e.g. all png or all jpg)

# The images will be compressed and saved with a different name, and then
# the new compressed images will be merged into one pdf file.

# Each image will be a page of the PDF file, with the size of an A4
# paper sheet in portrait mode, without margins.

# This script requires the python packages pillow and fpdf (or fpdf2)

###############################################

import os
from sys import platform
from fpdf import FPDF


def compress_images(image_paths_list, fpath):
    """
    This function opens all images in a specified folder, and then
    reduces them to half their size, and saves them in a new folder
    called 'compressed_images', inside the specified folder.

    Required input variables:

    `image_paths_list`: A list of strings in which each string is
    the absolute path of an image file.

    `fpath`: A string indicating the absolute path of the folder
    that contains the itens in `image_paths_list`.
    """

    from os import mkdir
    from PIL import Image
    from sys import platform

    # Get the extension of the images
    image_ext = '.' + image_paths_list[0].split('.')[-1]
    
    # Creating the compressed_images folder
    mkdir(fpath + '/compressed_images')

    # Open each image, resize, compress, and save it
    for i in range(len(image_paths_list)):
        pic = Image.open(image_paths_list[i])
        w, h = pic.size
        new_w, new_h = w//2, h//2
        new_pic = pic.resize((new_w, new_h), Image.Resampling.LANCZOS)
        new_pic.save(fpath + '/compressed_images' +
                     f"/compressed_image_{i+1:04d}" + image_ext,
                     optimize=True, quality=90)

    # Windows uses the backward slash (\), other systems use the forward slash (/)
    if platform.startswith('win'):
        print(f"The compressed images were saved in {fpath}\\compressed_images\n")
    else:
        print(f"The compressed images were saved in {fpath}/compressed_images\n")


###############################################

### Get user input

print('Make sure the images are named in order for the merging process.\n')

folder = input(r"""Type the folder name/path containing the images: """)
fpath = os.path.abspath(folder)
print()

if not os.path.exists(fpath):
    print(f"Error! Folder {fpath} not found!")
    print('Check if the folder path is correct.')
    exit(1)

pdf_name = input(r"""Type the name for the PDF file that will be generated: """)
if not pdf_name.endswith('.pdf'): pdf_name = pdf_name + '.pdf'
print()

image_ext = input('Type the extension of your images (e.g. png, jpg): ')
if not image_ext.startswith('.'): image_ext = '.' + image_ext
print()

###############################################

### Main script

# Creating the list with the paths of the image files
image_list = [f"{fpath}/{image}" for image in os.listdir(fpath)
              if image.endswith(image_ext)]
image_list.sort()

print('Compressing and saving images, please wait...\n')
compress_images(image_list, fpath)

# Creating a list with only the newly created compressed images
compressed = [f"{fpath}/compressed_images/{image}" for image in
              os.listdir(fpath + '/compressed_images')]
compressed.sort()

print('Creating the PDF file, please wait...\n')
pdf = FPDF()
for image in compressed:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)
    # 210 and 297 are the dimensions of an A4 size sheet.

# Save the pdf file
pdf.output(fpath + '/' + pdf_name)

# Windows uses backward slash (\), other systems use forward slash (/)
if platform.startswith('win'):
    print(f"Done. The PDF file was saved as {fpath}\\{pdf_name}.")
else:
    print(f"Done. The PDF file was saved as {fpath}/{pdf_name}.")

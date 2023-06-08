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


# This is a Python script to merge images into one PDF file

# All images need to be in the same folder, and have the same extension
# (e.g. all .png or all .jpg)

# Rename all images in (alphabetical or numeric) order for the merging process.

# Each image will be a page of the PDF file, with the size of an A4
# paper sheet in portrait mode, without margins.

# This script requires the fpdf or fpdf2 python package
# Installation example: 'pip install fpdf' or 'pip3 install fpdf'

######################################################

import os
from fpdf import FPDF

print('Make sure images are named in (alphabetical or numeric) order')
print('before proceeding.\n')

##### Get user input

folder = input("Type the folder name/path containing the images: ")
fpath = os.path.abspath(folder)
print()

# If folder doesn't exist, print error and exit
if not os.path.exists(fpath):
    print(f"Error! Folder {fpath} not found!")
    print('Check if the folder name/path is correct.')
    exit(1)

image_type = input('Type the extension of your images (e.g. png, jpg): ')
if not image_type.startswith('.'): image_type = '.' + image_type
print()

pdf_name = input("Type the name for the PDF file: ")
if not pdf_name.endswith('.pdf'): pdf_name = pdf_name + '.pdf'
print()

######################################################

###### Import images and generate the PDF file

# Create the list with the paths of the image files
image_list = [f"{fpath}/{image}" for image in os.listdir(fpath)
              if image.endswith(image_type)]
image_list.sort()

print('Please wait...\n')

# Create the PDF file and add the images
pdf = FPDF()
for image in image_list:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)
    # 210 and 297 are the dimensions in mm of an A4 size sheet.

# Save the pdf file
pdf.output(fpath + '/' + pdf_name)

print("Done. PDF file saved as:", os.path.join(fpath, pdf_name))

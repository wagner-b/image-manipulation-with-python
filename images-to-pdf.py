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


# Python script to merge images into one PDF file

# You need to put all images in a single folder, in the same directory
# in which this script will be executed.

# Rename all images in (alphabetical or numeric) order for the merging process.
# All images should be of the same extension (e.g. all png or all jpg)

# Each image will be a page of the PDF file, with the size of an A4
# paper sheet in portrait mode, without margins.

# You need to install the fpdf library before running this script
# Example: ' pip install fpdf ' or ' pip3 install fpdf '

###############################################

import os
from sys import platform
from fpdf import FPDF


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

    print('Please wait...')
    print()

    pdf = FPDF()
    for image in image_list:
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


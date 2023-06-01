# Image manipulation with Python
Each `.py` file in this repository is a simple Python script to either compress or change the transparency of an image file, or even to merge multiple image (or PDF) files into one PDF file. They all work independently from each other. I've tested them both on Windows and on Linux systems, so they should work regardless of which is your operating system.

In order to be able to run all these scrits, you need the Python packages `pillow` , `pypdf2`, and `fpdf` (or `fpdf2`) installed. Individual scripts require only one or two of these packages (indicated on the comments of the script itself). 

I find these scripts quite useful sometimes, especially if dealing with sensitive documents, when I'm not willing to upload them to a third-party server on the internet.

### compress-image.py
This script simply compresses (reduces) an image by half of its original size, and saves it with a different name.

### compress-images-to-pdf.py
This script compresses any amount of images, and generates a single PDF file with those compressed images (one image each page, portrait mode, A4 size sheet).

### images-to-pdf.py
This script generates a single PDF file out of any amount of images (one image each page, portrait mode, A4 size sheet).

### merge-pdfs.py
This script appends any amount of PDF files into a single PDF file, and saves it.

### white-to-transparency.py
This script opens an image, replaces the white color (or brighter colors, according to user input) with 100% transparency, and saves it with a different name.

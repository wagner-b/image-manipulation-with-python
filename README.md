# image-manipulation-with-python
Each `.py` file in this repository is a simple Python script to manipulate images and/or merge them in a PDF file, or even merge different PDF files in a single PDF file. They all work independently from each other. I tested them both on Windows and Linux, so they should work regardless of which is your operating system.

In order to be able to run all these scrits, you need the Python packages `pillow` , `fpdf` and `pypdf2` installed. Some scripts here do not require all 3 packages. The comments inside each script clearly indicate which package(s) is(are) required. 

All scripts here are free open-source software written by me. I'm sharing them here because I find them quite useful sometimes, especially if dealing with confidential or sensitive documents. If that's the case, maybe it isn't a good idea to send your data to a third-party server to manipulate it for you, since you can't be sure what it will do with your data. Since these scripts here are free and open-source software, you can look at the source code yourself, see that they aren't doing anything malicious with your data, and run them on your own machine.

# compress-image.py
This script simply compresses (or reduces) an image by half of its original size, and saves it with a different name.

# compress-images-to-pdf.py
This script compresses any amount of images, and generates a single PDF file with those compressed images (one image each page, portrait mode).

# images-to-pdf.py
This script generates a single PDF file out of any amount of images (one image each page, portrait mode).

# merge-pdfs.py
This script appends any amount of PDF files in a single PDF file, and saves it.

# white-to-transparency.py
This script opens an image, replaces the white color (or brighter colors, according to user input) with 100% transparency, and saves it with a different name.

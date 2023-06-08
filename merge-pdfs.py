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


# This is a Python script to merge any amount of pdf files into one pdf file
# To run this script, you need the python package 'pypdf2' installed

# All the pdf files you want to merge need to be inside the same folder
# Rename all pdf files in alphabetical or numeric order before running this script.

import os
from PyPDF2 import PdfMerger

print('Make sure the PDFs are named in order for the merging process.')
folder = input("Type the folder name/path with the PDF files: ")
fpath = os.path.abspath(folder)
print()

# Create the list with the paths of the PDF files
pdfs = [f"{fpath}/{pdf_file}" for pdf_file in os.listdir(fpath)
        if pdf_file.endswith('.pdf')]

# In case this script has already been executed, remove the merged pdf
for pdf in pdfs:
    if pdf.endswith('all_pdfs_merged.pdf'): pdfs.remove(pdf)

pdfs.sort()

# Append all PDFs into one
pdf_merger = PdfMerger()
for pdf_file in pdfs:
    pdf_merger.append(open(pdf_file, 'rb'))

# Save the final pdf file, with all pdfs merged
with open(f"{fpath}/all_pdfs_merged.pdf", 'wb') as pdf_final:
    pdf_merger.write(pdf_final)

print("Done. File saved as:", os.path.join(fpath, 'all_pdfs_merged.pdf'))

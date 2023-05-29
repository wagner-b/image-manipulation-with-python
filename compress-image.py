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


# This script resizes (to half the original size) and compresses an image file,
# while trying to maintain most of the original image quality.
# To run this script, you need the python package 'pillow' installed.

from PIL import Image

print('Type the exact name/path of the image, with extension (like .jpg or .png)')
img_file = input(r"Original image: ")
pic = Image.open(img_file)

w, h = pic.size
new_w = int(w//2)
new_h = int(h//2)

print()
print('Type the name/path for the new compressed image, with the extension')
new_img_name = input(r"New image: ")

# Resize the image, using an antialiasing for better quality
new_pic = pic.resize((new_w, new_h), Image.Resampling.LANCZOS)

# Save the image with optimization and 98% of quality
new_pic.save(new_img_name, optimize = True, quality = 98)

pic.close()
new_pic.close()

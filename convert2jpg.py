import os
import sys
from PIL import Image

# takes system args terminal
# input type, is it any kind of image file
# file conversion, what is the compression ratio
# standard  ISO/IEC 10918
# Go Georgia Dawgs!
# for the email blast SMTP bounce backs, check the failure rate and bounce reason
# from the receiving server

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        im = Image.open(sys.argv[1])
        target_name = sys.argv[1] + ".jpg"
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
        print("Saved as " + target_name)
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: convert2jpg.py <file>")

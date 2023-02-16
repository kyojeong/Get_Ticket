# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:23:33 2023

@author: user
"""

import ddddocr

ocr = ddddocr.DdddOcr()
with open('1.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)

print(res)
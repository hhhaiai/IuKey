#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Copyright © 2021 sanbo Inc. All rights reserved.
@Description: 
@Version: 1.0
@Create: 2021-01-15 11:49:11
@author: sanbo

'''
import base64

def file_to_base64file(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()


def file_to_base64(file):
    with open(file, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)
        return base64_data.decode()

# print(file_to_base64("./data/JetBrains 2020.3.x更新1月7日 全家桶，激活方式.zip"))

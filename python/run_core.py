#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Copyright © 2021 sanbo Inc. All rights reserved.
@Description: 
@Version: 1.0
@Create: 2021-01-15 11:49:23
@author: sanbo

'''
"""
蓝奏网盘 API，封装了对蓝奏云的各种操作，解除了上传格式、大小限制
"""
import base64
import os
import time
from lanzou.api import LanZouCloud
from upload_2_github import *
from utils import *


def file_to_base64(file):
    with open(file, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)
        return base64_data.decode()


def get_file_name(file_path):
    (filepath, tempfilename) = os.path.split(file_path)
    # print("filepath: {}".format(filepath))
    # print("tempfilename: {}".format(tempfilename))
    # (filename,extension) = os.path.splitext(file_path)
    # print("filename: {}".format(filename))
    # print("extension: {}".format(extension))
    return tempfilename


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    if os.path.exists(file_name + ".download"):
        os.remove(file_name + ".download")


def clean_dir():
    lp_dir = os.getcwd()
    for file_name in os.listdir(lp_dir):
        if file_name.endswith(".zip"):
            remove_file(file_name)
    pass


def get_zip_name(loop_dirs):
    # print("\tloop_dirs: {}---{}".format(loop_dirs,os.listdir(loop_dirs)))
    for file_list in os.listdir(loop_dirs):
        if file_list.endswith(".zip"):
            # print(file_list)
            if file_list.endswith("/"):
                conn = ""
            else:
                conn = "/"
            # print("\tfile_list:--{}".format(file_list))
            path = loop_dirs + conn + file_list
            return path
    return ""


if __name__ == '__main__':
    lanzou = LanZouCloud()
    print("Setup 0: Clean work space...")
    clean_dir()
    down_url = ''
    share_url = 'https://souyunku.lanzoux.com/b0aki3kna'
    if is_folder_url(share_url):
        folderDetail = lanzou.get_folder_info_by_url(share_url)
        print(folderDetail)
        fdlist = folderDetail.files
        lle = len(fdlist)
        # print("len: {} ; fdList: {}; type: {}".format(str(lle), fdlist, type(fdlist)))
        if lle > 1:
            for index in range(lle):
                # print("len>1. 含全家桶: fdlist[{}]{}".format(index, fdlist[index]))
                fileInFolder = fdlist[index]
                # print("len>1. fileInFolder: {}".format(fileInFolder))
                pname = fileInFolder.name
                if "全家桶" in pname:
                    # print("len>1. 含全家桶: {}".format(pname))
                    down_url = fileInFolder.url
                    break
        elif lle == 1:
            fileInFolder = fdlist[0]
            # print("len=1.{}".format(fileInFolder))
            down_url = fileInFolder.url
        else:
            down_url = ""
            # print("other.down_url is null!")
            pass
    print("Setup 1: down file： [{}]".format(down_url))

    code = lanzou.down_file_by_url(down_url, '',
                                   os.getcwd(), overwrite=True)
    print("Setup 2: get file path")

    f_path = get_zip_name(os.getcwd())
    print("\tf_path: {}".format(f_path))
    f_name = get_file_name(f_path)

    final_fn = "{}.zip".format(str(time.strftime("%y%m%d-%H%M%S")))
    os.rename(f_name, final_fn)

    print("\tfile_path: [{}]".format(final_fn))
    try:
        print("Setup 3: upload file to github")
        update_filef(final_fn)
    finally:
        print("Setup 4: clean file in dir. after 5 min")
        clean_dir()
        pass

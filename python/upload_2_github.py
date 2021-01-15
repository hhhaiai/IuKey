#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Copyright © 2021 sanbo Inc. All rights reserved.
@Description:
@Version: 1.0
@Create: 2021-01-15 12:33:23
@author: sanbo

'''
import json
import urllib

import requests

import file_2_base64

token = ""
user = "hhhaiai"
repo = "idea_register"
path = ""


# 上传文件
def update_filef(filename=''):
    try:
        url = "https://api.github.com/repos/{}/{}/contents/{}{}".format(user, repo, path, filename)
        # file_data=open_file(filename)
        headers = {"Authorization": "token " + token}
        content = file_2_base64.file_to_base64(filename)
        # print(content)
        # print("content len: {}".format(len(content)))
        data = {
            # "committer": {
            #     "name": "sanbo",
            #     "email": "sanbo.xyz@gmail.com"
            # },
            "message": "Upload by xyz",
            "content": content
        }
        data = json.dumps(data)
        req = requests.put(url=url, data=data, headers=headers)
        req.encoding = "utf-8"
        re_data = json.loads(req.text)
        # print("re_data: {}".format(re_data))
        down_url = re_data['content']['download_url']
        sha = re_data['content']['sha']
        print("\tupload file sha: " + sha)
        # 在国内默认的down_url可能会无法访问，因此使用CDN访问
        cdn_url = "https://cdn.jsdelivr.net/gh/{}/{}/{}{}".format(user, repo, path, urllib.parse.quote(filename))
        print("\tChina down path: {}".format(cdn_url))
        print("\tGithub download_url: " + down_url)
    except  Exception as e:
        print('Reason:', e)
        pass

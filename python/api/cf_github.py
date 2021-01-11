import json
# 文件名
import os
import requests
import urllib

from api import B64s

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
        content = B64s.file_to_base64(filename)
        # print(content)
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
    except:
        pass
    try:
        os.remove(filename)
    except:
        pass

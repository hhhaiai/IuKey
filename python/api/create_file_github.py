import json, requests, base64
from B64s import *

# 文件名
from api import B64s

file_name = "JetBrains 2020.3.x更新1月7日 全家桶，激活方式.zip"
file_path = "./data/" + file_name
token = "2d313dee6c23a8dcaa5f13fecfd39cfd98a2fb47"
user = "hhhaiai"
repo = "idea_register"
path = ""


# 上传文件
def uf(filename='', token="", url=""):
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
    print(re_data)
    down_url = re_data['content']['download_url']
    sha = re_data['content']['sha']
    print("file sha: " + sha)
    # 在国内默认的down_url可能会无法访问，因此使用CDN访问
    print("China down path: https://cdn.jsdelivr.net/gh/{}/{}/{}{}".format(user, repo, path, file_name))
    print("Github download_url: " + down_url)


if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/contents/{}{}".format(user, repo, path, file_name)  # 用户名、库名、路径
    uf(file_path, token, url)

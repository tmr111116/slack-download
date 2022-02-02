from datetime import datetime
import os
import requests
import json
import os.path

def files_list(files_dir, token, page):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://slack.com/api/files.list?pretty=1&page={page}"
    result = requests.get(url, headers=headers)
    files_json = result.text
    with open(f"{files_dir}/_index_p{page}.json", 'w') as f:
      f.write(files_json)
    data = json.loads(files_json)
    return data

def download_files(files_dir, token, files):
    headers = {"Authorization": f"Bearer {token}"}

    for file in files:
        file_name = f"{files_dir}/{file['id']}_{file['name']}"
        print(f"dowonload '{file_name}'")
        if not "url_private_download" in file:
            print("url_private_download がないのでスキップ")
            print(json.dumps(file))
            continue
        file_url = file["url_private_download"]
        # 同じファイル名の物があると上書きされてしまうため存在を確認する
        if os.path.exists(file_name):
            print("重複しました")
            continue
        response = requests.get(file_url, headers=headers)
        with open(file_name, 'wb') as f:
            # ファイルを保存する
            f.write(response.content)

def fileDownload():
    TOKEN = os.environ["TOKEN"]

    dir_name = datetime.now().isoformat(' ', 'seconds')
    files_dir = f"download_files/{dir_name}"
    os.mkdir(files_dir)

    pages = 999
    page = 1
    while page <= pages:
      print(f"file.list page {page}")
      data = files_list(files_dir, TOKEN, page)
      print(json.dumps(data["paging"]))
      pages = data["paging"]["pages"]
      page += 1
      download_files(files_dir, TOKEN, data["files"])

if __name__ == '__main__':
    fileDownload()

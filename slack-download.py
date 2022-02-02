import requests
import json
import os.path

def fileDownload():
    print('fileDownload')

    # 大文字の所は自分の欲しいファイルなどに変換
    # ts_from, ts_toなどはUnixTimeで記述
    url = "https://slack.com/api/files.list?token=LEGACYTOKEN&channel=CHANNELID&ts_from=1535727600&ts_to=1538319600&user=USERID&pretty=1"

    result = requests.get(url)

    data = json.loads(result.text)

    # ファイルをダウンロードするためにヘッダーが必要
    headers = {'Authorization': 'Bearer '+LEGACYTOKEN}
    count = 0
    for file in data["files"]:
        file_url = file["url_private_download"]
        file_title = file["title"]

        # 同じファイル名の物があると上書きされてしまうため存在を確認する
        if os.path.exists(file_title):
            print("重複しました")
            count = count + 1
            file_title = file_title + str(count)
        response = requests.get(file_url, headers=headers)
        with open(file_title, 'wb') as f:
            # ファイルを保存する  
            f.write(response.content)

if __name__ == '__main__':
    fileDownload()

import requests
import json
import os.path

def fileDownload():
    print('fileDownloading...')
    # レガシートークン( 参考：https://api.slack.com/custom-integrations/legacy-tokens )
    LEGACYTOKEN = "ここにいれてね"

    # UnixTimeで記述, 入れなければ全期間( 参考：https://tool.konisimple.net/date/unixtime )
    DATE_FROM = ""
    DATE_TO = ""

    url = "https://slack.com/api/files.list?token=" + LEGACYTOKEN + "&ts_from=" + DATE_FROM + "&ts_to=" + DATE_TO + "&pretty=1"

    result = requests.get(url)

    data = json.loads(result.text)

    # ファイルをダウンロードするためのヘッダー
    headers = {'Authorization': 'Bearer ' + LEGACYTOKEN}
    count = 0
    for file in data["files"]:
        file_name = file["name"]
        if not "url_private_download" in file:
            continue
        file_url = file["url_private_download"]
        # 同じファイル名の物があると上書きされてしまうため存在を確認する
        if os.path.exists(file_name):
            print("重複しました")
            count = count + 1
            insert_point = file_name.find(".")
            insert_string = "(" + str(count) + ")"
            file_name = '{0}{1}{2}'.format(file_name[:insert_point], insert_string, file_name[insert_point:])
        response = requests.get(file_url, headers=headers)
        with open(file_name, 'wb') as f:
            # ファイルを保存する
            f.write(response.content)

if __name__ == '__main__':
    fileDownload()

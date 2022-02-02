# slack-download

https://qiita.com/yuma1217/items/86cf9d852a2b83fa7296
https://blog.nainaism.com/slack-download/

1. slack app を作る。
1. workspace にインストールする。
1. Bot Token Scopes に `files:read`, `channels:join`, `channels:read` を追加する。
1. Bot User OAuth Token を `.env` に `TOKEN=xoxb-…` で設定する。
1. どこかのチャンネルに join させないとファイルのリストが取れないっぽい。
    - https://stackoverflow.com/a/65646237
    - https://api.slack.com/methods/conversations.join/test でやると楽。
1. `docker-compose up`

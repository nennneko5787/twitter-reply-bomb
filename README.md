# Twitter-Reply-Bomb

ムカつくユーザーにリプライ爆弾を送ろう。

> [!WARNING]
> このツールを使用して起きた損害について作者の[nennneko5787](https://x.com/Fng1Bot)は一切の責任を負いません。

> [!CAUTION]
> このツールを使用するためには Twitter アカウントを用意する必要があります。  
> あなたの大事なアカウントを凍結させないためにも、いつも使っていないアカウントまたは新規に作ったアカウントでツールを実行することを**強く**推奨します。

## How to use this tool

### 必要なもの

- PC
- git (git を使用してダウンロードする場合)
- Python 3.8 以降

### インストール

#### git を使用してダウンロード

git を使用し、このリポジトリをクローンします。

```
git clone https://github.com/nennneko5787/twitter-reply-bomb.git
```

その後、ディレクトリを移動します。

```
cd twitter-reply-bomb
```

#### zip からダウンロード

https://github.com/nennneko5787/twitter-reply-bomb/archive/refs/heads/main.zip から、最新のソースコードをダウンロードします。  
解凍して、main.py が入っているフォルダまで移動します。

#### 仮想環境(venv)の作成

仮想環境を作成することを**強く**推奨します。

```
(Windows)
py -m venv venv
(Mac / Linux)
python3 -m venv venv
```

#### 依存関係のインストール

```
(Windows)
py -m pip install -U -r requirements.txt
(Mac / Linux)
python3 -m pip install -U -r requirements.txt
```

#### `credentials.json` ファイルの作成

スパムをするアカウントの情報が入った`credentials.json`ファイルを作成します。  
これは、以下のような書式になります。

```json
[
  {
    "enable": true,
    "username": "<ユーザー名>",
    "email": "<メールアドレス>",
    "password": "<パスワード>"
  }
]
```

`credentials.json` ファイルの書式は、[このドキュメント](credentials.json.md) にて解説しています。

#### `settings.json` ファイルの変更

設定ファイルである`settings.json`ファイルを変更します。  
`settings.json` ファイルの書式は、[このドキュメント](settings.json.md) にて解説しています。

#### 実行

```
(Windows)
py main.py
(Mac / Linux)
python3 main.py
```

`URL of the tweet you want to send a reply cannon: `と出たらリプライ爆弾を送りたいツイートの URL を入力してください。Enter キーで次に進みます。  
その後、`text(n): `と聞かれるので好きな文字を入力してください。Enter キーで次に進みます。  
`Ready!`と出たら準備完了です。  
`Ctrl`キーと`C`キーを押すと終了します。

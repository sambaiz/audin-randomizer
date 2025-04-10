# オーディンの祝祭の島 ランダマイザ

このアプリケーションは、オーディンの祝祭の島から8つの島をランダムに選ぶStreamlitアプリケーションです。
フエゴ島は必ず含まれます。

## 必要条件

- Python 3.7以上
- pip（Pythonパッケージマネージャー）

## インストール方法

1. リポジトリをクローンまたはダウンロードします。

2. 必要なパッケージをインストールします：
```bash
pip install -r requirements.txt
```

## 使い方

1. 以下のコマンドでアプリケーションを起動します：
```bash
streamlit run app.py
```

2. ブラウザが自動的に開き、アプリケーションが表示されます。

3. 「島をランダマイズ」ボタンをクリックすると、8つの島がランダムに選ばれます。
   - フエゴ島は必ず含まれます
   - 残りの7つの島は他の島からランダムに選ばれます

## 機能

- シンプルで使いやすいインターフェース
- ワンクリックでランダマイズ
- フエゴ島を必ず含む仕様
- モバイルフレンドリーなデザイン 
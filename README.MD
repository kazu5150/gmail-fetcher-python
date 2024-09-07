# Gmail-Dify Integration Project

このプロジェクトは、Gmailから特定の条件に合致するメールを取得し、その内容をDify APIを使用して解析するPythonスクリプトです。解析結果は構造化されたデータとして出力されます。

## 機能

- Gmailから特定の件名を持つメールを検索・取得
- 取得したメール本文をDify APIに送信して解析
- 解析結果（日付、アイテム、数量、配送先情報など）を構造化して表示

## ファイル構成

```
gmail-dify-integration/
│
├── src/
│   └── gmail_fetcher.py   # Gmail APIを使用してメールを取得する機能を実装
│
├── main.py                # メインスクリプト。プログラムのエントリーポイント
├── .env                   # 環境変数設定ファイル（gitignoreに含める）
├── .env.example           # 環境変数の例示ファイル
├── requirements.txt       # 必要なPythonパッケージのリスト
├── credentials.json       # Google OAuth認証情報（gitignoreに含める）
├── .gitignore             # Gitが無視すべきファイルのリスト
└── README.md              # プロジェクトの説明書（このファイル）
```

## 前提条件

- Python 3.6以上
- Google Cloud Platformのプロジェクト（Gmail API有効化済み）
- Dify APIのアカウントとAPIキー

## Google Cloud Platform (GCP) の設定

1. [Google Cloud Console](https://console.cloud.google.com/) にアクセスし、Googleアカウントでログインします。

2. 新しいプロジェクトを作成します：
   - 画面上部のプロジェクト選択ドロップダウンをクリック
   - 「新しいプロジェクト」を選択
   - プロジェクト名を入力し、「作成」をクリック

3. Gmail API を有効化します：
   - 左側のメニューから「APIとサービス」>「ライブラリ」を選択
   - 検索バーに「Gmail API」と入力し、検索結果から選択
   - 「有効にする」ボタンをクリック

4. OAuth 同意画面を設定します：
   - 左側のメニューから「APIとサービス」>「OAuth同意画面」を選択
   - ユーザータイプとして「外部」を選択し、「作成」をクリック
   - アプリ名、ユーザーサポートメール、デベロッパーの連絡先情報を入力
   - 「スコープを追加または削除」をクリックし、`https://www.googleapis.com/auth/gmail.readonly` を追加
   - 画面の指示に従って設定を完了

5. OAuth 2.0 クライアント ID を作成します：
   - 左側のメニューから「APIとサービス」>「認証情報」を選択
   - 「認証情報を作成」>「OAuth クライアント ID」をクリック
   - アプリケーションの種類として「デスクトップアプリ」を選択
   - 名前を入力し、「作成」をクリック
   - 作成されたクライアント ID とクライアントシークレットが表示されます
   - 「JSONをダウンロード」ボタンをクリックし、ファイルをダウンロード

6. ダウンロードしたJSONファイルの名前を `credentials.json` に変更し、プロジェクトのルートディレクトリに配置します。


## Difyワークフローappの作成

![Difyワークフロー](image/dify_workflow.png)


## セットアップ

1. リポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/gmail-dify-integration.git
   cd gmail-dify-integration
   ```

2. 仮想環境を作成し、アクティベートします：
   ```
   python -m venv venv
   source venv/bin/activate  # Unix or MacOS
   venv\Scripts\activate  # Windows
   ```

3. 必要なパッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

4. `.env.example`ファイルを`.env`にコピーし、必要な情報を入力します：
   ```
   cp .env.example .env
   ```
   そして、`.env`ファイルを編集して以下の環境変数を設定します：
   ```
   GMAIL_QUERY_STRING=Your Gmail Search Query
   MAX_RESULTS=10
   DIFY_API_URL=https://api.dify.ai/v1/workflows/run
   DIFY_API_KEY=Your Dify API Key
   ```

5. Google Cloud Consoleから認証情報（OAuth 2.0クライアントID）をダウンロードし、`credentials.json`としてプロジェクトのルートディレクトリに保存します。

## 使用方法

1. スクリプトを実行します：
   ```
   python main.py
   ```

2. 初回実行時は、Googleアカウントの認証を求められます。ブラウザでの認証を完了してください。

3. スクリプトは指定された条件に合致するGmailメッセージを取得し、Dify APIを使用して解析します。

4. 解析結果が構造化されたフォーマットで表示されます。

## 出力例

```
Subject: 重要な配送情報
From: sender@example.com
Body: メール本文の一部...

Dify Response:
日付: 2024/09/06
アイテム: ロゴ封筒（角2）
数量: 100
配送先名: 所沢市役所
郵便番号: 359-xxxx
配送先住所: 埼玉県 所沢市xxxxxxxxxx
配送先電話番号: 04-xxx-xxxx

--------------------
```

## 注意事項

- このスクリプトは、Gmail APIとDify APIの利用制限に従います。大量のリクエストを送信する場合は、各サービスの利用規約を確認してください。
- `credentials.json`と`.env`ファイルには機密情報が含まれているため、Gitリポジトリにコミットしないよう注意してください。

## トラブルシューティング

- 認証エラーが発生した場合は、`credentials.json`の設定と、Google Cloud Consoleでの権限設定を確認してください。
- Dify APIのエラーが発生した場合は、APIキーと設定を確認してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## 貢献

バグ報告や機能リクエストは、GitHubのIssueで受け付けています。プルリクエストも歓迎します。







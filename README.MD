# Gmail Fetcher

Gmail Fetcher は Python を使用して、特定の文字列を件名に含む Gmail メッセージを取得するスクリプトです。

## 機能

- Gmail API を使用して特定の件名を持つメールを検索
- 環境変数を使用して検索クエリと取得するメッセージ数をカスタマイズ可能
- 取得したメールの件名、送信者、スニペットを表示

## フォルダ構造

```
gmail-fetcher/
│
├── src/
│   └── gmail_fetcher.py      # メインのPythonスクリプト
│
├── .env.example              # 環境変数の例
├── .env                      # 実際の環境変数（.gitignoreに追加）
├── .gitignore                # Gitが無視するファイルの設定
├── README.md                 # プロジェクトの説明書（このファイル）
├── requirements.txt          # 必要なPythonパッケージのリスト
├── credentials.json          # Google Cloud Platformの認証情報（.gitignoreに追加）
└── token.pickle              # アクセストークン（自動生成、.gitignoreに追加）
```

## 前提条件

- Python 3.6 以上
- Google Cloud Platform のプロジェクト
- Gmail API の有効化
- OAuth 2.0 クライアント ID の作成


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


## セットアップ

1. このリポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/gmail-fetcher.git
   cd gmail-fetcher
   ```

2. 仮想環境を作成し、アクティベートします：
   ```
   python -m venv myenv
   source myenv/bin/activate  # Unix or MacOS
   myenv\Scripts\activate  # Windows
   ```

3. 必要なパッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

4. `.env` ファイルを作成します：
   - リポジトリ内の `.env.example` ファイルをコピーして `.env` という名前で保存します：
     ```
     cp .env.example .env
     ```
   - `.env` ファイルを開き、必要に応じて値を変更します：
     ```
     GMAIL_QUERY_STRING=重要
     MAX_RESULTS=10
     ```

5. Google Cloud Platform から取得した `credentials.json` ファイルをプロジェクトのルートディレクトリに配置します。

## 環境変数の設定

`.env` ファイルは、アプリケーションの設定を環境変数として保存するために使用されます。以下の変数を設定できます：

- `GMAIL_QUERY_STRING`: Gmail の検索クエリ文字列（デフォルト: '重要'）
- `MAX_RESULTS`: 取得するメッセージの最大数（デフォルト: 10）

注意: `.env` ファイルには機密情報が含まれる可能性があるため、このファイルは `.gitignore` に追加されており、リポジトリにコミットされません。代わりに、`.env.example` ファイルがテンプレートとして提供されています。

## 使用方法

スクリプトを実行するには、以下のコマンドを使用します：

```
python src/gmail_fetcher.py
```

初回実行時には、ブラウザが開いて Gmail アカウントへのアクセス許可を求められます。許可すると、アクセストークンが `token.pickle` ファイルに保存され、以降の実行時に再利用されます。

## カスタマイズ

環境変数を変更することで、スクリプトの動作をカスタマイズできます：

- 検索クエリを変更するには、`.env` ファイルの `GMAIL_QUERY_STRING` の値を変更します。
- 取得するメッセージの数を変更するには、`.env` ファイルの `MAX_RESULTS` の値を変更します。

変更後は、スクリプトを再実行して新しい設定を適用します。

## トラブルシューティング

[前回の内容をそのまま維持]

## 注意事項

- このスクリプトは個人的な使用やテスト目的で作成されています。大量のリクエストを送信しないよう注意してください。
- `credentials.json`、`token.pickle`、`.env` ファイルには機密情報が含まれているため、`.gitignore` に追加されていることを確認し、公開リポジトリにアップロードしないでください。

## ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) の下で公開されています。

## 貢献

問題の報告や改善の提案は、GitHub の Issue 機能をご利用ください。プルリクエストも歓迎します。







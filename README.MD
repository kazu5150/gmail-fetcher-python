# Gmail Fetcher

Gmail Fetcher は Python を使用して、特定の文字列を件名に含む Gmail メッセージを取得するスクリプトです。

## 機能

- Gmail API を使用して特定の件名を持つメールを検索
- 環境変数を使用して検索クエリと取得するメッセージ数をカスタマイズ可能
- 取得したメールの件名、送信者、スニペットを表示

## 前提条件

- Python 3.6 以上
- Google Cloud Platform のプロジェクト
- Gmail API の有効化
- OAuth 2.0 クライアント ID の作成

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

4. Google Cloud Console から OAuth 2.0 クライアント ID をダウンロードし、`credentials.json` としてプロジェクトのルートディレクトリに保存します。

5. `.env` ファイルを作成し、以下の内容を追加します（必要に応じて値を変更してください）：
   ```
   GMAIL_QUERY_STRING=重要
   MAX_RESULTS=10
   ```

## 使用方法

スクリプトを実行するには、以下のコマンドを使用します：

```
python src/gmail_fetcher.py
```

初回実行時には、ブラウザが開いて Gmail アカウントへのアクセス許可を求められます。許可すると、アクセストークンが `token.pickle` ファイルに保存され、以降の実行時に再利用されます。

## カスタマイズ

- 検索クエリを変更するには、`.env` ファイルの `GMAIL_QUERY_STRING` の値を変更します。
- 取得するメッセージの数を変更するには、`.env` ファイルの `MAX_RESULTS` の値を変更します。

## 注意事項

- このスクリプトは個人的な使用やテスト目的で作成されています。大量のリクエストを送信しないよう注意してください。
- `credentials.json` と `token.pickle` には機密情報が含まれているため、`.gitignore` に追加されていることを確認し、公開リポジトリにアップロードしないでください。

## ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) の下で公開されています。

## 貢献

問題の報告や改善の提案は、GitHub の Issue 機能をご利用ください。プルリクエストも歓迎します。

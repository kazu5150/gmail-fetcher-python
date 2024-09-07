import os
from dotenv import load_dotenv
from src.gmail_fetcher import get_gmail_service, list_messages_with_title_and_body

# 環境変数を読み込む
load_dotenv()

if __name__ == '__main__':
    service = get_gmail_service()
    title_query = os.getenv('GMAIL_QUERY_STRING', '重要')  # デフォルト値として '重要' を設定
    max_results = int(os.getenv('MAX_RESULTS', 10))  # デフォルト値として 10 を設定
    list_messages_with_title_and_body(service, title_query, max_results=max_results)
    
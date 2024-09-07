import os
import sys
import requests
from dotenv import load_dotenv
from src.gmail_fetcher import get_gmail_service, list_messages_with_title_and_body

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# 環境変数を読み込む
load_dotenv()

# Dify API の設定
DIFY_API_URL = os.getenv('DIFY_API_URL', 'https://api.dify.ai/v1/workflows/run')
DIFY_API_KEY = os.getenv('DIFY_API_KEY')


def send_to_dify(body, max_length=800):
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }

    truncated_body = body[:max_length]

    payload = {
        "inputs": {"query": truncated_body},
        "response_mode": "blocking",
        "user": "example@gmail.com"
    }

    try:
        response = requests.post(DIFY_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending request to Dify: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")
        return None


def parse_dify_response(response):
    if 'data' in response and 'outputs' in response['data']:
        outputs = response['data']['outputs']
        return f"""
日付: {outputs.get('date', 'N/A')}
アイテム: {outputs.get('item', 'N/A')}
数量: {outputs.get('item_number', 'N/A')}
配送先名: {outputs.get('delivery_place_name', 'N/A')}
郵便番号: {outputs.get('postal_number', 'N/A')}
配送先住所: {outputs.get('delvery_address', 'N/A')}
配送先電話番号: {outputs.get('delivery_place_phone', 'N/A')}
"""
    return "Unable to parse Dify response"


def process_gmail_messages(service, title_query, max_results):
    messages = list_messages_with_title_and_body(service, title_query, max_results=max_results)

    for msg in messages:
        print(f"Subject: {msg['subject']}")
        print(f"From: {msg['sender']}")
        print(f"Body: {msg['body'][:600]}...")  # 最初の600文字のみ表示

        # Dify にメール本文を送信（800文字に制限）
        dify_response = send_to_dify(msg['body'])
        if dify_response:
            print("Dify Response:")
            parsed_response = parse_dify_response(dify_response)
            print(parsed_response)
        else:
            print("Failed to get response from Dify")

        print("--------------------")


if __name__ == '__main__':
    service = get_gmail_service()
    title_query = os.getenv('GMAIL_QUERY_STRING', '重要')  # デフォルト値として '重要' を設定
    max_results = int(os.getenv('MAX_RESULTS', 10))  # デフォルト値として 10 を設定

    process_gmail_messages(service, title_query, max_results)

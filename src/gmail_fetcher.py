from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
import base64
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# 環境変数を読み込む
load_dotenv()

# 必要なスコープを設定
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    service = build('gmail', 'v1', credentials=creds)
    return service


def list_messages_with_title(service, title_query, user_id='me', max_results=10):
    try:
        query = f"subject:{title_query}"
        response = service.users().messages().list(userId=user_id, q=query, maxResults=max_results).execute()
        messages = response.get('messages', [])
        
        if not messages:
            print(f"No messages found with '{title_query}' in the title")
            return
        
        print(f"Messages with '{title_query}' in the title:")
        for message in messages:
            msg = service.users().messages().get(userId=user_id, id=message['id']).execute()
            
            # メールの件名と送信者を取得
            subject = ""
            sender = ""
            for header in msg['payload']['headers']:
                if header['name'] == 'Subject':
                    subject = header['value']
                elif header['name'] == 'From':
                    sender = header['value']
                if subject and sender:
                    break
            
            # メールの本文を取得（プレーンテキストの場合）
            if 'data' in msg['payload']['body']:
                body = base64.urlsafe_b64decode(msg['payload']['body']['data']).decode('utf-8')
            else:
                body = "Body could not be decoded"
            
            print(f"Subject: {subject}")
            print(f"From: {sender}")
            print(f"Snippet: {msg['snippet']}")
            print("--------------------")
    
    except Exception as error:
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    service = get_gmail_service()
    title_query = os.getenv('GMAIL_QUERY_STRING', '【ゆうちょデビット】')  # デフォルト値として '【ゆうちょデビット】' を設定
    max_results = int(os.getenv('MAX_RESULTS', 10))  # デフォルト値として 10 を設定
    list_messages_with_title(service, title_query, max_results=max_results)

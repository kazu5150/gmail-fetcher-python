from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
import base64
from email.header import decode_header

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

def decode_subject(subject):
    decoded_subject, encoding = decode_header(subject)[0]
    if isinstance(decoded_subject, bytes):
        return decoded_subject.decode(encoding or 'utf-8')
    return decoded_subject

def get_message_body(message):
    if 'payload' not in message:
        return "Message payload not found"

    if 'body' in message['payload']:
        if 'data' in message['payload']['body']:
            return base64.urlsafe_b64decode(message['payload']['body']['data']).decode('utf-8')
    
    if 'parts' in message['payload']:
        for part in message['payload']['parts']:
            if part['mimeType'] == 'text/plain':
                if 'data' in part['body']:
                    return base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
    
    return "Body could not be decoded"

def list_messages_with_title_and_body(service, title_query, user_id='me', max_results=10):
    try:
        query = f"subject:{title_query}"
        response = service.users().messages().list(userId=user_id, q=query, maxResults=max_results).execute()
        messages = response.get('messages', [])
        
        if not messages:
            print(f"No messages found with '{title_query}' in the title")
            return
        
        print(f"Messages with '{title_query}' in the title:")
        for message in messages:
            msg = service.users().messages().get(userId=user_id, id=message['id'], format='full').execute()
            
            # メールの件名と送信者を取得
            subject = ""
            sender = ""
            for header in msg['payload']['headers']:
                if header['name'] == 'Subject':
                    subject = decode_subject(header['value'])
                elif header['name'] == 'From':
                    sender = header['value']
                if subject and sender:
                    break
            
            # メールの本文を取得
            body = get_message_body(msg)
            
            print(f"Subject: {subject}")
            print(f"From: {sender}")
            print(f"Body: {body[:500]}...")  # 最初の500文字のみ表示
            print("--------------------")
    
    except Exception as error:
        print(f'An error occurred: {error}')
        
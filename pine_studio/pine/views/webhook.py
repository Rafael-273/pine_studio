import json
import time
import requests
from django.http import JsonResponse
from django.views import View
from django.conf import settings
import hashlib


class MessengerWebhook(View):
    def get(self, request, *args, **kwargs):
        challenge = request.GET.get('hub.challenge')
        if challenge:
            return JsonResponse({'hub.challenge': challenge})
        return JsonResponse({'status': 'invalid'}, status=400)

    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        
        for entry in payload.get('entry', []):
            for messaging_event in entry.get('messaging', []):
                sender_id = messaging_event['sender']['id']
                message_text = messaging_event.get('message', {}).get('text')
                
                if message_text:
                    self.process_message(sender_id, message_text)
                    self.send_event_to_facebook(sender_id, message_text)

        return JsonResponse({'status': 'ok'})

    def process_message(self, sender_id, message_text):
        response_text = f"Você disse: {message_text}"
        self.send_message(sender_id, response_text)

    def send_message(self, recipient_id, message_text):
        url = f'https://graph.facebook.com/v13.0/me/messages?access_token={settings.FACEBOOK_PAGE_ACCESS_TOKEN}'
        headers = {'Content-Type': 'application/json'}
        data = {
            'recipient': {'id': recipient_id},
            'message': {'text': message_text}
        }
        
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def send_event_to_facebook(self, sender_id, message_text):
        hashed_email = hashlib.sha256(sender_id.encode('utf-8')).hexdigest()

        event_data = {
            "data": [
                {
                    "event_name": "Purchase",
                    "event_time": int(time.time()),
                    "action_source": "website",
                    "user_data": {
                        "em": [hashed_email],
                    },
                    "custom_data": {
                        "currency": "USD",
                        "value": 142.52
                    },
                    "original_event_data": {
                        "event_name": "Purchase",
                        "event_time": int(time.time())
                    }
                }
            ]
        }

        url = f'https://graph.facebook.com/v13.0/{settings.FACEBOOK_PIXEL_ID}/events?access_token={settings.FACEBOOK_PAGE_ACCESS_TOKEN}'

        response = requests.post(url, headers={'Content-Type': 'application/json'}, json=event_data)

        if response.status_code == 200:
            print("Evento enviado com sucesso!")
        else:
            print(f"Falha ao enviar evento: {response.status_code} - {response.text}")

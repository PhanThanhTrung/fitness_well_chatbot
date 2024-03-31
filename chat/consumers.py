import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .chatbot import Assistant
class ChatConsumer(WebsocketConsumer):
    _bot = Assistant()
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self._bot.talk_to_assistant(input_text=text_data_json["text"])
        get_event = {
                "type": "chat_message",
                "text": {"msg": text_data_json["text"], "source": "user"},
            }
        self.chat_message(event=get_event)

        output = self._bot.get_assistant_response()
        send_event = {
            "type": "chat.message",
            "text": {"msg": output, "source": "bot"},
        }
        self.chat_message(event=send_event)

    def chat_message(self, event):
        text = event["text"]
        self.send(text_data=json.dumps({"text": text}))
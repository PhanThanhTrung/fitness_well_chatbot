import json

from channels.generic.websocket import WebsocketConsumer
from .chatbot import Assistant
import markdown
class ChatConsumer(WebsocketConsumer):
    _bot = Assistant()
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if len(text_data_json["text"])==0:
            return
        else:
            get_event = {
                    "type": "chat_message",
                    "text": {"msg": text_data_json["text"], "source": "user"},
                }
            self._bot.talk_to_assistant(input_text=text_data_json["text"])
            self.chat_message(event=get_event)

            output = self._bot.get_assistant_response()
            output_html = markdown.markdown(output)
            output_html = output_html.replace('\n', '<br>') # Monkey patching to completely convert markdown string to html
            send_event = {
                "type": "chat.message",
                "text": {"msg": output_html, "source": "bot"},
            }
            self.chat_message(event=send_event)

    def chat_message(self, event):
        text = event["text"]
        self.send(text_data=json.dumps({"text": text}))
import json

from channels.generic.websocket import WebsocketConsumer
from .chatbot import Assistant
import markdown
import pandas as pd
import os
class ChatConsumer(WebsocketConsumer):
    _bot = Assistant()
    _chat_history = []
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
            self._save_message(source="user", text=text_data_json["text"])
            self._save_message(source="bot", text=output)

    def chat_message(self, event):
        text = event["text"]
        self.send(text_data=json.dumps({"text": text}))
    
    def _save_message(self, source: str, text: str):
        message = {
                "type": "chat.message",
                "source": source,
                "text": text,
            }
        self._chat_history.append(message)
    
    def disconnect(self, code):
        _current_thread_id = self._bot.thread.id
        _path = os.path.join(os.environ.get("TESTING_DATA_FILE", "data"), _current_thread_id)
        _path = _path + ".json"
        os.makedirs(os.path.dirname(_path), exist_ok=True)
        with open(_path, 'w', encoding='utf8') as f:
            json.dump(self._chat_history, fp=f, ensure_ascii=False)
        return super().disconnect(code)
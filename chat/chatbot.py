from openai import OpenAI
import os
import time
import asyncio

class Assistant:
    def __init__(self) -> None:    
        self.name = "FitnessWell_virtual_assistant"
        self.client = OpenAI(api_key=os.environ.get("SECRET_KEY"))
        self.thread = self.client.beta.threads.create()
        self.assistant = self.client.beta.assistants.list().data[-1]
        # import ipdb; ipdb.set_trace()
    def talk_to_assistant(self, input_text):
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role='user',
            content=input_text
        )
    
    def get_assistant_response(self):
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id
        )
        while run.status in ["queued", "in_progress", "cancelling"]:
            time.sleep(1)
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id
            )
        if run.status=='completed':
            messages = self.client.beta.threads.messages.list(
                thread_id=self.thread.id,
            )
            output = messages.data[0].content[-1].text.value
            return output
        else:
            return "Chatbot failed to answer your question."
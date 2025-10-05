from ollama import chat
from ollama import ChatResponse

class OllamaClient:

    def __init__(self, content):
        self.content = content
        
    def process_prompt(self):

      response = self.generate_payload()
      if response != None or response != '':
         return response

    def generate_payload(self):
      system_prompt = f''' 
        You are an expert at extracting keywords from job descriptions.
        Extract keywords and technologies.
        Do not create sentences.
        Make sure to output bullet points.
        Keep the answer short and brief in bullet point format.
      '''
      response: ChatResponse = chat(
        model='qwen3:0.6b',   
        messages= [{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': self.content}], 
      )

      return response["message"]["content"]

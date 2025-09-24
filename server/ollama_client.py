from ollama import chat
import requests
import json


class OllamaClient:
    def __init__(self, content):
        self.content = content
    
    url = "http://127.0.0.1:11434/api/chat"

    def process_prompt(self):

      payload = self.generate_payload()

      response = requests.post(OllamaClient.url, json=payload, stream=True)

      list_of_response = []

      if response.status_code == 200:
          print("Streaming response from Ollama:")
          for line in response.iter_lines(decode_unicode=True):
              if line: 
                  try:
                      json_data = json.loads(line)
                      if "message" in json_data and "content" in json_data["message"]:
                          #print(json_data["message"]["content"], end="")
                          list_of_response.append(json_data["message"]["content"])
                  except json.JSONDecodeError:
                      print(f"\nFailed to parse line: {line}")
          print()
          promptResponse = ''.join(list_of_response)
          return promptResponse
      else:
          print(f"Error: {response.status_code}")
          print(response.text)


    def generate_payload(self):
      system_prompt = ''' You are an expert at tailoring resumes. Always make sure to return
        tailored points in bullet points. Do not use markdown.
      '''
      payload = {
        "model": 'gemma3',  
        "messages": [{'role': 'user', 'content': self.content}, {'role': 'system', 'content': system_prompt}], 
      }
        
      return payload




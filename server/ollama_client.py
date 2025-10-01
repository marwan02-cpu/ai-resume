from ollama import chat
from ollama import ChatResponse

class OllamaClient:
    
    resume = '''PUT RESUME INFO HERE '''
    def __init__(self, content):
        self.content = content
    def process_prompt(self):

      response = self.generate_payload()
      if response != None or response != '':
         return response

    def generate_payload(self):
      system_prompt = f''' 
        You are an expert at tailoring resumes.
        Here is the resume to tailor: {OllamaClient.resume}
        Only return the tailored resume in your output.
        Follow the same format given to you.
        Make sure to include the key technologies from the job posting in the tailored resume.

        Tailor the resume as if I did some of the work even if it's not mentioned in the resume.
        At the end put which aspects you've tailored.
      '''
      response: ChatResponse = chat(
        model='gemma3',  
        messages= [{'role': 'user', 'content': self.content}, {'role': 'system', 'content': system_prompt}], 
      )
        
      return response["message"]["content"]

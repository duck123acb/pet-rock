import requests
import secret
import time

'''
you need to run ollama serve beforehand

we're probably gonna use mistral, but we'll see
'''

def make_request(prompt):
  response = requests.post(
    "http://localhost:11434/api/generate",
    json={
      'model': "llama3.2",
      "prompt": f"{prompt}",
      "stream": False
    }
  )


  # Parse the response
  data = response.json()
  return data["response"]

'testing'
# print(make_request(secret.setup_prompt))

# while True:
#   print(make_request("give me a line"))
#   time.sleep(3)
import requests

'''
you need to run ollama serve beforehand

we're probably gonna use mistral, but we'll see
'''

def make_request(prompt):
  response = requests.post(
    "http://localhost:11434/api/generate",
    json={
      f'model': "mistral",
      "prompt": "{prompt}",
      "stream": False
    }
  )


  # Parse the response
  data = response.json()
  return data["response"]

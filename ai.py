import ollama
import secret

'''
you need to run ollama serve beforehand

we're probably gonna use mistral, but we'll see
'''
def make_request(user_prompt):
  stream = ollama.generate(
    model=secret.model,
    prompt=f"{user_prompt}",
  )

  return stream['response']

# make_request("")

'testing'
# print(make_request(secret.setup_prompt))

# while True:
#   print(make_request("give me a line"))
#   time.sleep(3)
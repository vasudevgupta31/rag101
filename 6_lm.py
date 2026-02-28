from ollama import chat

response = chat(model='gpt-oss:20b',
                messages=[{'role': 'user', 'content': 'Hello!'}])
print(response.message.content)

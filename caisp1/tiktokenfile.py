import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
text = "ChatGPT is powerful!, but that is also subjective"

tokens = enc.encode(text)
print(tokens)
print([enc.decode([t]) for t in tokens])
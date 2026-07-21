from transformers import pipeline

ner = pipeline("ner")

text = "Sundar Pichai is the CEO of Google."

result = ner(text)

print(result)
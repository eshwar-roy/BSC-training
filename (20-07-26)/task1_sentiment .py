from transformers import pipeline
classifier = pipeline("sentiment-analysis")
text = "I love learning AI."
result = classifier(text)
print(result) 
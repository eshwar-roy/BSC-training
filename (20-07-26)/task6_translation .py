from transformers import pipeline

translator = pipeline("translation_en_to_fr")

text = "Machine Learning is changing the world."

result = translator(text)

print(result) 
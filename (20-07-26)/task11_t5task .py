from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

text = "Summarize: Artificial Intelligence helps computers learn from data and solve problems."

result = generator(text)

print(result[0]["generated_text"])
from transformers import pipeline
generator = pipeline(
    "text-generation",
    model="gpt2"
)
result = generator(
    "Artificial Intelligence is",
    max_new_tokens=40
)
print(result[0]["generated_text"])
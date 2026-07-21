from transformers import pipeline

classifier = pipeline("sentiment-analysis")

reviews = [
    "The product is excellent.",
    "Very bad experience.",
    "The service was okay.",
    "I am happy with the purchase."
]

for review in reviews:
    result = classifier(review)
    print(review)
    print(result)
    print()
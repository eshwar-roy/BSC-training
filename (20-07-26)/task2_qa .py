from transformers import pipeline

qa = pipeline(
    task="question-answering",
    model="distilbert-base-cased-distilled-squad"
)

result = qa(
    question="What is AI?",
    context="Artificial Intelligence is the simulation of human intelligence in machines."
)
print(result) 
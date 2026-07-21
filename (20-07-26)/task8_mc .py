from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I love learning AI."

inputs = tokenizer(
    text,
    return_tensors="pt"
)

outputs = model(**inputs)

probabilities = torch.softmax(
    outputs.logits,
    dim=1
)

prediction = torch.argmax(
    outputs.logits,
    dim=1
)

label = model.config.id2label[prediction.item()]

print(probabilities)

print(label) 
from transformers import AutoTokenizer, AutoModel
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
print("Tokenizer Loaded Successfully")
print("Model Loaded Successfully")
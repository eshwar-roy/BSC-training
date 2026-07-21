from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

model_name = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name)

text = "Artificial Intelligence is"

inputs = tokenizer(
    text,
    return_tensors="pt"
)

output = model.generate(
    **inputs,
    max_new_tokens=40
)

generated_text = tokenizer.decode(
    output[0],
    skip_special_tokens=True
)

print(generated_text)
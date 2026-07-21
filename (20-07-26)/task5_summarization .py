from transformers import pipeline
summarizer = pipeline("summarization")
text = """
Artificial Intelligence is changing healthcare,
education, finance and transportation.
It helps automate work and improve decision making.
"""
summary = summarizer( 
    text,
    max_length=40,
    min_length=15,
    do_sample=False
)
print(summary[0]["summary_text"])
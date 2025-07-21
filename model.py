from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os
from dotenv import load_dotenv

class Transliterator:
    def __init__(self, model_name_or_path: str):
        load_dotenv()
        HF_ARABIX_BACKEND=os.getenv("HF_ARABIX_BACKEND")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, token=HF_ARABIX_BACKEND)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name_or_path, token=HF_ARABIX_BACKEND)

    def transliterate(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from huggingface_hub import login
import os
from dotenv import load_dotenv


class Transliterator:
    def __init__(self, model_name_or_path: str):
        self.model_path = model_name_or_path
        self.login()
        self.load_tokenizer()
        self.load_model()

    def login(self):
        load_dotenv()
        HF_ARABIX_BACKEND = os.getenv("HF_ARABIX_BACKEND")
        print(HF_ARABIX_BACKEND)
        login(token=HF_ARABIX_BACKEND)

    def load_tokenizer(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)

    def load_model(self):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path)

    def transliterate(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os


class Transliterator:
    def __init__(self, model_name_or_path: str):
        hf_token = os.getenv("HF_ARABIX_SMALL_KEY")
        print(hf_token)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_auth_token=hf_token)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name_or_path, use_auth_token=hf_token)

    def transliterate(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
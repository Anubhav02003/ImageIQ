import torch
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

class VQAModel:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
        self.model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

    def answer_question(self, image_path, question):
        image = Image.open(image_path).convert('RGB')
        inputs = self.processor(image, question, return_tensors="pt")
        with torch.no_grad():  # Disables gradient calculation for inference[1][2][5]
            out = self.model.generate(**inputs)
        answer = self.processor.decode(out[0], skip_special_tokens=True)
        return answer

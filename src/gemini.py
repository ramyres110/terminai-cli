import os
import platform
import google.generativeai as genai
from .settings import Setting

class MyGemini:
    model = None

    def __init__(self, setting: Setting) -> None:
        self.model = self.configure(setting)

    def configure(self, setting: Setting):
        if (setting.apikey.strip() == ""):
            raise Exception("API Key Not Found")
                
        if (setting.model.strip() == ""):
            raise Exception("Model name Not Found")
        
        # Set up the model
        generation_config = {
        "temperature": 0.5,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 100000,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
        ]

        system_instruction = "Act like tech expert and be more succint"

        genai.configure(api_key=setting.apikey)
        
        model = genai.GenerativeModel(
            model_name=setting.model,
            generation_config=generation_config,
            system_instruction=system_instruction,
            safety_settings=safety_settings
        )

        return model

    def list_model(self) -> list[str]:
        models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                models.append(m.name)
        return models

    def count_token(self, prompt) -> int :
        self.model.count_tokens(prompt)

    def ask(self, txt) -> str:
        # TODO: Separar prompt engineer
        context = [f"The user name is {os.getlogin()}",
                   f"The user is using {platform.system()} {platform.release()}",
                   "Answer the question in the language that was made"]
        prompt = [*context, f"The question is: {txt}"]
        response = self.model.generate_content(prompt)
        return f"\nANSWER:\n{response.text}"

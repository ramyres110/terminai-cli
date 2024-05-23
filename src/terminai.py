import os
from sys import argv, path
from subprocess import call

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
path.append(parent)

from src.settings import Setting
from src.gemini import MyGemini
from src.constants import HELP_TEXT

class App:
    setting = None

    def __init__(self) -> None:
        self.setting = Setting()

    def show_help(self):
        print(HELP_TEXT)

    def open_configfile(self):        
        call(f"explorer {self.setting.envfile}", shell=False)

    def list_apis(self):        
        print(self.setting.api)

    def list_models(self):
        model = MyGemini(self.setting)
        print(f"For API {self.setting.api}")       
        for m in model.list_model():
            if m == f"models/{self.setting.model}":
                print(f"* {m}")
            else:
                print(f"- {m}")

    def send_prompt(self, text):
        model = MyGemini(self.setting)
        resp = model.ask(text)
        print(resp)

    def run(self):
        if len(argv) == 1:
            self.show_help()
        elif len(argv) == 2:   
            param = argv[1]
            
            if param.strip() == "":
                print("Invalid prompt!")
            elif param in ["-h", "--help"]:
                self.show_help()
            elif param in ["-s", "--setup"]:
                self.open_configfile()
            elif param in ["--list-api"]:
                self.list_apis()
            elif param in ["--list-models"]:
                self.list_models()
            else:
                self.send_prompt(param.strip())
        else:
            print("Invalid!!")
            self.show_help()            
            
if __name__ == "__main__":
    app = App()
    app.run()
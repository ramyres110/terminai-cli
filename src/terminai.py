import os
from sys import argv, path
from subprocess import call

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
path.append(parent)

from src.settings import Setting
from src.gemini import MyGemini

HELP_TEXT="""
TerminAI: LLM AI for terminal.
Use: terminai ["prompt" | options]
* prompt: llm prompt
* options:
    -h or --help: Show this
    -s or --setup: Open config file 
        Configs:
            api *default Gemini
            model *default gemini-1.5-pro-latest
            apikey *Gen at <https://aistudio.google.com/app/apikey>
    --list-api: Show implemented APIs
    --list-models: Show list of models at API
"""

class App:
    setting = None
    model = None

    def __init__(self) -> None:
        self.setting = Setting()
        self.model = MyGemini(self.setting)

    def show_help(self):
        print(HELP_TEXT)

    def open_configfile(self):        
        call(f"explorer {self.setting.envfile}", shell=False)

    def list_apis(self):        
        print(self.setting.api)

    def list_models(self):
        print(f"For API {self.setting.api}")       
        for m in self.model.list_model():
            if m == f"models/{self.setting.model}":
                print(f"* {m}")
            else:
                print(f"- {m}")

    def run(self):
        if len(argv) == 1:
            self.show_help()
        elif len(argv) == 2:        
            if argv[1] in ["-h", "--help"]:
                self.show_help()
            elif argv[1] in ["-s", "--setup"]:
                self.open_configfile()
            elif argv[1] in ["--list-api"]:
                self.list_apis()
            elif argv[1] in ["--list-models"]:
                self.list_models()
            elif argv[1].strip() == "":
                print("Invalid prompt!")
            else:
                prompt = argv[1].strip()
                resp = self.model.ask(prompt)
                print(resp)
        else:
            print("Invalid!!")
            self.show_help()
            
            
if __name__ == "__main__":
    app = App()
    app.run()
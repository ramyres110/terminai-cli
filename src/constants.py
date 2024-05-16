from pathlib import Path

HOMEDIR = str(Path.home())
CONFIG_SECTION = "config"

ENV_FILE_PATH = f"{HOMEDIR}\\.terminai"

TERMINAI_ENV = {
    "envfile": ENV_FILE_PATH,
    "api": "gemini",
    "model": "gemini-1.5-pro-latest",
    "apikey": ""
}

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

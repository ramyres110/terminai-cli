from pathlib import Path
from configparser import ConfigParser

HOMEDIR = str(Path.home())
CONFIG_SECTION = "config"

ENV_FILE_PATH = f"{HOMEDIR}\\.terminai"

TERMINAI_ENV = {
    "envfile": ENV_FILE_PATH,
    "api": "gemini",
    "model": "gemini-1.5-pro-latest",
    "apikey": ""
}

class Setting:
    envfile = TERMINAI_ENV["envfile"]
    api = TERMINAI_ENV["api"]
    model = TERMINAI_ENV["model"]
    apikey = TERMINAI_ENV["apikey"]

    def __init__(self) -> None:
        settings = self.loadSettings()
        self.envfile = settings["envfile"]
        self.api = settings["api"]
        self.model = settings["model"]
        self.apikey = settings["apikey"]

    def saveSettings(self):
        config = ConfigParser()
        config.read(ENV_FILE_PATH)
        if not config.has_section(CONFIG_SECTION):
            config.add_section(CONFIG_SECTION)
        for (key, value) in TERMINAI_ENV.items():
            config.set(CONFIG_SECTION, key.upper(), value)
        with open(ENV_FILE_PATH,'w') as configfile:
            config.write(configfile)
        
        
    def loadSettings(self):
        envfile_path = Path(ENV_FILE_PATH)       
        config = ConfigParser()
        config.read(ENV_FILE_PATH)

        if not envfile_path.is_file():
            self.saveSettings()
            return TERMINAI_ENV
        else:
            for key in TERMINAI_ENV.keys():
                TERMINAI_ENV[key] = config.get(CONFIG_SECTION, key.upper())
            return TERMINAI_ENV


    def getValueOf(self, var_name: str) -> str:
        self.loadSettings()
        return TERMINAI_ENV[var_name]


    def setValueOf(self, var_name: str, value: str):
        self.loadSettings()
        if not var_name in TERMINAI_ENV.keys():
            return False
        TERMINAI_ENV[var_name] = value
        self.saveSettings()
        return True

# local test
if __name__ == "__main__":
    setting = Setting()
    envfile = setting.getValueOf("envfile")
    if envfile != ENV_FILE_PATH:
        raise 
    setting.setValueOf("envfile", ENV_FILE_PATH)
    envfile = setting.getValueOf("envfile")
    if envfile != ENV_FILE_PATH:
        raise 
    envfile = setting.envfile
    if envfile != ENV_FILE_PATH:
        raise 
    print(setting.apikey)
import importlib

class Settings:
    def __init__(self):
        setting_modules = ['EmailAll.config.setting','EmailAll.config.api']
        for setting_module in setting_modules:
            setting = importlib.import_module(setting_module)
            for attr in dir(setting):
                setattr(self, attr, getattr(setting,attr))
settings = Settings()
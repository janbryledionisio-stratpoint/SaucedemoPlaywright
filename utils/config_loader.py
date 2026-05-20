import yaml

class Config:
    def __init__(self, config_file = "config/config.yaml"):
        with open(config_file, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self, *keys, default = None):
        data = self.config
        for key in keys:
            if not isinstance(data, dict):
                return default
            data = data.get(key, default)
        return data
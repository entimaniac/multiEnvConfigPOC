from config.config_base import BaseConfig


class Pipeline1Config(BaseConfig):
    # python 3.10 can use a switch (match) here instead
    def __init__(self):
        super().__init__()
        if self.environment == "staging":
            self.valA = "stagA"
            self.valB = "stagB"
            self.valC = "stagC"
        elif self.environment == "production":
            self.valA = "prodA"
            self.valB = "prodB"
            self.valC = "prodC"
        else:
            self.valA = "devA"
            self.valB = "devB"
            self.valC = "devC"

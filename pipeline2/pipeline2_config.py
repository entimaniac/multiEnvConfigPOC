from config.config_base import BaseConfig


class Pipeline2Config(BaseConfig):
    # python 3.10 can use a switch (match) here instead
    def __init__(self):
        super().__init__()
        if self.environment == "staging":
            self.valA = "222stagA"
            self.valB = "222stagB"
        elif self.environment == "production":
            self.valA = "222prodA"
            self.valB = "222prodB"
        else:
            self.valA = "222devA"
            self.valB = "222devB"

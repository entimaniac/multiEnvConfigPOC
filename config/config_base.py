import os

from config.string_decorator import to_string


@to_string
class BaseConfig:
    def __init__(self):
        self.environment = os.getenv("ENV", "default").lower()

    # def __str__(self):
    #     class_name = type(self).__name__
    #     instance_variables_string = ', '.join('%s=%s' % item for item in vars(self).items())
    #     return '%s(%s)' % (class_name, instance_variables_string)


class Pipeline1Config(BaseConfig):
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


def test_this():
    print("testing:")
    config = Pipeline1Config()
    print(config.valA)
    print(config)


test_this()

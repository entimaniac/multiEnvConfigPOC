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

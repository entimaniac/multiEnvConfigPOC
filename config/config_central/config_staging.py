import os


class AppConfig:
    environment = os.getenv("ENV", "default").lower()


class ExampleConfig:
    notebook_name = "/some/path/to/a/notebook/staging"


class P1Config:
    valA = "stag1"


class P2Config:
    valA = "stag2"

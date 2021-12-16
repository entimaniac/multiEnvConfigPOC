import os


class AppConfig:
    environment = os.getenv("ENV", "default").lower()


class ExampleConfig:
    notebook_name = "/some/path/to/a/notebook/production"


class P1Config:
    valA = "prod1"


class P2Config:
    valA = "prod2"

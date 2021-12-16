import os


class AppConfig:
    environment = os.getenv("ENV", "default").lower()


class ExampleConfig:
    notebook_name = "/some/path/to/a/notebook/default"


class P1Config:
    valA = "dev1"


class P2Config:
    valA = "dev2"

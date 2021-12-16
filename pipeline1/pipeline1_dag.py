from config.config_central import ExampleConfig, AppConfig, P1Config
from pipeline1.pipeline1_config import Pipeline1Config


def test_this():
    # locally located multi-env config:
    config = Pipeline1Config()
    print(config.valA)
    print(config)

    # centrally located multi-env config:
    print(AppConfig.environment)
    print(ExampleConfig.notebook_name)
    print(P1Config.valA)


test_this()

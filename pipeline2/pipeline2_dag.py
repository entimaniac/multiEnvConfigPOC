from config.config_central import AppConfig, ExampleConfig, P2Config

from pipeline2.pipeline2_config import Pipeline2Config


def test_that():
    # locally located multi-env config:
    config = Pipeline2Config()
    print(config.valA)
    print(config)

    # centrally located multi-env config:
    print(AppConfig.environment)
    print(ExampleConfig.notebook_name)
    print(P2Config.valA)


test_that()

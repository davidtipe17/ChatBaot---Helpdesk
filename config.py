from os import getenv
from datetime import timedelta


class DevelopmentConfig():
    DEBUG = True


class ProductionConfig():
    DEBUG = False


config_env = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

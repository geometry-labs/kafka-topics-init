from pydantic import BaseSettings
from typing import Union

class Config(BaseSettings):
    KAFKA_URL: str
    KAFKA_SCHEMA_REGISTRY_URL: str
    KAFKA_TOPIC_INIT_TOPICS_PATH: str = "/topics/topics.json"

configs = Config()

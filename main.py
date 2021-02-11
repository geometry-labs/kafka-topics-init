import json
import requests
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.schema_registry import SchemaRegistryClient, Schema

from config import configs


def main():
    kafka_url = configs.KAFKA_URL

    admin_client = AdminClient({
        "bootstrap.servers": kafka_url
    })

    topics_path = configs.KAFKA_TOPIC_INIT_TOPICS_PATH
    with open(topics_path) as f:
        topics_config = json.load(f)

    topic_list = []
    schema_list = []
    for tc in topics_config:
        topic_name = tc["name"]
        topic_num_partitions = tc["num_partitions"]

        topic_list.append(NewTopic(topic_name, topic_num_partitions, 1))

        if "schema" in tc:
            schema_list.append(tc)

    # Create topics
    try:
        admin_client.create_topics(topic_list)
    except kafka.errors.TopicAlreadyExistsError:
        # topics already exists
        print("Topics already made")

    # Register Schemas
    schema_registry_client = SchemaRegistryClient({
        "url": "http://" + configs.KAFKA_SCHEMA_REGISTRY_URL
    })

    for ts in schema_list:
        name = ts["schema"]["schema"]["title"]
        shcema_type = ts["schema"]["schemaType"]
        schema_raw = ts["schema"]["schema"]

        schema = Schema(json.dumps(schema_raw), "JSON")
        print("Schema Registered")
        print(schema_registry_client.register_schema(name, schema))


if __name__ == "__main__":
    main()


import json
import kafka

from config import configs


def main():
    kafka_url = configs.KAFKA_URL

    admin_client = kafka.admin.KafkaAdminClient(
        bootstrap_servers=kafka_url, 
        client_id='kafka-topic-init-client'
    )

    topics_path = configs.KAFKA_TOPIC_INIT_TOPICS_PATH
    with open(topics_path) as f:
        topics_config = json.load(f)

    topic_list = []
    for tc in topics_config:
        topic_name = tc["name"]
        topic_num_partitions = tc["num_partitions"]

        topic_list.append(kafka.admin.NewTopic(name=topic_name, num_partitions=topic_num_partitions, replication_factor=1))

    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
    except kafka.errors.TopicAlreadyExistsError:
        # topics already exists
        exit(0)


if __name__ == "__main__":
    main()


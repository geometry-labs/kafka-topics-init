# kafka-topic-init

Init container to be used with [icon-api]() stack. 
Use this contianer to set up kafka topics.

Docker Hub: [image](https://hub.docker.com/r/pranavt61/kafka-topic-init)

## Edit the topics.json to add topics
```
[
  {
    "name": "your_topic_name",
    "num_partitions": 16
  },
  {    
    "name": "other_topic_name",
    "num_partitions": 1,
    "schema": {
      "schemaType": "JSON"
      "schema": {...}
    }
  }
]
```

## Build
```
docker build . -t icon-kafka-topics-init:latest
docker run \
  -e KAFKA_URL="kafka:9092" \
  -e KAFKA_SCHEMA_REGISTRY_URL="schemaregistry:8081" \
  icon-kafka-topics-init:latest
```

## Docker Compose set up
```
  kafka-topic-init:
    image: pranavt61/kafka-topic-init:latest
    depends_on:
      - kafka
    environment:
      KAFKA_URL: kafka:9092
      KAFKA_SCHEMA_REGISTRY_URL: schemaregistry:8081
    volumes:
      - ./kafka-topic-init/:/topics/
    restart: on-failure
```

## Enviroment Variables

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| KAFKA_URL | location of broker | NULL | True |
| KAFKA_SCHEMA_REGISTRY_URL | location of schema registry | NULL | True |
| KAFKA_TOPIC_INIT_TOPICS_PATH | location of topics.json | "./topics.json" | False |

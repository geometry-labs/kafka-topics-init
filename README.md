# kafka-topic-init

Init container to be used with [icon-api]() stack. 
Use this contianer to set up kafka topics.

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
    "schema": {...}
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

## Enviroment Variables

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| KAFKA_URL | location of broker | NULL | True |
| KAFKA_SCHEMA_REGISTRY_URL | location of schema registry | NULL | True |
| KAFKA_TOPIC_INIT_TOPICS_PATH | location of topics.json | "./topics.json" | False |

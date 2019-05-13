from pubsubs.registry import Registry

config = {
    "listeners": ["localhost:9092"],
    "subscriber": {
        "poll": 0.1,
        "group.id": "mygroup",
        "auto.offset.reset": "earliest"
    },
}

registry = Registry()
kafka = registry.new(name="myKafka", backend="kafka", **config)

subscriber = kafka.subscribe("mytopic")
while True:
    message = subscriber.listen()
    assert message == "howl"

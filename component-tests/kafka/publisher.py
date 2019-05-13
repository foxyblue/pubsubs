from pubsubs.registry import Registry

CONFIG = """\
pubsubs:
    myKafka:
        backend: kafka
        listeners: ['localhost:9092']
        publisher:
            poll: 1.0
            message.timeout.ms: 1500
"""

registry = Registry()
registry.register_from_config(CONFIG)

kafka = registry["myKafka"]
kafka.publish(topic="mytopic", message="howl")

"""Generated from Smithy shape ``com.amazonaws.iot#KafkaAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.client_properties
    import capo_iot.types.kafka_headers
    import capo_iot.types.string


class KafkaAction(TypedDict, closed=True):
    destination_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of Kafka action's VPC <code>TopicRuleDestination</code>.</p>"""
    topic: "capo_iot.types.string.String"
    """<p>The Kafka topic for messages to be sent to the Kafka broker.</p>"""
    key: NotRequired["capo_iot.types.string.String"]
    """<p>The Kafka message key.</p>"""
    partition: NotRequired["capo_iot.types.string.String"]
    """<p>The Kafka message partition.</p>"""
    client_properties: "capo_iot.types.client_properties.ClientProperties"
    """<p>Properties of the Apache Kafka producer client.</p>"""
    headers: NotRequired["capo_iot.types.kafka_headers.KafkaHeaders"]
    """<p>The list of Kafka headers that you specify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaAction) -> dict:
    out: dict = {}
    out["destinationArn"] = value["destination_arn"]
    out["topic"] = value["topic"]
    if "key" in value:
        out["key"] = value["key"]
    if "partition" in value:
        out["partition"] = value["partition"]
    import capo_iot.types.client_properties

    out["clientProperties"] = capo_iot.types.client_properties.serialize_json(
        value["client_properties"]
    )
    if "headers" in value:
        import capo_iot.types.kafka_headers

        out["headers"] = capo_iot.types.kafka_headers.serialize_json(value["headers"])
    return out


def deserialize_json(data: dict) -> KafkaAction:
    out: KafkaAction = {}  # type: ignore[typeddict-item]
    if data.get("destinationArn") is not None:
        out["destination_arn"] = data["destinationArn"]
    else:
        out["destination_arn"] = ""
    if data.get("topic") is not None:
        out["topic"] = data["topic"]
    else:
        out["topic"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("partition") is not None:
        out["partition"] = data["partition"]
    if data.get("clientProperties") is not None:
        import capo_iot.types.client_properties

        out["client_properties"] = capo_iot.types.client_properties.deserialize_json(
            data["clientProperties"]
        )
    else:
        out["client_properties"] = {}
    if data.get("headers") is not None:
        import capo_iot.types.kafka_headers

        out["headers"] = capo_iot.types.kafka_headers.deserialize_json(data["headers"])
    return out

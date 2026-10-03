"""Generated from Smithy shape ``com.amazonaws.iot#RepublishAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.mqtt_headers
    import capo_iot.types.qos
    import capo_iot.types.topic_pattern


class RepublishAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access.</p>"""
    topic: "capo_iot.types.topic_pattern.TopicPattern"
    """<p>The name of the MQTT topic.</p>"""
    qos: NotRequired["capo_iot.types.qos.Qos"]
    """<p>The Quality of Service (QoS) level to use when republishing messages. The default value is 0.</p>"""
    headers: NotRequired["capo_iot.types.mqtt_headers.MqttHeaders"]
    """<p>MQTT Version 5.0 headers information. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html"> MQTT</a> from the Amazon Web Services IoT Core Developer Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepublishAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["topic"] = value["topic"]
    if "qos" in value:
        out["qos"] = value["qos"]
    if "headers" in value:
        import capo_iot.types.mqtt_headers

        out["headers"] = capo_iot.types.mqtt_headers.serialize_json(value["headers"])
    return out


def deserialize_json(data: dict) -> RepublishAction:
    out: RepublishAction = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("RepublishAction.role_arn required")
    if data.get("topic") is not None:
        out["topic"] = data["topic"]
    else:
        raise DeserializationError("RepublishAction.topic required")
    if data.get("qos") is not None:
        out["qos"] = data["qos"]
    if data.get("headers") is not None:
        import capo_iot.types.mqtt_headers

        out["headers"] = capo_iot.types.mqtt_headers.deserialize_json(data["headers"])
    return out

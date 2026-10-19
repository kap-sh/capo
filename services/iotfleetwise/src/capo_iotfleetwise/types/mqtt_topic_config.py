"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#MqttTopicConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.iam_role_arn
    import capo_iotfleetwise.types.mqtt_topic_arn


class MqttTopicConfig(TypedDict, closed=True):
    mqtt_topic_arn: "capo_iotfleetwise.types.mqtt_topic_arn.MqttTopicArn"
    """<p>The ARN of the MQTT topic.</p>"""
    execution_role_arn: "capo_iotfleetwise.types.iam_role_arn.IAMRoleArn"
    """<p>The ARN of the role that grants Amazon Web Services IoT FleetWise permission to access and act on messages sent to the MQTT topic.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MqttTopicConfig) -> dict:
    out: dict = {}
    out["mqttTopicArn"] = value["mqtt_topic_arn"]
    out["executionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MqttTopicConfig:
    out: MqttTopicConfig = {}  # type: ignore[typeddict-item]
    if data.get("mqttTopicArn") is not None:
        out["mqtt_topic_arn"] = data["mqttTopicArn"]
    else:
        out["mqtt_topic_arn"] = ""
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    return out

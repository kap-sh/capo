"""Generated from Smithy shape ``com.amazonaws.iot#MetricsExportConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.mqtt_topic
    import capo_iot.types.role_arn


class MetricsExportConfig(TypedDict, closed=True):
    mqtt_topic: "capo_iot.types.mqtt_topic.MqttTopic"
    """<p>The MQTT topic that Device Defender Detect should publish messages to for metrics export.</p>"""
    role_arn: "capo_iot.types.role_arn.RoleArn"
    """<p>This role ARN has permission to publish MQTT messages, after which Device Defender Detect can assume the role and publish messages on your behalf.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsExportConfig) -> dict:
    out: dict = {}
    out["mqttTopic"] = value["mqtt_topic"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> MetricsExportConfig:
    out: MetricsExportConfig = {}  # type: ignore[typeddict-item]
    if data.get("mqttTopic") is not None:
        out["mqtt_topic"] = data["mqttTopic"]
    else:
        out["mqtt_topic"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.iotevents#IotTopicPublishAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.mqtt_topic
    import capo_iot_events.types.payload


class IotTopicPublishAction(TypedDict, closed=True):
    mqtt_topic: "capo_iot_events.types.mqtt_topic.MQTTTopic"
    """<p>The MQTT topic of the message. You can use a string expression that includes variables (<code>$variable.<variable-name></code>) and input values (<code>$input.<input-name>.<path-to-datum></code>) as the topic string.</p>"""
    payload: NotRequired["capo_iot_events.types.payload.Payload"]
    """<p>You can configure the action payload when you publish a message to an AWS IoT Core topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotTopicPublishAction) -> dict:
    out: dict = {}
    out["mqttTopic"] = value["mqtt_topic"]
    if "payload" in value:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> IotTopicPublishAction:
    out: IotTopicPublishAction = {}  # type: ignore[typeddict-item]
    if data.get("mqttTopic") is not None:
        out["mqtt_topic"] = data["mqttTopic"]
    else:
        out["mqtt_topic"] = ""
    if data.get("payload") is not None:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.deserialize_json(data["payload"])
    return out

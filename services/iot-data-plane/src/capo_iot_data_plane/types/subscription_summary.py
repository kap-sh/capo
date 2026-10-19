"""Generated from Smithy shape ``com.amazonaws.iotdataplane#SubscriptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.qos
    import capo_iot_data_plane.types.topic_filter


class SubscriptionSummary(TypedDict, closed=True):
    topic_filter: "capo_iot_data_plane.types.topic_filter.TopicFilter"
    """<p>The topic filter pattern that the client is subscribed to. May include MQTT wildcards such as + (single-level) and # (multi-level).</p>"""
    qos: "capo_iot_data_plane.types.qos.Qos"
    """<p>The Quality of Service (QoS) level for the subscription. Valid values are 0 (at most once) and 1 (at least once).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionSummary) -> dict:
    out: dict = {}
    out["topicFilter"] = value["topic_filter"]
    out["qos"] = value.get("qos", 0)
    return out


def deserialize_json(data: dict) -> SubscriptionSummary:
    out: SubscriptionSummary = {}  # type: ignore[typeddict-item]
    if data.get("topicFilter") is not None:
        out["topic_filter"] = data["topicFilter"]
    else:
        out["topic_filter"] = ""
    if data.get("qos") is not None:
        out["qos"] = data["qos"]
    else:
        out["qos"] = 0
    return out

"""Generated from Smithy shape ``com.amazonaws.iot#KafkaActionHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.kafka_header_key
    import capo_iot.types.kafka_header_value


class KafkaActionHeader(TypedDict, closed=True):
    key: "capo_iot.types.kafka_header_key.KafkaHeaderKey"
    """<p>The key of the Kafka header.</p>"""
    value: "capo_iot.types.kafka_header_value.KafkaHeaderValue"
    """<p>The value of the Kafka header.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaActionHeader) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KafkaActionHeader:
    out: KafkaActionHeader = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out

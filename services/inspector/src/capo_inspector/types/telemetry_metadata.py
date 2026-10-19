"""Generated from Smithy shape ``com.amazonaws.inspector#TelemetryMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.long
    import capo_inspector.types.message_type


class TelemetryMetadata(TypedDict, closed=True):
    message_type: "capo_inspector.types.message_type.MessageType"
    """<p>A specific type of behavioral data that is collected by the agent.</p>"""
    count: "capo_inspector.types.long.Long"
    """<p>The count of messages that the agent sends to the Amazon Inspector service.</p>"""
    data_size: NotRequired["capo_inspector.types.long.Long"]
    """<p>The data size of messages that the agent sends to the Amazon Inspector service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TelemetryMetadata) -> dict:
    out: dict = {}
    out["messageType"] = value["message_type"]
    out["count"] = value["count"]
    if "data_size" in value:
        out["dataSize"] = value["data_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TelemetryMetadata:
    out: TelemetryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("messageType") is not None:
        out["message_type"] = data["messageType"]
    else:
        out["message_type"] = ""
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("dataSize") is not None:
        out["data_size"] = data["dataSize"]
    return out

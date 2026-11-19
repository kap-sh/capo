"""Generated from Smithy shape ``com.amazonaws.scheduler#EventBridgePutEventsV2Parameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.detail_type
    import capo_scheduler.types.source


class EventBridgePutEventsV2Parameters(TypedDict, closed=True):
    detail_type: "capo_scheduler.types.detail_type.DetailType"
    """<p>A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.</p>"""
    source: "capo_scheduler.types.source.Source"
    """<p>The source of the event. The source can't start with the <code>aws.</code> prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgePutEventsV2Parameters) -> dict:
    out: dict = {}
    out["DetailType"] = value["detail_type"]
    out["Source"] = value["source"]
    return out


def deserialize_json(data: dict) -> EventBridgePutEventsV2Parameters:
    out: EventBridgePutEventsV2Parameters = {}  # type: ignore[typeddict-item]
    if data.get("DetailType") is not None:
        out["detail_type"] = data["DetailType"]
    else:
        out["detail_type"] = ""
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        out["source"] = ""
    return out

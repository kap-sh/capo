"""Generated from Smithy shape ``com.amazonaws.elementalinference#FixedIntervalTrigger``."""

from typing_extensions import TypedDict


class FixedIntervalTrigger(TypedDict, closed=True):
    interval_seconds: "int"
    """<p>The amount of content, in seconds, between runs of the function. Valid range: 1 to 60. For a function with eventBridgeDelivery set to ENABLED, the minimum is 4. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FixedIntervalTrigger) -> dict:
    out: dict = {}
    out["intervalSeconds"] = value["interval_seconds"]
    return out


def deserialize_json(data: dict) -> FixedIntervalTrigger:
    out: FixedIntervalTrigger = {}  # type: ignore[typeddict-item]
    if data.get("intervalSeconds") is not None:
        out["interval_seconds"] = data["intervalSeconds"]
    else:
        out["interval_seconds"] = 0
    return out

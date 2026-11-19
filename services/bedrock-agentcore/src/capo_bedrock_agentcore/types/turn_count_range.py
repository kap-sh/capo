"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TurnCountRange``."""

from typing_extensions import NotRequired, TypedDict


class TurnCountRange(TypedDict, closed=True):
    min: NotRequired["int"]
    """<p>The minimum number of turns.</p>"""
    max: NotRequired["int"]
    """<p>The maximum number of turns. The default is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TurnCountRange) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> TurnCountRange:
    out: TurnCountRange = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = data["min"]
    if data.get("max") is not None:
        out["max"] = data["max"]
    return out

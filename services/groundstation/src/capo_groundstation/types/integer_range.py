"""Generated from Smithy shape ``com.amazonaws.groundstation#IntegerRange``."""

from typing_extensions import TypedDict


class IntegerRange(TypedDict, closed=True):
    minimum: "int"
    """<p>A minimum value.</p>"""
    maximum: "int"
    """<p>A maximum value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerRange) -> dict:
    out: dict = {}
    out["minimum"] = value["minimum"]
    out["maximum"] = value["maximum"]
    return out


def deserialize_json(data: dict) -> IntegerRange:
    out: IntegerRange = {}  # type: ignore[typeddict-item]
    if data.get("minimum") is not None:
        out["minimum"] = data["minimum"]
    else:
        out["minimum"] = 0
    if data.get("maximum") is not None:
        out["maximum"] = data["maximum"]
    else:
        out["maximum"] = 0
    return out

"""Generated from Smithy shape ``com.amazonaws.iot#LocationTimestamp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.string


class LocationTimestamp(TypedDict, closed=True):
    value: "capo_iot.types.string.String"
    """<p>An expression that returns a long epoch time value.</p>"""
    unit: NotRequired["capo_iot.types.string.String"]
    """<p>The precision of the timestamp value that results from the expression described in <code>value</code>.</p> <p>Valid values: <code>SECONDS</code> | <code>MILLISECONDS</code> | <code>MICROSECONDS</code> | <code>NANOSECONDS</code>. The default is <code>MILLISECONDS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocationTimestamp) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "unit" in value:
        out["unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> LocationTimestamp:
    out: LocationTimestamp = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    return out

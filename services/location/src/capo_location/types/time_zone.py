"""Generated from Smithy shape ``com.amazonaws.location#TimeZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.sensitive_integer
    import capo_location.types.sensitive_string


class TimeZone(TypedDict, closed=True):
    name: "capo_location.types.sensitive_string.SensitiveString"
    """<p>The name of the time zone, following the <a href="https://www.iana.org/time-zones"> IANA time zone standard</a>. For example, <code>America/Los_Angeles</code>.</p>"""
    offset: NotRequired["capo_location.types.sensitive_integer.SensitiveInteger"]
    """<p>The time zone's offset, in seconds, from UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeZone) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "offset" in value:
        out["Offset"] = value["offset"]
    return out


def deserialize_json(data: dict) -> TimeZone:
    out: TimeZone = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("TimeZone.name required")
    if data.get("Offset") is not None:
        out["offset"] = data["Offset"]
    return out

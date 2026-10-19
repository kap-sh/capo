"""Generated from Smithy shape ``com.amazonaws.geoplaces#TimeZone``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.duration_seconds
    import capo_geo_places.types.sensitive_string


class TimeZone(TypedDict, closed=True):
    name: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The time zone name.</p>"""
    offset: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Time zone offset of the timezone from UTC.</p>"""
    offset_seconds: "capo_geo_places.types.duration_seconds.DurationSeconds"
    """<p>The offset of the time zone from UTC, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeZone) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "offset" in value:
        out["Offset"] = value["offset"]
    out["OffsetSeconds"] = value.get("offset_seconds", 0)
    return out


def deserialize_json(data: dict) -> TimeZone:
    out: TimeZone = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Offset") is not None:
        out["offset"] = data["Offset"]
    if data.get("OffsetSeconds") is not None:
        out["offset_seconds"] = data["OffsetSeconds"]
    else:
        out["offset_seconds"] = 0
    return out


def redact_sensitive(value: TimeZone) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "offset" in value:
        out["offset"] = "*** Sensitive Data Redacted ***"
    if "offset_seconds" in value:
        out["offset_seconds"] = "*** Sensitive Data Redacted ***"
    return out

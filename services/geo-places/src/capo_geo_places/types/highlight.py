"""Generated from Smithy shape ``com.amazonaws.geoplaces#Highlight``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class Highlight(TypedDict, closed=True):
    start_index: NotRequired["int"]
    """<p>Start index of the highlight.</p>"""
    end_index: NotRequired["int"]
    """<p>End index of the highlight.</p>"""
    value: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The highlight's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Highlight) -> dict:
    out: dict = {}
    if "start_index" in value:
        out["StartIndex"] = value["start_index"]
    if "end_index" in value:
        out["EndIndex"] = value["end_index"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Highlight:
    out: Highlight = {}  # type: ignore[typeddict-item]
    if data.get("StartIndex") is not None:
        out["start_index"] = data["StartIndex"]
    if data.get("EndIndex") is not None:
        out["end_index"] = data["EndIndex"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


def redact_sensitive(value: Highlight) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out

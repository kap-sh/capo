"""Generated from Smithy shape ``com.amazonaws.guardduty#SharedBehavior``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class SharedBehavior(TypedDict, closed=True):
    path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The JSON path of the finding attribute that matched.</p>"""
    value: NotRequired["capo_guardduty.types.string.String"]
    """<p>The value that matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharedBehavior) -> dict:
    out: dict = {}
    if "path" in value:
        out["path"] = value["path"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SharedBehavior:
    out: SharedBehavior = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out

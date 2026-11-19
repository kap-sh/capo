"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingTypeCount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.string


class FindingTypeCount(TypedDict, closed=True):
    finding_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The finding type.</p>"""
    count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings of this type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeCount) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> FindingTypeCount:
    out: FindingTypeCount = {}  # type: ignore[typeddict-item]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    return out

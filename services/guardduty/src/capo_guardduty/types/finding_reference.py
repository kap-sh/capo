"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.finding_id
    import capo_guardduty.types.string


class FindingReference(TypedDict, closed=True):
    finding_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the finding.</p>"""
    uid: NotRequired["capo_guardduty.types.finding_id.FindingId"]
    """<p>The ID of the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingReference) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "uid" in value:
        out["uid"] = value["uid"]
    return out


def deserialize_json(data: dict) -> FindingReference:
    out: FindingReference = {}  # type: ignore[typeddict-item]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    return out

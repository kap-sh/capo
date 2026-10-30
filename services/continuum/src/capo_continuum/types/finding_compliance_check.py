"""Generated from Smithy shape ``com.amazonaws.continuum#FindingComplianceCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.finding_category
    import capo_continuum.types.finding_description


class FindingComplianceCheck(TypedDict, closed=True):
    uid: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    name: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    description: NotRequired[
        "capo_continuum.types.finding_description.FindingDescription"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FindingComplianceCheck) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> FindingComplianceCheck:
    out: FindingComplianceCheck = {}  # type: ignore[typeddict-item]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out

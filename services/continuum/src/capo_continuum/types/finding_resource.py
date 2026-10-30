"""Generated from Smithy shape ``com.amazonaws.continuum#FindingResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.finding_category
    import capo_continuum.types.finding_resource_uid


class FindingResource(TypedDict, closed=True):
    uid: NotRequired["capo_continuum.types.finding_resource_uid.FindingResourceUid"]
    name: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    type: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    region: NotRequired["capo_continuum.types.finding_category.FindingCategory"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingResource) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> FindingResource:
    out: FindingResource = {}  # type: ignore[typeddict-item]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    return out

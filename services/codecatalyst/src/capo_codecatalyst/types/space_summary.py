"""Generated from Smithy shape ``com.amazonaws.codecatalyst#SpaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.region_string


class SpaceSummary(TypedDict, closed=True):
    name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    region_name: "capo_codecatalyst.types.region_string.RegionString"
    """<p>The Amazon Web Services Region where the space exists.</p>"""
    display_name: NotRequired["str"]
    """<p>The friendly name of the space displayed to users.</p>"""
    description: NotRequired["str"]
    """<p>The description of the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["regionName"] = value["region_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> SpaceSummary:
    out: SpaceSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    else:
        out["region_name"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out

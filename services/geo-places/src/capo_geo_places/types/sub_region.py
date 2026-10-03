"""Generated from Smithy shape ``com.amazonaws.geoplaces#SubRegion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class SubRegion(TypedDict, closed=True):
    code: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p> Abbreviated code for the county or sub-region. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    name: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Name for the county or sub-region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubRegion) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SubRegion:
    out: SubRegion = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out

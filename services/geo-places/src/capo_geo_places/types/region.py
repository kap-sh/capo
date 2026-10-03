"""Generated from Smithy shape ``com.amazonaws.geoplaces#Region``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class Region(TypedDict, closed=True):
    code: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p> Abbreviated code for a the state, province or region of the country. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <p>Example: <code>BC</code>.</p>"""
    name: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Name for a the state, province, or region of the country. </p> <p>Example: <code>British Columbia</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Region) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out

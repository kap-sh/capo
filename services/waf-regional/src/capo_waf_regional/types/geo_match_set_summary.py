"""Generated from Smithy shape ``com.amazonaws.wafregional#GeoMatchSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.resource_name


class GeoMatchSetSummary(TypedDict, closed=True):
    geo_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>GeoMatchSetId</code> for an <a>GeoMatchSet</a>. You can use <code>GeoMatchSetId</code> in a <a>GetGeoMatchSet</a> request to get detailed information about an <a>GeoMatchSet</a>.</p>"""
    name: "capo_waf_regional.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>GeoMatchSet</a>. You can't change the name of an <code>GeoMatchSet</code> after you create it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchSetSummary) -> dict:
    out: dict = {}
    out["GeoMatchSetId"] = value["geo_match_set_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GeoMatchSetSummary:
    out: GeoMatchSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("GeoMatchSetId") is not None:
        out["geo_match_set_id"] = data["GeoMatchSetId"]
    else:
        out["geo_match_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out

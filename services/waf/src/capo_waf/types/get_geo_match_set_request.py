"""Generated from Smithy shape ``com.amazonaws.waf#GetGeoMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id


class GetGeoMatchSetRequest(TypedDict, closed=True):
    geo_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>GeoMatchSetId</code> of the <a>GeoMatchSet</a> that you want to get. <code>GeoMatchSetId</code> is returned by <a>CreateGeoMatchSet</a> and by <a>ListGeoMatchSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGeoMatchSetRequest) -> dict:
    out: dict = {}
    out["GeoMatchSetId"] = value["geo_match_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGeoMatchSetRequest:
    out: GetGeoMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("GeoMatchSetId") is not None:
        out["geo_match_set_id"] = data["GeoMatchSetId"]
    else:
        out["geo_match_set_id"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.wafregional#DeleteGeoMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.resource_id


class DeleteGeoMatchSetRequest(TypedDict, closed=True):
    geo_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>GeoMatchSetID</code> of the <a>GeoMatchSet</a> that you want to delete. <code>GeoMatchSetId</code> is returned by <a>CreateGeoMatchSet</a> and by <a>ListGeoMatchSets</a>.</p>"""
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGeoMatchSetRequest) -> dict:
    out: dict = {}
    out["GeoMatchSetId"] = value["geo_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGeoMatchSetRequest:
    out: DeleteGeoMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("GeoMatchSetId") is not None:
        out["geo_match_set_id"] = data["GeoMatchSetId"]
    else:
        out["geo_match_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out

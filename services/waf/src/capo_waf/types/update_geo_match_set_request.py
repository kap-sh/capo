"""Generated from Smithy shape ``com.amazonaws.waf#UpdateGeoMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.geo_match_set_updates
    import capo_waf.types.resource_id


class UpdateGeoMatchSetRequest(TypedDict, closed=True):
    geo_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>GeoMatchSetId</code> of the <a>GeoMatchSet</a> that you want to update. <code>GeoMatchSetId</code> is returned by <a>CreateGeoMatchSet</a> and by <a>ListGeoMatchSets</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: "capo_waf.types.geo_match_set_updates.GeoMatchSetUpdates"
    """<p>An array of <code>GeoMatchSetUpdate</code> objects that you want to insert into or delete from an <a>GeoMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>GeoMatchSetUpdate</a>: Contains <code>Action</code> and <code>GeoMatchConstraint</code> </p> </li> <li> <p> <a>GeoMatchConstraint</a>: Contains <code>Type</code> and <code>Value</code> </p> <p>You can have only one <code>Type</code> and <code>Value</code> per <code>GeoMatchConstraint</code>. To add multiple countries, include multiple <code>GeoMatchSetUpdate</code> objects in your request.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGeoMatchSetRequest) -> dict:
    out: dict = {}
    out["GeoMatchSetId"] = value["geo_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    import capo_waf.types.geo_match_set_updates

    out["Updates"] = capo_waf.types.geo_match_set_updates.serialize_aws_json_1_1(
        value["updates"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGeoMatchSetRequest:
    out: UpdateGeoMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("GeoMatchSetId") is not None:
        out["geo_match_set_id"] = data["GeoMatchSetId"]
    else:
        out["geo_match_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    if data.get("Updates") is not None:
        import capo_waf.types.geo_match_set_updates

        out["updates"] = capo_waf.types.geo_match_set_updates.deserialize_aws_json_1_1(
            data["Updates"]
        )
    else:
        out["updates"] = []
    return out

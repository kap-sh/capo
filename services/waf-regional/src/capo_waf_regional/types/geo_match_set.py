"""Generated from Smithy shape ``com.amazonaws.wafregional#GeoMatchSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.geo_match_constraints
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.resource_name


class GeoMatchSet(TypedDict, closed=True):
    geo_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>GeoMatchSetId</code> for an <code>GeoMatchSet</code>. You use <code>GeoMatchSetId</code> to get information about a <code>GeoMatchSet</code> (see <a>GeoMatchSet</a>), update a <code>GeoMatchSet</code> (see <a>UpdateGeoMatchSet</a>), insert a <code>GeoMatchSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete a <code>GeoMatchSet</code> from AWS WAF (see <a>DeleteGeoMatchSet</a>).</p> <p> <code>GeoMatchSetId</code> is returned by <a>CreateGeoMatchSet</a> and by <a>ListGeoMatchSets</a>.</p>"""
    name: NotRequired["capo_waf_regional.types.resource_name.ResourceName"]
    """<p>A friendly name or description of the <a>GeoMatchSet</a>. You can't change the name of an <code>GeoMatchSet</code> after you create it.</p>"""
    geo_match_constraints: (
        "capo_waf_regional.types.geo_match_constraints.GeoMatchConstraints"
    )
    """<p>An array of <a>GeoMatchConstraint</a> objects, which contain the country that you want AWS WAF to search for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchSet) -> dict:
    out: dict = {}
    out["GeoMatchSetId"] = value["geo_match_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_waf_regional.types.geo_match_constraints

    out["GeoMatchConstraints"] = (
        capo_waf_regional.types.geo_match_constraints.serialize_aws_json_1_1(
            value["geo_match_constraints"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GeoMatchSet:
    out: GeoMatchSet = {}  # type: ignore[typeddict-item]
    if data.get("GeoMatchSetId") is not None:
        out["geo_match_set_id"] = data["GeoMatchSetId"]
    else:
        out["geo_match_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("GeoMatchConstraints") is not None:
        import capo_waf_regional.types.geo_match_constraints

        out["geo_match_constraints"] = (
            capo_waf_regional.types.geo_match_constraints.deserialize_aws_json_1_1(
                data["GeoMatchConstraints"]
            )
        )
    else:
        out["geo_match_constraints"] = []
    return out

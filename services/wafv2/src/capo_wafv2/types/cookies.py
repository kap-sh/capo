"""Generated from Smithy shape ``com.amazonaws.wafv2#Cookies``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.cookie_match_pattern
    import capo_wafv2.types.map_match_scope
    import capo_wafv2.types.oversize_handling


class Cookies(TypedDict, closed=True):
    match_pattern: "capo_wafv2.types.cookie_match_pattern.CookieMatchPattern"
    """<p>The filter to use to identify the subset of cookies to inspect in a web request. </p> <p>You must specify exactly one setting: either <code>All</code>, <code>IncludedCookies</code>, or <code>ExcludedCookies</code>.</p> <p>Example JSON: <code>"MatchPattern": { "IncludedCookies": [ "session-id-time", "session-id" ] }</code> </p>"""
    match_scope: "capo_wafv2.types.map_match_scope.MapMatchScope"
    """<p>The parts of the cookies to inspect with the rule inspection criteria. If you specify <code>ALL</code>, WAF inspects both keys and values. </p> <p> <code>All</code> does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical <code>AND</code> statement to combine two match rules, one that inspects the keys and another that inspects the values. </p>"""
    oversize_handling: "capo_wafv2.types.oversize_handling.OversizeHandling"
    """<p>What WAF should do if the cookies of the request are more numerous or larger than WAF can inspect. WAF does not support inspecting the entire contents of request cookies when they exceed 8 KB (8192 bytes) or 200 total cookies. The underlying host service forwards a maximum of 200 cookies and at most 8 KB of cookie contents to WAF. </p> <p>The options for oversize handling are the following:</p> <ul> <li> <p> <code>CONTINUE</code> - Inspect the available cookies normally, according to the rule inspection criteria. </p> </li> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Cookies) -> dict:
    out: dict = {}
    import capo_wafv2.types.cookie_match_pattern

    out["MatchPattern"] = capo_wafv2.types.cookie_match_pattern.serialize_aws_json_1_1(
        value["match_pattern"]
    )
    import capo_wafv2.types.map_match_scope

    out["MatchScope"] = capo_wafv2.types.map_match_scope.serialize_aws_json_1_1(
        value["match_scope"]
    )
    import capo_wafv2.types.oversize_handling

    out["OversizeHandling"] = capo_wafv2.types.oversize_handling.serialize_aws_json_1_1(
        value["oversize_handling"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Cookies:
    out: Cookies = {}  # type: ignore[typeddict-item]
    if data.get("MatchPattern") is not None:
        import capo_wafv2.types.cookie_match_pattern

        out["match_pattern"] = (
            capo_wafv2.types.cookie_match_pattern.deserialize_aws_json_1_1(
                data["MatchPattern"]
            )
        )
    else:
        raise DeserializationError("Cookies.match_pattern required")
    if data.get("MatchScope") is not None:
        import capo_wafv2.types.map_match_scope

        out["match_scope"] = capo_wafv2.types.map_match_scope.deserialize_aws_json_1_1(
            data["MatchScope"]
        )
    else:
        raise DeserializationError("Cookies.match_scope required")
    if data.get("OversizeHandling") is not None:
        import capo_wafv2.types.oversize_handling

        out["oversize_handling"] = (
            capo_wafv2.types.oversize_handling.deserialize_aws_json_1_1(
                data["OversizeHandling"]
            )
        )
    else:
        raise DeserializationError("Cookies.oversize_handling required")
    return out

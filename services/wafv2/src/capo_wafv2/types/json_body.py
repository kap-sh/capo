"""Generated from Smithy shape ``com.amazonaws.wafv2#JsonBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.body_parsing_fallback_behavior
    import capo_wafv2.types.json_match_pattern
    import capo_wafv2.types.json_match_scope
    import capo_wafv2.types.oversize_handling


class JsonBody(TypedDict, closed=True):
    match_pattern: "capo_wafv2.types.json_match_pattern.JsonMatchPattern"
    """<p>The patterns to look for in the JSON body. WAF inspects the results of these pattern matches against the rule inspection criteria. </p>"""
    match_scope: "capo_wafv2.types.json_match_scope.JsonMatchScope"
    """<p>The parts of the JSON to match against using the <code>MatchPattern</code>. If you specify <code>ALL</code>, WAF matches against keys and values. </p> <p> <code>All</code> does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical <code>AND</code> statement to combine two match rules, one that inspects the keys and another that inspects the values. </p>"""
    invalid_fallback_behavior: NotRequired[
        "capo_wafv2.types.body_parsing_fallback_behavior.BodyParsingFallbackBehavior"
    ]
    """<p>What WAF should do if it fails to completely parse the JSON body. The options are the following:</p> <ul> <li> <p> <code>EVALUATE_AS_STRING</code> - Inspect the body as plain text. WAF applies the text transformations and inspection criteria that you defined for the JSON inspection to the body text string.</p> </li> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul> <p>If you don't provide this setting, WAF parses and evaluates the content only up to the first parsing failure that it encounters. </p> <note> <p>WAF parsing doesn't fully validate the input JSON string, so parsing can succeed even for invalid JSON. When parsing succeeds, WAF doesn't apply the fallback behavior. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body">JSON body</a> in the <i>WAF Developer Guide</i>.</p> </note>"""
    oversize_handling: NotRequired[
        "capo_wafv2.types.oversize_handling.OversizeHandling"
    ]
    """<p>What WAF should do if the body is larger than WAF can inspect. </p> <p>WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to WAF for inspection. </p> <ul> <li> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p> </li> <li> <p>For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL <code>AssociationConfig</code>, for additional processing fees. </p> </li> <li> <p>For Amplify, use the CloudFront limit.</p> </li> </ul> <p>The options for oversize handling are the following:</p> <ul> <li> <p> <code>CONTINUE</code> - Inspect the available body contents normally, according to the rule inspection criteria. </p> </li> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul> <p>You can combine the <code>MATCH</code> or <code>NO_MATCH</code> settings for oversize handling with your rule and web ACL action settings, so that you block any request whose body is over the limit. </p> <p>Default: <code>CONTINUE</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JsonBody) -> dict:
    out: dict = {}
    import capo_wafv2.types.json_match_pattern

    out["MatchPattern"] = capo_wafv2.types.json_match_pattern.serialize_aws_json_1_1(
        value["match_pattern"]
    )
    import capo_wafv2.types.json_match_scope

    out["MatchScope"] = capo_wafv2.types.json_match_scope.serialize_aws_json_1_1(
        value["match_scope"]
    )
    if "invalid_fallback_behavior" in value:
        import capo_wafv2.types.body_parsing_fallback_behavior

        out["InvalidFallbackBehavior"] = (
            capo_wafv2.types.body_parsing_fallback_behavior.serialize_aws_json_1_1(
                value["invalid_fallback_behavior"]
            )
        )
    if "oversize_handling" in value:
        import capo_wafv2.types.oversize_handling

        out["OversizeHandling"] = (
            capo_wafv2.types.oversize_handling.serialize_aws_json_1_1(
                value["oversize_handling"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JsonBody:
    out: JsonBody = {}  # type: ignore[typeddict-item]
    if data.get("MatchPattern") is not None:
        import capo_wafv2.types.json_match_pattern

        out["match_pattern"] = (
            capo_wafv2.types.json_match_pattern.deserialize_aws_json_1_1(
                data["MatchPattern"]
            )
        )
    else:
        raise DeserializationError("JsonBody.match_pattern required")
    if data.get("MatchScope") is not None:
        import capo_wafv2.types.json_match_scope

        out["match_scope"] = capo_wafv2.types.json_match_scope.deserialize_aws_json_1_1(
            data["MatchScope"]
        )
    else:
        raise DeserializationError("JsonBody.match_scope required")
    if data.get("InvalidFallbackBehavior") is not None:
        import capo_wafv2.types.body_parsing_fallback_behavior

        out["invalid_fallback_behavior"] = (
            capo_wafv2.types.body_parsing_fallback_behavior.deserialize_aws_json_1_1(
                data["InvalidFallbackBehavior"]
            )
        )
    if data.get("OversizeHandling") is not None:
        import capo_wafv2.types.oversize_handling

        out["oversize_handling"] = (
            capo_wafv2.types.oversize_handling.deserialize_aws_json_1_1(
                data["OversizeHandling"]
            )
        )
    return out

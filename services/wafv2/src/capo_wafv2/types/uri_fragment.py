"""Generated from Smithy shape ``com.amazonaws.wafv2#UriFragment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.fallback_behavior


class UriFragment(TypedDict, closed=True):
    fallback_behavior: NotRequired[
        "capo_wafv2.types.fallback_behavior.FallbackBehavior"
    ]
    """<p>What WAF should do if it fails to completely parse the JSON body. The options are the following:</p> <ul> <li> <p> <code>EVALUATE_AS_STRING</code> - Inspect the body as plain text. WAF applies the text transformations and inspection criteria that you defined for the JSON inspection to the body text string.</p> </li> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul> <p>If you don't provide this setting, WAF parses and evaluates the content only up to the first parsing failure that it encounters. </p> <p>Example JSON: <code>{ "UriFragment": { "FallbackBehavior": "MATCH"} }</code> </p> <note> <p>WAF parsing doesn't fully validate the input JSON string, so parsing can succeed even for invalid JSON. When parsing succeeds, WAF doesn't apply the fallback behavior. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body">JSON body</a> in the <i>WAF Developer Guide</i>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UriFragment) -> dict:
    out: dict = {}
    if "fallback_behavior" in value:
        import capo_wafv2.types.fallback_behavior

        out["FallbackBehavior"] = (
            capo_wafv2.types.fallback_behavior.serialize_aws_json_1_1(
                value["fallback_behavior"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UriFragment:
    out: UriFragment = {}  # type: ignore[typeddict-item]
    if data.get("FallbackBehavior") is not None:
        import capo_wafv2.types.fallback_behavior

        out["fallback_behavior"] = (
            capo_wafv2.types.fallback_behavior.deserialize_aws_json_1_1(
                data["FallbackBehavior"]
            )
        )
    return out

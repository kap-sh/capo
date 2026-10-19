"""Generated from Smithy shape ``com.amazonaws.wafv2#ForwardedIPConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.fallback_behavior
    import capo_wafv2.types.forwarded_ip_header_name


class ForwardedIPConfig(TypedDict, closed=True):
    header_name: "capo_wafv2.types.forwarded_ip_header_name.ForwardedIPHeaderName"
    """<p>The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to <code>X-Forwarded-For</code>.</p> <note> <p>If the specified header isn't present in the request, WAF doesn't apply the rule to the web request at all.</p> </note>"""
    fallback_behavior: "capo_wafv2.types.fallback_behavior.FallbackBehavior"
    """<p>The match status to assign to the web request if the request doesn't have a valid IP address in the specified position.</p> <note> <p>If the specified header isn't present in the request, WAF doesn't apply the rule to the web request at all.</p> </note> <p>You can specify the following fallback behaviors:</p> <ul> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForwardedIPConfig) -> dict:
    out: dict = {}
    out["HeaderName"] = value["header_name"]
    import capo_wafv2.types.fallback_behavior

    out["FallbackBehavior"] = capo_wafv2.types.fallback_behavior.serialize_aws_json_1_1(
        value["fallback_behavior"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ForwardedIPConfig:
    out: ForwardedIPConfig = {}  # type: ignore[typeddict-item]
    if data.get("HeaderName") is not None:
        out["header_name"] = data["HeaderName"]
    else:
        out["header_name"] = ""
    if data.get("FallbackBehavior") is not None:
        import capo_wafv2.types.fallback_behavior

        out["fallback_behavior"] = (
            capo_wafv2.types.fallback_behavior.deserialize_aws_json_1_1(
                data["FallbackBehavior"]
            )
        )
    else:
        import typing

        out["fallback_behavior"] = typing.cast(
            "capo_wafv2.types.fallback_behavior.FallbackBehavior", ""
        )
    return out

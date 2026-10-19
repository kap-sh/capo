"""Generated from Smithy shape ``com.amazonaws.wafv2#IPSetForwardedIPConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.fallback_behavior
    import capo_wafv2.types.forwarded_ip_header_name
    import capo_wafv2.types.forwarded_ip_position


class IPSetForwardedIPConfig(TypedDict, closed=True):
    header_name: "capo_wafv2.types.forwarded_ip_header_name.ForwardedIPHeaderName"
    """<p>The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to <code>X-Forwarded-For</code>.</p> <note> <p>If the specified header isn't present in the request, WAF doesn't apply the rule to the web request at all.</p> </note>"""
    fallback_behavior: "capo_wafv2.types.fallback_behavior.FallbackBehavior"
    """<p>The match status to assign to the web request if the request doesn't have a valid IP address in the specified position.</p> <note> <p>If the specified header isn't present in the request, WAF doesn't apply the rule to the web request at all.</p> </note> <p>You can specify the following fallback behaviors:</p> <ul> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul>"""
    position: "capo_wafv2.types.forwarded_ip_position.ForwardedIPPosition"
    """<p>The position in the header to search for the IP address. The header can contain IP addresses of the original client and also of proxies. For example, the header value could be <code>10.1.1.1, 127.0.0.0, 10.10.10.10</code> where the first IP address identifies the original client and the rest identify proxies that the request went through. </p> <p>The options for this setting are the following: </p> <ul> <li> <p>FIRST - Inspect the first IP address in the list of IP addresses in the header. This is usually the client's original IP.</p> </li> <li> <p>LAST - Inspect the last IP address in the list of IP addresses in the header.</p> </li> <li> <p>ANY - Inspect all IP addresses in the header for a match. If the header contains more than 10 IP addresses, WAF inspects the last 10.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetForwardedIPConfig) -> dict:
    out: dict = {}
    out["HeaderName"] = value["header_name"]
    import capo_wafv2.types.fallback_behavior

    out["FallbackBehavior"] = capo_wafv2.types.fallback_behavior.serialize_aws_json_1_1(
        value["fallback_behavior"]
    )
    import capo_wafv2.types.forwarded_ip_position

    out["Position"] = capo_wafv2.types.forwarded_ip_position.serialize_aws_json_1_1(
        value["position"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IPSetForwardedIPConfig:
    out: IPSetForwardedIPConfig = {}  # type: ignore[typeddict-item]
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
    if data.get("Position") is not None:
        import capo_wafv2.types.forwarded_ip_position

        out["position"] = (
            capo_wafv2.types.forwarded_ip_position.deserialize_aws_json_1_1(
                data["Position"]
            )
        )
    else:
        import typing

        out["position"] = typing.cast(
            "capo_wafv2.types.forwarded_ip_position.ForwardedIPPosition", ""
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.wafv2#IPSetReferenceStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.ip_set_forwarded_ip_config
    import capo_wafv2.types.resource_arn


class IPSetReferenceStatement(TypedDict, closed=True):
    arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the <a>IPSet</a> that this statement references.</p>"""
    ip_set_forwarded_ip_config: NotRequired[
        "capo_wafv2.types.ip_set_forwarded_ip_config.IPSetForwardedIPConfig"
    ]
    """<p>The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name. </p> <note> <p>If the specified header isn't present in the request, WAF doesn't apply the rule to the web request at all.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetReferenceStatement) -> dict:
    out: dict = {}
    out["ARN"] = value["arn"]
    if "ip_set_forwarded_ip_config" in value:
        import capo_wafv2.types.ip_set_forwarded_ip_config

        out["IPSetForwardedIPConfig"] = (
            capo_wafv2.types.ip_set_forwarded_ip_config.serialize_aws_json_1_1(
                value["ip_set_forwarded_ip_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IPSetReferenceStatement:
    out: IPSetReferenceStatement = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    else:
        out["arn"] = ""
    if data.get("IPSetForwardedIPConfig") is not None:
        import capo_wafv2.types.ip_set_forwarded_ip_config

        out["ip_set_forwarded_ip_config"] = (
            capo_wafv2.types.ip_set_forwarded_ip_config.deserialize_aws_json_1_1(
                data["IPSetForwardedIPConfig"]
            )
        )
    return out

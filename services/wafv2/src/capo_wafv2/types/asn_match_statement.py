"""Generated from Smithy shape ``com.amazonaws.wafv2#AsnMatchStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.asn_list
    import capo_wafv2.types.forwarded_ip_config


class AsnMatchStatement(TypedDict, closed=True):
    asn_list: "capo_wafv2.types.asn_list.AsnList"
    """<p>Contains one or more Autonomous System Numbers (ASNs). ASNs are unique identifiers assigned to large internet networks managed by organizations such as internet service providers, enterprises, universities, or government agencies. </p>"""
    forwarded_ip_config: NotRequired[
        "capo_wafv2.types.forwarded_ip_config.ForwardedIPConfig"
    ]
    """<p>The configuration for inspecting IP addresses to match against an ASN in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsnMatchStatement) -> dict:
    out: dict = {}
    import capo_wafv2.types.asn_list

    out["AsnList"] = capo_wafv2.types.asn_list.serialize_aws_json_1_1(value["asn_list"])
    if "forwarded_ip_config" in value:
        import capo_wafv2.types.forwarded_ip_config

        out["ForwardedIPConfig"] = (
            capo_wafv2.types.forwarded_ip_config.serialize_aws_json_1_1(
                value["forwarded_ip_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AsnMatchStatement:
    out: AsnMatchStatement = {}  # type: ignore[typeddict-item]
    if data.get("AsnList") is not None:
        import capo_wafv2.types.asn_list

        out["asn_list"] = capo_wafv2.types.asn_list.deserialize_aws_json_1_1(
            data["AsnList"]
        )
    else:
        out["asn_list"] = []
    if data.get("ForwardedIPConfig") is not None:
        import capo_wafv2.types.forwarded_ip_config

        out["forwarded_ip_config"] = (
            capo_wafv2.types.forwarded_ip_config.deserialize_aws_json_1_1(
                data["ForwardedIPConfig"]
            )
        )
    return out

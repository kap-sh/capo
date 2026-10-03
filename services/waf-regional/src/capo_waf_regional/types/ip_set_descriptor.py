"""Generated from Smithy shape ``com.amazonaws.wafregional#IPSetDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.ip_set_descriptor_type
    import capo_waf_regional.types.ip_set_descriptor_value


class IPSetDescriptor(TypedDict, closed=True):
    type: "capo_waf_regional.types.ip_set_descriptor_type.IPSetDescriptorType"
    """<p>Specify <code>IPV4</code> or <code>IPV6</code>.</p>"""
    value: "capo_waf_regional.types.ip_set_descriptor_value.IPSetDescriptorValue"
    """<p>Specify an IPv4 address by using CIDR notation. For example:</p> <ul> <li> <p>To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify <code>192.0.2.44/32</code>.</p> </li> <li> <p>To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify <code>192.0.2.0/24</code>.</p> </li> </ul> <p>For more information about CIDR notation, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>.</p> <p>Specify an IPv6 address by using CIDR notation. For example:</p> <ul> <li> <p>To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify <code>1111:0000:0000:0000:0000:0000:0000:0111/128</code>.</p> </li> <li> <p>To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify <code>1111:0000:0000:0000:0000:0000:0000:0000/64</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetDescriptor) -> dict:
    out: dict = {}
    import capo_waf_regional.types.ip_set_descriptor_type

    out["Type"] = capo_waf_regional.types.ip_set_descriptor_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IPSetDescriptor:
    out: IPSetDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_waf_regional.types.ip_set_descriptor_type

        out["type"] = (
            capo_waf_regional.types.ip_set_descriptor_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("IPSetDescriptor.type required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("IPSetDescriptor.value required")
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_boolean_value
    import capo_ec2.types.vpc_id


class ModifyVpcAttributeRequest(TypedDict, closed=True):
    enable_dns_hostnames: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not.</p> <p>You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute. You can only enable DNS hostnames if you've enabled DNS support.</p>"""
    enable_dns_support: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled.</p> <p>You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    enable_network_address_usage_metrics: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether Network Address Usage metrics are enabled for your VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enable_dns_hostnames" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_dns_hostnames"], pairs, f"{key_prefix}EnableDnsHostnames"
        )
    if "enable_dns_support" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_dns_support"], pairs, f"{key_prefix}EnableDnsSupport"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "enable_network_address_usage_metrics" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_network_address_usage_metrics"],
            pairs,
            f"{key_prefix}EnableNetworkAddressUsageMetrics",
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcAttributeRequest:
    out: ModifyVpcAttributeRequest = {}  # type: ignore[typeddict-item]
    child_enable_dns_hostnames = el.find("EnableDnsHostnames")
    if child_enable_dns_hostnames is not None:
        import capo_ec2.types.attribute_boolean_value

        out["enable_dns_hostnames"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_dns_hostnames
            )
        )
    child_enable_dns_support = el.find("EnableDnsSupport")
    if child_enable_dns_support is not None:
        import capo_ec2.types.attribute_boolean_value

        out["enable_dns_support"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_dns_support
            )
        )
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_enable_network_address_usage_metrics = el.find(
        "EnableNetworkAddressUsageMetrics"
    )
    if child_enable_network_address_usage_metrics is not None:
        import capo_ec2.types.attribute_boolean_value

        out["enable_network_address_usage_metrics"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_network_address_usage_metrics
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayVpcAttachmentRequestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.appliance_mode_support_value
    import capo_ec2.types.dns_support_value
    import capo_ec2.types.ipv6_support_value
    import capo_ec2.types.security_group_referencing_support_value


class ModifyTransitGatewayVpcAttachmentRequestOptions(TypedDict, closed=True):
    dns_support: NotRequired["capo_ec2.types.dns_support_value.DnsSupportValue"]
    """<p>Enable or disable DNS support. The default is <code>enable</code>.</p>"""
    security_group_referencing_support: NotRequired[
        "capo_ec2.types.security_group_referencing_support_value.SecurityGroupReferencingSupportValue"
    ]
    """<p>Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management. </p> <p>This option is disabled by default.</p> <p>For more information about security group referencing, see <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security">Security group referencing</a> in the <i>Amazon Web Services Transit Gateways Guide</i>.</p>"""
    ipv6_support: NotRequired["capo_ec2.types.ipv6_support_value.Ipv6SupportValue"]
    """<p>Specifies whether IPv6 support is enabled for the attachment. When enabled, the transit gateway network interface receives an IPv6 address. When you enable route propagation, IPv6 VPC CIDRs propagate to the transit gateway route tables. When disabled, the network interface does not receive an IPv6 address, and IPv6 routes do not propagate. The setting does not filter IPv6 traffic.</p>"""
    appliance_mode_support: NotRequired[
        "capo_ec2.types.appliance_mode_support_value.ApplianceModeSupportValue"
    ]
    """<p>Enable or disable support for appliance mode. If enabled, a traffic flow between a source and destination uses the same Availability Zone for the VPC attachment for the lifetime of that flow. The default is <code>disable</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayVpcAttachmentRequestOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dns_support" in value:
        import capo_ec2.types.dns_support_value

        capo_ec2.types.dns_support_value.serialize_ec2_query(
            value["dns_support"], pairs, f"{key_prefix}DnsSupport"
        )
    if "security_group_referencing_support" in value:
        import capo_ec2.types.security_group_referencing_support_value

        capo_ec2.types.security_group_referencing_support_value.serialize_ec2_query(
            value["security_group_referencing_support"],
            pairs,
            f"{key_prefix}SecurityGroupReferencingSupport",
        )
    if "ipv6_support" in value:
        import capo_ec2.types.ipv6_support_value

        capo_ec2.types.ipv6_support_value.serialize_ec2_query(
            value["ipv6_support"], pairs, f"{key_prefix}Ipv6Support"
        )
    if "appliance_mode_support" in value:
        import capo_ec2.types.appliance_mode_support_value

        capo_ec2.types.appliance_mode_support_value.serialize_ec2_query(
            value["appliance_mode_support"], pairs, f"{key_prefix}ApplianceModeSupport"
        )


def deserialize_ec2_query(
    el: Element,
) -> ModifyTransitGatewayVpcAttachmentRequestOptions:
    out: ModifyTransitGatewayVpcAttachmentRequestOptions = {}  # type: ignore[typeddict-item]
    child_dns_support = el.find("DnsSupport")
    if child_dns_support is not None:
        import capo_ec2.types.dns_support_value

        out["dns_support"] = capo_ec2.types.dns_support_value.deserialize_ec2_query(
            child_dns_support
        )
    child_security_group_referencing_support = el.find(
        "SecurityGroupReferencingSupport"
    )
    if child_security_group_referencing_support is not None:
        import capo_ec2.types.security_group_referencing_support_value

        out["security_group_referencing_support"] = (
            capo_ec2.types.security_group_referencing_support_value.deserialize_ec2_query(
                child_security_group_referencing_support
            )
        )
    child_ipv6_support = el.find("Ipv6Support")
    if child_ipv6_support is not None:
        import capo_ec2.types.ipv6_support_value

        out["ipv6_support"] = capo_ec2.types.ipv6_support_value.deserialize_ec2_query(
            child_ipv6_support
        )
    child_appliance_mode_support = el.find("ApplianceModeSupport")
    if child_appliance_mode_support is not None:
        import capo_ec2.types.appliance_mode_support_value

        out["appliance_mode_support"] = (
            capo_ec2.types.appliance_mode_support_value.deserialize_ec2_query(
                child_appliance_mode_support
            )
        )
    return out

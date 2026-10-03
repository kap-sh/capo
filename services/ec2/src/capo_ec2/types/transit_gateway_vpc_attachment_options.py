"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayVpcAttachmentOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.appliance_mode_support_value
    import capo_ec2.types.dns_support_value
    import capo_ec2.types.ipv6_support_value
    import capo_ec2.types.security_group_referencing_support_value


class TransitGatewayVpcAttachmentOptions(TypedDict, closed=True):
    dns_support: NotRequired["capo_ec2.types.dns_support_value.DnsSupportValue"]
    """<p>Indicates whether DNS support is enabled.</p>"""
    security_group_referencing_support: NotRequired[
        "capo_ec2.types.security_group_referencing_support_value.SecurityGroupReferencingSupportValue"
    ]
    """<p>Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.</p> <p>This option is enabled by default.</p> <p>For more information about security group referencing, see <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security">Security group referencing</a> in the <i>Amazon Web Services Transit Gateways Guide</i>.</p>"""
    ipv6_support: NotRequired["capo_ec2.types.ipv6_support_value.Ipv6SupportValue"]
    """<p>Indicates whether IPv6 support is disabled.</p>"""
    appliance_mode_support: NotRequired[
        "capo_ec2.types.appliance_mode_support_value.ApplianceModeSupportValue"
    ]
    """<p>Indicates whether appliance mode support is enabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayVpcAttachmentOptions, pairs: list[tuple[str, str]], prefix: str
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


def deserialize_ec2_query(el: Element) -> TransitGatewayVpcAttachmentOptions:
    out: TransitGatewayVpcAttachmentOptions = {}  # type: ignore[typeddict-item]
    child_dns_support = el.find("dnsSupport")
    if child_dns_support is not None:
        import capo_ec2.types.dns_support_value

        out["dns_support"] = capo_ec2.types.dns_support_value.deserialize_ec2_query(
            child_dns_support
        )
    child_security_group_referencing_support = el.find(
        "securityGroupReferencingSupport"
    )
    if child_security_group_referencing_support is not None:
        import capo_ec2.types.security_group_referencing_support_value

        out["security_group_referencing_support"] = (
            capo_ec2.types.security_group_referencing_support_value.deserialize_ec2_query(
                child_security_group_referencing_support
            )
        )
    child_ipv6_support = el.find("ipv6Support")
    if child_ipv6_support is not None:
        import capo_ec2.types.ipv6_support_value

        out["ipv6_support"] = capo_ec2.types.ipv6_support_value.deserialize_ec2_query(
            child_ipv6_support
        )
    child_appliance_mode_support = el.find("applianceModeSupport")
    if child_appliance_mode_support is not None:
        import capo_ec2.types.appliance_mode_support_value

        out["appliance_mode_support"] = (
            capo_ec2.types.appliance_mode_support_value.deserialize_ec2_query(
                child_appliance_mode_support
            )
        )
    return out

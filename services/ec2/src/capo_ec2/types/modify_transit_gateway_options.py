"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.auto_accept_shared_attachments_value
    import capo_ec2.types.default_route_table_association_value
    import capo_ec2.types.default_route_table_propagation_value
    import capo_ec2.types.dns_support_value
    import capo_ec2.types.encryption_support_option_value
    import capo_ec2.types.long
    import capo_ec2.types.security_group_referencing_support_value
    import capo_ec2.types.transit_gateway_cidr_block_string_list
    import capo_ec2.types.transit_gateway_route_table_id
    import capo_ec2.types.vpn_ecmp_support_value


class ModifyTransitGatewayOptions(TypedDict, closed=True):
    add_transit_gateway_cidr_blocks: NotRequired[
        "capo_ec2.types.transit_gateway_cidr_block_string_list.TransitGatewayCidrBlockStringList"
    ]
    """<p>Adds IPv4 or IPv6 CIDR blocks for the transit gateway. Must be a size /24 CIDR block or larger for IPv4, or a size /64 CIDR block or larger for IPv6.</p>"""
    remove_transit_gateway_cidr_blocks: NotRequired[
        "capo_ec2.types.transit_gateway_cidr_block_string_list.TransitGatewayCidrBlockStringList"
    ]
    """<p>Removes CIDR blocks for the transit gateway.</p>"""
    vpn_ecmp_support: NotRequired[
        "capo_ec2.types.vpn_ecmp_support_value.VpnEcmpSupportValue"
    ]
    """<p>Enable or disable Equal Cost Multipath Protocol support.</p>"""
    dns_support: NotRequired["capo_ec2.types.dns_support_value.DnsSupportValue"]
    """<p>Enable or disable DNS support.</p>"""
    security_group_referencing_support: NotRequired[
        "capo_ec2.types.security_group_referencing_support_value.SecurityGroupReferencingSupportValue"
    ]
    """<p>Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management. </p> <p>This option is disabled by default.</p> <p>For more information about security group referencing, see <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security">Security group referencing</a> in the <i>Amazon Web Services Transit Gateways Guide</i>.</p>"""
    auto_accept_shared_attachments: NotRequired[
        "capo_ec2.types.auto_accept_shared_attachments_value.AutoAcceptSharedAttachmentsValue"
    ]
    """<p>Enable or disable automatic acceptance of attachment requests.</p>"""
    default_route_table_association: NotRequired[
        "capo_ec2.types.default_route_table_association_value.DefaultRouteTableAssociationValue"
    ]
    """<p>Enable or disable automatic association with the default association route table.</p>"""
    association_default_route_table_id: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the default association route table.</p>"""
    default_route_table_propagation: NotRequired[
        "capo_ec2.types.default_route_table_propagation_value.DefaultRouteTablePropagationValue"
    ]
    """<p>Indicates whether resource attachments automatically propagate routes to the default propagation route table. Enabled by default. If <code>defaultRouteTablePropagation</code> is set to <code>enable</code>, Amazon Web Services Transit Gateway will create the default transit gateway route table.</p>"""
    propagation_default_route_table_id: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the default propagation route table.</p>"""
    amazon_side_asn: NotRequired["capo_ec2.types.long.Long"]
    """<p>A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.</p> <p>The modify ASN operation is not allowed on a transit gateway if it has the following attachments:</p> <ul> <li> <p>Dynamic VPN</p> </li> <li> <p>Static VPN</p> </li> <li> <p>Direct Connect Gateway</p> </li> <li> <p>Connect</p> </li> <li> <p>VPN Concentrator</p> </li> <li> <p>Client VPN</p> </li> </ul> <p>You must first delete all transit gateway attachments configured prior to modifying the ASN on the transit gateway.</p>"""
    encryption_support: NotRequired[
        "capo_ec2.types.encryption_support_option_value.EncryptionSupportOptionValue"
    ]
    """<p>Enable or disable encryption support for VPC Encryption Control.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "add_transit_gateway_cidr_blocks" in value:
        import capo_ec2.types.transit_gateway_cidr_block_string_list

        capo_ec2.types.transit_gateway_cidr_block_string_list.serialize_ec2_query(
            value["add_transit_gateway_cidr_blocks"],
            pairs,
            f"{key_prefix}AddTransitGatewayCidrBlocks",
        )
    if "remove_transit_gateway_cidr_blocks" in value:
        import capo_ec2.types.transit_gateway_cidr_block_string_list

        capo_ec2.types.transit_gateway_cidr_block_string_list.serialize_ec2_query(
            value["remove_transit_gateway_cidr_blocks"],
            pairs,
            f"{key_prefix}RemoveTransitGatewayCidrBlocks",
        )
    if "vpn_ecmp_support" in value:
        import capo_ec2.types.vpn_ecmp_support_value

        capo_ec2.types.vpn_ecmp_support_value.serialize_ec2_query(
            value["vpn_ecmp_support"], pairs, f"{key_prefix}VpnEcmpSupport"
        )
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
    if "auto_accept_shared_attachments" in value:
        import capo_ec2.types.auto_accept_shared_attachments_value

        capo_ec2.types.auto_accept_shared_attachments_value.serialize_ec2_query(
            value["auto_accept_shared_attachments"],
            pairs,
            f"{key_prefix}AutoAcceptSharedAttachments",
        )
    if "default_route_table_association" in value:
        import capo_ec2.types.default_route_table_association_value

        capo_ec2.types.default_route_table_association_value.serialize_ec2_query(
            value["default_route_table_association"],
            pairs,
            f"{key_prefix}DefaultRouteTableAssociation",
        )
    if "association_default_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}AssociationDefaultRouteTableId",
                str(value["association_default_route_table_id"]),
            )
        )
    if "default_route_table_propagation" in value:
        import capo_ec2.types.default_route_table_propagation_value

        capo_ec2.types.default_route_table_propagation_value.serialize_ec2_query(
            value["default_route_table_propagation"],
            pairs,
            f"{key_prefix}DefaultRouteTablePropagation",
        )
    if "propagation_default_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}PropagationDefaultRouteTableId",
                str(value["propagation_default_route_table_id"]),
            )
        )
    if "amazon_side_asn" in value:
        pairs.append((f"{key_prefix}AmazonSideAsn", str(value["amazon_side_asn"])))
    if "encryption_support" in value:
        import capo_ec2.types.encryption_support_option_value

        capo_ec2.types.encryption_support_option_value.serialize_ec2_query(
            value["encryption_support"], pairs, f"{key_prefix}EncryptionSupport"
        )


def deserialize_ec2_query(el: Element) -> ModifyTransitGatewayOptions:
    out: ModifyTransitGatewayOptions = {}  # type: ignore[typeddict-item]
    child_add_transit_gateway_cidr_blocks = el.find("AddTransitGatewayCidrBlocks")
    if child_add_transit_gateway_cidr_blocks is not None:
        import capo_ec2.types.transit_gateway_cidr_block_string_list

        out["add_transit_gateway_cidr_blocks"] = (
            capo_ec2.types.transit_gateway_cidr_block_string_list.deserialize_ec2_query(
                child_add_transit_gateway_cidr_blocks
            )
        )
    child_remove_transit_gateway_cidr_blocks = el.find("RemoveTransitGatewayCidrBlocks")
    if child_remove_transit_gateway_cidr_blocks is not None:
        import capo_ec2.types.transit_gateway_cidr_block_string_list

        out["remove_transit_gateway_cidr_blocks"] = (
            capo_ec2.types.transit_gateway_cidr_block_string_list.deserialize_ec2_query(
                child_remove_transit_gateway_cidr_blocks
            )
        )
    child_vpn_ecmp_support = el.find("VpnEcmpSupport")
    if child_vpn_ecmp_support is not None:
        import capo_ec2.types.vpn_ecmp_support_value

        out["vpn_ecmp_support"] = (
            capo_ec2.types.vpn_ecmp_support_value.deserialize_ec2_query(
                child_vpn_ecmp_support
            )
        )
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
    child_auto_accept_shared_attachments = el.find("AutoAcceptSharedAttachments")
    if child_auto_accept_shared_attachments is not None:
        import capo_ec2.types.auto_accept_shared_attachments_value

        out["auto_accept_shared_attachments"] = (
            capo_ec2.types.auto_accept_shared_attachments_value.deserialize_ec2_query(
                child_auto_accept_shared_attachments
            )
        )
    child_default_route_table_association = el.find("DefaultRouteTableAssociation")
    if child_default_route_table_association is not None:
        import capo_ec2.types.default_route_table_association_value

        out["default_route_table_association"] = (
            capo_ec2.types.default_route_table_association_value.deserialize_ec2_query(
                child_default_route_table_association
            )
        )
    child_association_default_route_table_id = el.find("AssociationDefaultRouteTableId")
    if child_association_default_route_table_id is not None:
        out["association_default_route_table_id"] = str(
            child_association_default_route_table_id.text or ""
        )
    child_default_route_table_propagation = el.find("DefaultRouteTablePropagation")
    if child_default_route_table_propagation is not None:
        import capo_ec2.types.default_route_table_propagation_value

        out["default_route_table_propagation"] = (
            capo_ec2.types.default_route_table_propagation_value.deserialize_ec2_query(
                child_default_route_table_propagation
            )
        )
    child_propagation_default_route_table_id = el.find("PropagationDefaultRouteTableId")
    if child_propagation_default_route_table_id is not None:
        out["propagation_default_route_table_id"] = str(
            child_propagation_default_route_table_id.text or ""
        )
    child_amazon_side_asn = el.find("AmazonSideAsn")
    if child_amazon_side_asn is not None:
        out["amazon_side_asn"] = int(child_amazon_side_asn.text or "")
    child_encryption_support = el.find("EncryptionSupport")
    if child_encryption_support is not None:
        import capo_ec2.types.encryption_support_option_value

        out["encryption_support"] = (
            capo_ec2.types.encryption_support_option_value.deserialize_ec2_query(
                child_encryption_support
            )
        )
    return out

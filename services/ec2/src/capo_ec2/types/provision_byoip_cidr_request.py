"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionByoipCidrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.cidr_authorization_context
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class ProvisionByoipCidrRequest(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The public IPv4 or IPv6 address range, in CIDR notation. The most specific IPv4 prefix that you can specify is /24. The most specific IPv6 address range that you can bring is /48 for CIDRs that are publicly advertisable and /56 for CIDRs that are not publicly advertisable. The address range cannot overlap with another address range that you've brought to this or another Region.</p>"""
    cidr_authorization_context: NotRequired[
        "capo_ec2.types.cidr_authorization_context.CidrAuthorizationContext"
    ]
    """<p>A signed document that proves that you are authorized to bring the specified IP address range to Amazon using BYOIP.</p>"""
    publicly_advertisable: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>(IPv6 only) Indicate whether the address range will be publicly advertised to the internet.</p> <p>Default: true</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the address range and the address pool.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    pool_tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the address pool.</p>"""
    multi_region: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Reserved.</p>"""
    network_border_group: NotRequired["capo_ec2.types.string.String"]
    """<p>If you have <a href="https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html">Local Zones</a> enabled, you can choose a network border group for Local Zones when you provision and advertise a BYOIPv4 CIDR. Choose the network border group carefully as the EIP and the Amazon Web Services resource it is associated with must reside in the same network border group.</p> <p>You can provision BYOIP address ranges to and advertise them in the following Local Zone network border groups:</p> <ul> <li> <p>us-east-1-dfw-2</p> </li> <li> <p>us-west-2-lax-1</p> </li> <li> <p>us-west-2-phx-2</p> </li> </ul> <note> <p>You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this time.</p> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProvisionByoipCidrRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "cidr_authorization_context" in value:
        import capo_ec2.types.cidr_authorization_context

        capo_ec2.types.cidr_authorization_context.serialize_ec2_query(
            value["cidr_authorization_context"],
            pairs,
            f"{key_prefix}CidrAuthorizationContext",
        )
    if "publicly_advertisable" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAdvertisable",
                "true" if value["publicly_advertisable"] else "false",
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "pool_tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["pool_tag_specifications"], pairs, f"{key_prefix}PoolTagSpecification"
        )
    if "multi_region" in value:
        pairs.append(
            (f"{key_prefix}MultiRegion", "true" if value["multi_region"] else "false")
        )
    if "network_border_group" in value:
        pairs.append(
            (f"{key_prefix}NetworkBorderGroup", str(value["network_border_group"]))
        )


def deserialize_ec2_query(el: Element) -> ProvisionByoipCidrRequest:
    out: ProvisionByoipCidrRequest = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_cidr_authorization_context = el.find("CidrAuthorizationContext")
    if child_cidr_authorization_context is not None:
        import capo_ec2.types.cidr_authorization_context

        out["cidr_authorization_context"] = (
            capo_ec2.types.cidr_authorization_context.deserialize_ec2_query(
                child_cidr_authorization_context
            )
        )
    child_publicly_advertisable = el.find("PubliclyAdvertisable")
    if child_publicly_advertisable is not None:
        out["publicly_advertisable"] = (
            child_publicly_advertisable.text or ""
        ).lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_pool_tag_specifications = el.find("PoolTagSpecification")
    if child_pool_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["pool_tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_pool_tag_specifications
            )
        )
    child_multi_region = el.find("MultiRegion")
    if child_multi_region is not None:
        out["multi_region"] = (child_multi_region.text or "").lower() == "true"
    child_network_border_group = el.find("NetworkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    return out

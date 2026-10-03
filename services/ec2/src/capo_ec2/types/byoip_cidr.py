"""Generated from Smithy shape ``com.amazonaws.ec2#ByoipCidr``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.asn_association_set
    import capo_ec2.types.byoip_cidr_state
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.string


class ByoipCidr(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The address range, in CIDR notation.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the address range.</p>"""
    asn_associations: NotRequired[
        "capo_ec2.types.asn_association_set.AsnAssociationSet"
    ]
    """<p>The BYOIP CIDR associations with ASNs.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>Upon success, contains the ID of the address pool. Otherwise, contains an error message.</p>"""
    state: NotRequired["capo_ec2.types.byoip_cidr_state.ByoipCidrState"]
    """<p>The state of the address range.</p> <ul> <li> <p> <code>advertised</code>: The address range is being advertised to the internet by Amazon Web Services.</p> </li> <li> <p> <code>deprovisioned</code>: The address range is deprovisioned.</p> </li> <li> <p> <code>failed-deprovision</code>: The request to deprovision the address range was unsuccessful. Ensure that all EIPs from the range have been deallocated and try again.</p> </li> <li> <p> <code>failed-provision</code>: The request to provision the address range was unsuccessful.</p> </li> <li> <p> <code>pending-deprovision</code>: You’ve submitted a request to deprovision an address range and it's pending.</p> </li> <li> <p> <code>pending-provision</code>: You’ve submitted a request to provision an address range and it's pending.</p> </li> <li> <p> <code>provisioned</code>: The address range is provisioned and can be advertised. The range is not currently advertised.</p> </li> <li> <p> <code>provisioned-not-publicly-advertisable</code>: The address range is provisioned and cannot be advertised.</p> </li> </ul>"""
    network_border_group: NotRequired["capo_ec2.types.string.String"]
    """<p>If you have <a href="https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html">Local Zones</a> enabled, you can choose a network border group for Local Zones when you provision and advertise a BYOIPv4 CIDR. Choose the network border group carefully as the EIP and the Amazon Web Services resource it is associated with must reside in the same network border group.</p> <p>You can provision BYOIP address ranges to and advertise them in the following Local Zone network border groups:</p> <ul> <li> <p>us-east-1-dfw-2</p> </li> <li> <p>us-west-2-lax-1</p> </li> <li> <p>us-west-2-phx-2</p> </li> </ul> <note> <p>You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this time.</p> </note>"""
    advertisement_type: NotRequired["capo_ec2.types.string.String"]
    """<p>Specifies the advertisement method for the BYOIP CIDR. Valid values are:</p> <ul> <li> <p> <code>unicast</code>: IP is advertised from a single location (regional services like EC2)</p> </li> <li> <p> <code>anycast</code>: IP is advertised from multiple global locations simultaneously (global services like CloudFront)</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-cloudfront.html">Bring your own IP to CloudFront using IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    pool_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the address pool associated with the CIDR.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool associated with the CIDR.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ByoipCidr, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "asn_associations" in value:
        import capo_ec2.types.asn_association_set

        capo_ec2.types.asn_association_set.serialize_ec2_query(
            value["asn_associations"], pairs, f"{key_prefix}AsnAssociationSet"
        )
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))
    if "state" in value:
        import capo_ec2.types.byoip_cidr_state

        capo_ec2.types.byoip_cidr_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "network_border_group" in value:
        pairs.append(
            (f"{key_prefix}NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "advertisement_type" in value:
        pairs.append(
            (f"{key_prefix}AdvertisementType", str(value["advertisement_type"]))
        )
    if "pool_id" in value:
        pairs.append((f"{key_prefix}PoolId", str(value["pool_id"])))
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))


def deserialize_ec2_query(el: Element) -> ByoipCidr:
    out: ByoipCidr = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_asn_associations = el.find("asnAssociationSet")
    if child_asn_associations is not None:
        import capo_ec2.types.asn_association_set

        out["asn_associations"] = (
            capo_ec2.types.asn_association_set.deserialize_ec2_query(
                child_asn_associations
            )
        )
    child_status_message = el.find("statusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.byoip_cidr_state

        out["state"] = capo_ec2.types.byoip_cidr_state.deserialize_ec2_query(
            child_state
        )
    child_network_border_group = el.find("networkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    child_advertisement_type = el.find("advertisementType")
    if child_advertisement_type is not None:
        out["advertisement_type"] = str(child_advertisement_type.text or "")
    child_pool_id = el.find("poolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    child_ipam_pool_id = el.find("ipamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolCidr``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.ipam_pool_cidr_failure_reason
    import capo_ec2.types.ipam_pool_cidr_id
    import capo_ec2.types.ipam_pool_cidr_state
    import capo_ec2.types.string


class IpamPoolCidr(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR provisioned to the IPAM pool. A CIDR is a representation of an IP address and its associated network mask (or netmask) and refers to a range of IP addresses. An IPv4 CIDR example is <code>10.24.34.0/23</code>. An IPv6 CIDR example is <code>2001:DB8::/32</code>.</p>"""
    state: NotRequired["capo_ec2.types.ipam_pool_cidr_state.IpamPoolCidrState"]
    """<p>The state of the CIDR.</p>"""
    failure_reason: NotRequired[
        "capo_ec2.types.ipam_pool_cidr_failure_reason.IpamPoolCidrFailureReason"
    ]
    """<p>Details related to why an IPAM pool CIDR failed to be provisioned.</p>"""
    ipam_pool_cidr_id: NotRequired["capo_ec2.types.ipam_pool_cidr_id.IpamPoolCidrId"]
    """<p>The IPAM pool CIDR ID.</p>"""
    netmask_length: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The netmask length of the CIDR you'd like to provision to a pool. Can be used for provisioning Amazon-provided IPv6 CIDRs to top-level pools and for provisioning CIDRs to pools with source pools. Cannot be used to provision BYOIP CIDRs to top-level pools. "NetmaskLength" or "Cidr" is required.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPoolCidr, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "state" in value:
        import capo_ec2.types.ipam_pool_cidr_state

        capo_ec2.types.ipam_pool_cidr_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "failure_reason" in value:
        import capo_ec2.types.ipam_pool_cidr_failure_reason

        capo_ec2.types.ipam_pool_cidr_failure_reason.serialize_ec2_query(
            value["failure_reason"], pairs, f"{key_prefix}FailureReason"
        )
    if "ipam_pool_cidr_id" in value:
        pairs.append((f"{key_prefix}IpamPoolCidrId", str(value["ipam_pool_cidr_id"])))
    if "netmask_length" in value:
        pairs.append((f"{key_prefix}NetmaskLength", str(value["netmask_length"])))


def deserialize_ec2_query(el: Element) -> IpamPoolCidr:
    out: IpamPoolCidr = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_pool_cidr_state

        out["state"] = capo_ec2.types.ipam_pool_cidr_state.deserialize_ec2_query(
            child_state
        )
    child_failure_reason = el.find("failureReason")
    if child_failure_reason is not None:
        import capo_ec2.types.ipam_pool_cidr_failure_reason

        out["failure_reason"] = (
            capo_ec2.types.ipam_pool_cidr_failure_reason.deserialize_ec2_query(
                child_failure_reason
            )
        )
    child_ipam_pool_cidr_id = el.find("ipamPoolCidrId")
    if child_ipam_pool_cidr_id is not None:
        out["ipam_pool_cidr_id"] = str(child_ipam_pool_cidr_id.text or "")
    child_netmask_length = el.find("netmaskLength")
    if child_netmask_length is not None:
        out["netmask_length"] = int(child_netmask_length.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateIpamPoolCidrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.ipam_pool_allocation_allowed_cidrs
    import capo_ec2.types.ipam_pool_allocation_disallowed_cidrs
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class AllocateIpamPoolCidrRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool from which you would like to allocate a CIDR.</p>"""
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR you would like to allocate from the IPAM pool. Note the following:</p> <ul> <li> <p>If there is no DefaultNetmaskLength allocation rule set on the pool, you must specify either the NetmaskLength or the CIDR.</p> </li> <li> <p>If the DefaultNetmaskLength allocation rule is set on the pool, you can specify either the NetmaskLength or the CIDR and the DefaultNetmaskLength allocation rule will be ignored.</p> </li> </ul> <p>Possible values: Any available IPv4 or IPv6 CIDR.</p>"""
    netmask_length: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The netmask length of the CIDR you would like to allocate from the IPAM pool. Note the following:</p> <ul> <li> <p>If there is no DefaultNetmaskLength allocation rule set on the pool, you must specify either the NetmaskLength or the CIDR.</p> </li> <li> <p>If the DefaultNetmaskLength allocation rule is set on the pool, you can specify either the NetmaskLength or the CIDR and the DefaultNetmaskLength allocation rule will be ignored.</p> </li> </ul> <p>Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the allocation.</p>"""
    preview_next_cidr: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A preview of the next available CIDR in a pool.</p>"""
    allowed_cidrs: NotRequired[
        "capo_ec2.types.ipam_pool_allocation_allowed_cidrs.IpamPoolAllocationAllowedCidrs"
    ]
    """<p>Include a particular CIDR range that can be returned by the pool. Allowed CIDRs are only allowed if using netmask length for allocation.</p>"""
    disallowed_cidrs: NotRequired[
        "capo_ec2.types.ipam_pool_allocation_disallowed_cidrs.IpamPoolAllocationDisallowedCidrs"
    ]
    """<p>Exclude a particular CIDR range from being returned by the pool. Disallowed CIDRs are only allowed if using netmask length for allocation.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> <p>If you specify tags, the request is authorized against the allocation resource in addition to the pool resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllocateIpamPoolCidrRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "netmask_length" in value:
        pairs.append((f"{key_prefix}NetmaskLength", str(value["netmask_length"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "preview_next_cidr" in value:
        pairs.append(
            (
                f"{key_prefix}PreviewNextCidr",
                "true" if value["preview_next_cidr"] else "false",
            )
        )
    if "allowed_cidrs" in value:
        import capo_ec2.types.ipam_pool_allocation_allowed_cidrs

        capo_ec2.types.ipam_pool_allocation_allowed_cidrs.serialize_ec2_query(
            value["allowed_cidrs"], pairs, f"{key_prefix}AllowedCidr"
        )
    if "disallowed_cidrs" in value:
        import capo_ec2.types.ipam_pool_allocation_disallowed_cidrs

        capo_ec2.types.ipam_pool_allocation_disallowed_cidrs.serialize_ec2_query(
            value["disallowed_cidrs"], pairs, f"{key_prefix}DisallowedCidr"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> AllocateIpamPoolCidrRequest:
    out: AllocateIpamPoolCidrRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_netmask_length = el.find("NetmaskLength")
    if child_netmask_length is not None:
        out["netmask_length"] = int(child_netmask_length.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_preview_next_cidr = el.find("PreviewNextCidr")
    if child_preview_next_cidr is not None:
        out["preview_next_cidr"] = (
            child_preview_next_cidr.text or ""
        ).lower() == "true"
    child_allowed_cidrs = el.find("AllowedCidr")
    if child_allowed_cidrs is not None:
        import capo_ec2.types.ipam_pool_allocation_allowed_cidrs

        out["allowed_cidrs"] = (
            capo_ec2.types.ipam_pool_allocation_allowed_cidrs.deserialize_ec2_query(
                child_allowed_cidrs
            )
        )
    child_disallowed_cidrs = el.find("DisallowedCidr")
    if child_disallowed_cidrs is not None:
        import capo_ec2.types.ipam_pool_allocation_disallowed_cidrs

        out["disallowed_cidrs"] = (
            capo_ec2.types.ipam_pool_allocation_disallowed_cidrs.deserialize_ec2_query(
                child_disallowed_cidrs
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    return out

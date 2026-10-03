"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_netmask_length
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.request_ipam_resource_tag_list
    import capo_ec2.types.string


class ModifyIpamPoolRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool you want to modify.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the IPAM pool you want to modify.</p>"""
    auto_import: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If true, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only. </p> <p>A locale must be set on the pool for this feature to work.</p>"""
    allocation_min_netmask_length: NotRequired[
        "capo_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128. The minimum netmask length must be less than the maximum netmask length.</p>"""
    allocation_max_netmask_length: NotRequired[
        "capo_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.The maximum netmask length must be greater than the minimum netmask length.</p>"""
    allocation_default_netmask_length: NotRequired[
        "capo_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.</p>"""
    clear_allocation_default_netmask_length: NotRequired[
        "capo_ec2.types.boolean.Boolean"
    ]
    """<p>Clear the default netmask length allocation rule for this pool.</p>"""
    add_allocation_resource_tags: NotRequired[
        "capo_ec2.types.request_ipam_resource_tag_list.RequestIpamResourceTagList"
    ]
    """<p>Add tag allocation rules to a pool. For more information about allocation rules, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/create-top-ipam.html">Create a top-level pool</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    remove_allocation_resource_tags: NotRequired[
        "capo_ec2.types.request_ipam_resource_tag_list.RequestIpamResourceTagList"
    ]
    """<p>Remove tag allocation rules from a pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamPoolRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "auto_import" in value:
        pairs.append(
            (f"{key_prefix}AutoImport", "true" if value["auto_import"] else "false")
        )
    if "allocation_min_netmask_length" in value:
        pairs.append(
            (
                f"{key_prefix}AllocationMinNetmaskLength",
                str(value["allocation_min_netmask_length"]),
            )
        )
    if "allocation_max_netmask_length" in value:
        pairs.append(
            (
                f"{key_prefix}AllocationMaxNetmaskLength",
                str(value["allocation_max_netmask_length"]),
            )
        )
    if "allocation_default_netmask_length" in value:
        pairs.append(
            (
                f"{key_prefix}AllocationDefaultNetmaskLength",
                str(value["allocation_default_netmask_length"]),
            )
        )
    if "clear_allocation_default_netmask_length" in value:
        pairs.append(
            (
                f"{key_prefix}ClearAllocationDefaultNetmaskLength",
                "true" if value["clear_allocation_default_netmask_length"] else "false",
            )
        )
    if "add_allocation_resource_tags" in value:
        import capo_ec2.types.request_ipam_resource_tag_list

        capo_ec2.types.request_ipam_resource_tag_list.serialize_ec2_query(
            value["add_allocation_resource_tags"],
            pairs,
            f"{key_prefix}AddAllocationResourceTag",
        )
    if "remove_allocation_resource_tags" in value:
        import capo_ec2.types.request_ipam_resource_tag_list

        capo_ec2.types.request_ipam_resource_tag_list.serialize_ec2_query(
            value["remove_allocation_resource_tags"],
            pairs,
            f"{key_prefix}RemoveAllocationResourceTag",
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamPoolRequest:
    out: ModifyIpamPoolRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_auto_import = el.find("AutoImport")
    if child_auto_import is not None:
        out["auto_import"] = (child_auto_import.text or "").lower() == "true"
    child_allocation_min_netmask_length = el.find("AllocationMinNetmaskLength")
    if child_allocation_min_netmask_length is not None:
        out["allocation_min_netmask_length"] = int(
            child_allocation_min_netmask_length.text or ""
        )
    child_allocation_max_netmask_length = el.find("AllocationMaxNetmaskLength")
    if child_allocation_max_netmask_length is not None:
        out["allocation_max_netmask_length"] = int(
            child_allocation_max_netmask_length.text or ""
        )
    child_allocation_default_netmask_length = el.find("AllocationDefaultNetmaskLength")
    if child_allocation_default_netmask_length is not None:
        out["allocation_default_netmask_length"] = int(
            child_allocation_default_netmask_length.text or ""
        )
    child_clear_allocation_default_netmask_length = el.find(
        "ClearAllocationDefaultNetmaskLength"
    )
    if child_clear_allocation_default_netmask_length is not None:
        out["clear_allocation_default_netmask_length"] = (
            child_clear_allocation_default_netmask_length.text or ""
        ).lower() == "true"
    child_add_allocation_resource_tags = el.find("AddAllocationResourceTag")
    if child_add_allocation_resource_tags is not None:
        import capo_ec2.types.request_ipam_resource_tag_list

        out["add_allocation_resource_tags"] = (
            capo_ec2.types.request_ipam_resource_tag_list.deserialize_ec2_query(
                child_add_allocation_resource_tags
            )
        )
    child_remove_allocation_resource_tags = el.find("RemoveAllocationResourceTag")
    if child_remove_allocation_resource_tags is not None:
        import capo_ec2.types.request_ipam_resource_tag_list

        out["remove_allocation_resource_tags"] = (
            capo_ec2.types.request_ipam_resource_tag_list.deserialize_ec2_query(
                child_remove_allocation_resource_tags
            )
        )
    return out

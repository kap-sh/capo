"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceCidr``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boxed_double
    import capo_ec2.types.ipam_compliance_status
    import capo_ec2.types.ipam_id
    import capo_ec2.types.ipam_management_state
    import capo_ec2.types.ipam_overlap_status
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.ipam_resource_tag_list
    import capo_ec2.types.ipam_resource_type
    import capo_ec2.types.ipam_scope_id
    import capo_ec2.types.string


class IpamResourceCidr(TypedDict, closed=True):
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>The IPAM ID for an IPAM resource.</p>"""
    ipam_scope_id: NotRequired["capo_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The scope ID for an IPAM resource.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The pool ID for an IPAM resource.</p>"""
    resource_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region for an IPAM resource.</p>"""
    resource_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account number of the owner of an IPAM resource.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of an IPAM resource.</p>"""
    resource_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of an IPAM resource.</p>"""
    resource_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR for an IPAM resource.</p>"""
    resource_type: NotRequired["capo_ec2.types.ipam_resource_type.IpamResourceType"]
    """<p>The type of IPAM resource.</p>"""
    resource_tags: NotRequired[
        "capo_ec2.types.ipam_resource_tag_list.IpamResourceTagList"
    ]
    """<p>The tags for an IPAM resource.</p>"""
    ip_usage: NotRequired["capo_ec2.types.boxed_double.BoxedDouble"]
    """<p>The percentage of IP address space in use. To convert the decimal to a percentage, multiply the decimal by 100. Note the following:</p> <ul> <li> <p>For resources that are VPCs, this is the percentage of IP address space in the VPC that's taken up by subnet CIDRs. </p> </li> <li> <p>For resources that are subnets, if the subnet has an IPv4 CIDR provisioned to it, this is the percentage of IPv4 address space in the subnet that's in use. If the subnet has an IPv6 CIDR provisioned to it, the percentage of IPv6 address space in use is not represented. The percentage of IPv6 address space in use cannot currently be calculated. </p> </li> <li> <p>For resources that are public IPv4 pools, this is the percentage of IP address space in the pool that's been allocated to Elastic IP addresses (EIPs). </p> </li> </ul>"""
    compliance_status: NotRequired[
        "capo_ec2.types.ipam_compliance_status.IpamComplianceStatus"
    ]
    """<p>The compliance status of the IPAM resource. For more information on compliance statuses, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html">Monitor CIDR usage by resource</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    management_state: NotRequired[
        "capo_ec2.types.ipam_management_state.IpamManagementState"
    ]
    """<p>The management state of the resource. For more information about management states, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html">Monitor CIDR usage by resource</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    overlap_status: NotRequired["capo_ec2.types.ipam_overlap_status.IpamOverlapStatus"]
    """<p>The overlap status of an IPAM resource. The overlap status tells you if the CIDR for a resource overlaps with another CIDR in the scope. For more information on overlap statuses, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html">Monitor CIDR usage by resource</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of a VPC.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamResourceCidr, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))
    if "ipam_scope_id" in value:
        pairs.append((f"{key_prefix}IpamScopeId", str(value["ipam_scope_id"])))
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))
    if "resource_region" in value:
        pairs.append((f"{key_prefix}ResourceRegion", str(value["resource_region"])))
    if "resource_owner_id" in value:
        pairs.append((f"{key_prefix}ResourceOwnerId", str(value["resource_owner_id"])))
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_name" in value:
        pairs.append((f"{key_prefix}ResourceName", str(value["resource_name"])))
    if "resource_cidr" in value:
        pairs.append((f"{key_prefix}ResourceCidr", str(value["resource_cidr"])))
    if "resource_type" in value:
        import capo_ec2.types.ipam_resource_type

        capo_ec2.types.ipam_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "resource_tags" in value:
        import capo_ec2.types.ipam_resource_tag_list

        capo_ec2.types.ipam_resource_tag_list.serialize_ec2_query(
            value["resource_tags"], pairs, f"{key_prefix}ResourceTagSet"
        )
    if "ip_usage" in value:
        pairs.append(
            (
                f"{key_prefix}IpUsage",
                (
                    "NaN"
                    if value["ip_usage"] != value["ip_usage"]
                    else "Infinity"
                    if value["ip_usage"] == float("inf")
                    else "-Infinity"
                    if value["ip_usage"] == float("-inf")
                    else str(value["ip_usage"])
                ),
            )
        )
    if "compliance_status" in value:
        import capo_ec2.types.ipam_compliance_status

        capo_ec2.types.ipam_compliance_status.serialize_ec2_query(
            value["compliance_status"], pairs, f"{key_prefix}ComplianceStatus"
        )
    if "management_state" in value:
        import capo_ec2.types.ipam_management_state

        capo_ec2.types.ipam_management_state.serialize_ec2_query(
            value["management_state"], pairs, f"{key_prefix}ManagementState"
        )
    if "overlap_status" in value:
        import capo_ec2.types.ipam_overlap_status

        capo_ec2.types.ipam_overlap_status.serialize_ec2_query(
            value["overlap_status"], pairs, f"{key_prefix}OverlapStatus"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> IpamResourceCidr:
    out: IpamResourceCidr = {}  # type: ignore[typeddict-item]
    child_ipam_id = el.find("ipamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_ipam_scope_id = el.find("ipamScopeId")
    if child_ipam_scope_id is not None:
        out["ipam_scope_id"] = str(child_ipam_scope_id.text or "")
    child_ipam_pool_id = el.find("ipamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_resource_region = el.find("resourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_resource_owner_id = el.find("resourceOwnerId")
    if child_resource_owner_id is not None:
        out["resource_owner_id"] = str(child_resource_owner_id.text or "")
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_name = el.find("resourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_resource_cidr = el.find("resourceCidr")
    if child_resource_cidr is not None:
        out["resource_cidr"] = str(child_resource_cidr.text or "")
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        import capo_ec2.types.ipam_resource_type

        out["resource_type"] = capo_ec2.types.ipam_resource_type.deserialize_ec2_query(
            child_resource_type
        )
    child_resource_tags = el.find("resourceTagSet")
    if child_resource_tags is not None:
        import capo_ec2.types.ipam_resource_tag_list

        out["resource_tags"] = (
            capo_ec2.types.ipam_resource_tag_list.deserialize_ec2_query(
                child_resource_tags
            )
        )
    child_ip_usage = el.find("ipUsage")
    if child_ip_usage is not None:
        out["ip_usage"] = float(child_ip_usage.text or "")
    child_compliance_status = el.find("complianceStatus")
    if child_compliance_status is not None:
        import capo_ec2.types.ipam_compliance_status

        out["compliance_status"] = (
            capo_ec2.types.ipam_compliance_status.deserialize_ec2_query(
                child_compliance_status
            )
        )
    child_management_state = el.find("managementState")
    if child_management_state is not None:
        import capo_ec2.types.ipam_management_state

        out["management_state"] = (
            capo_ec2.types.ipam_management_state.deserialize_ec2_query(
                child_management_state
            )
        )
    child_overlap_status = el.find("overlapStatus")
    if child_overlap_status is not None:
        import capo_ec2.types.ipam_overlap_status

        out["overlap_status"] = (
            capo_ec2.types.ipam_overlap_status.deserialize_ec2_query(
                child_overlap_status
            )
        )
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out

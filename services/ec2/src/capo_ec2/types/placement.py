"""Generated from Smithy shape ``com.amazonaws.ec2#Placement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.integer
    import capo_ec2.types.placement_group_id
    import capo_ec2.types.placement_group_name
    import capo_ec2.types.string
    import capo_ec2.types.tenancy


class Placement(TypedDict, closed=True):
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the instance.</p> <p>On input, you can specify <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code>, but not both. If you specify neither one, Amazon EC2 automatically selects an Availability Zone for you.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet">CreateFleet</a>.</p>"""
    affinity: NotRequired["capo_ec2.types.string.String"]
    """<p>The affinity setting for the instance on the Dedicated Host.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet">CreateFleet</a> or <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html">ImportInstance</a>.</p>"""
    group_name: NotRequired["capo_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group that the instance is in.</p> <p>On input, you can specify <code>GroupId</code> or <code>GroupName</code>, but not both.</p>"""
    partition_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of the partition that the instance is in. Valid only if the placement group strategy is set to <code>partition</code>.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet">CreateFleet</a>.</p>"""
    host_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Dedicated Host on which the instance resides.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet">CreateFleet</a> or <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html">ImportInstance</a>.</p>"""
    tenancy: NotRequired["capo_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance. An instance with a tenancy of <code>dedicated</code> runs on single-tenant hardware.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet">CreateFleet</a>. The <code>host</code> tenancy is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html">ImportInstance</a> or for T3 instances that are configured for the <code>unlimited</code> CPU credit option.</p>"""
    spread_domain: NotRequired["capo_ec2.types.string.String"]
    """<p>Reserved for future use.</p>"""
    host_resource_group_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the host resource group in which to launch the instances.</p> <p>On input, if you specify this parameter, either omit the <b>Tenancy</b> parameter or set it to <code>host</code>.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet">CreateFleet</a>.</p>"""
    group_id: NotRequired["capo_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>The ID of the placement group that the instance is in.</p> <p>On input, you can specify <code>GroupId</code> or <code>GroupName</code>, but not both.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone of the instance.</p> <p>On input, you can specify <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code>, but not both. If you specify neither one, Amazon EC2 automatically selects an Availability Zone for you.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet">CreateFleet</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Placement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "affinity" in value:
        pairs.append((f"{key_prefix}Affinity", str(value["affinity"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "partition_number" in value:
        pairs.append((f"{key_prefix}PartitionNumber", str(value["partition_number"])))
    if "host_id" in value:
        pairs.append((f"{key_prefix}HostId", str(value["host_id"])))
    if "tenancy" in value:
        import capo_ec2.types.tenancy

        capo_ec2.types.tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{key_prefix}Tenancy"
        )
    if "spread_domain" in value:
        pairs.append((f"{key_prefix}SpreadDomain", str(value["spread_domain"])))
    if "host_resource_group_arn" in value:
        pairs.append(
            (f"{key_prefix}HostResourceGroupArn", str(value["host_resource_group_arn"]))
        )
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))


def deserialize_ec2_query(el: Element) -> Placement:
    out: Placement = {}  # type: ignore[typeddict-item]
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_affinity = el.find("affinity")
    if child_affinity is not None:
        out["affinity"] = str(child_affinity.text or "")
    child_group_name = el.find("groupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_partition_number = el.find("partitionNumber")
    if child_partition_number is not None:
        out["partition_number"] = int(child_partition_number.text or "")
    child_host_id = el.find("hostId")
    if child_host_id is not None:
        out["host_id"] = str(child_host_id.text or "")
    child_tenancy = el.find("tenancy")
    if child_tenancy is not None:
        import capo_ec2.types.tenancy

        out["tenancy"] = capo_ec2.types.tenancy.deserialize_ec2_query(child_tenancy)
    child_spread_domain = el.find("spreadDomain")
    if child_spread_domain is not None:
        out["spread_domain"] = str(child_spread_domain.text or "")
    child_host_resource_group_arn = el.find("hostResourceGroupArn")
    if child_host_resource_group_arn is not None:
        out["host_resource_group_arn"] = str(child_host_resource_group_arn.text or "")
    child_group_id = el.find("groupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.efs#MountTargetDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.availability_zone_id
    import capo_efs.types.availability_zone_name
    import capo_efs.types.aws_account_id
    import capo_efs.types.file_system_id
    import capo_efs.types.ip_address
    import capo_efs.types.ipv6_address
    import capo_efs.types.life_cycle_state
    import capo_efs.types.mount_target_id
    import capo_efs.types.network_interface_id
    import capo_efs.types.subnet_id
    import capo_efs.types.vpc_id


class MountTargetDescription(TypedDict, closed=True):
    owner_id: NotRequired["capo_efs.types.aws_account_id.AwsAccountId"]
    """<p>Amazon Web Services account ID that owns the resource.</p>"""
    mount_target_id: "capo_efs.types.mount_target_id.MountTargetId"
    """<p>System-assigned mount target ID.</p>"""
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system for which the mount target is intended.</p>"""
    subnet_id: "capo_efs.types.subnet_id.SubnetId"
    """<p>The ID of the mount target's subnet.</p>"""
    life_cycle_state: "capo_efs.types.life_cycle_state.LifeCycleState"
    """<p>Lifecycle state of the mount target.</p>"""
    ip_address: NotRequired["capo_efs.types.ip_address.IpAddress"]
    """<p>Address at which the file system can be mounted by using the mount target.</p>"""
    ipv6_address: NotRequired["capo_efs.types.ipv6_address.Ipv6Address"]
    """<p>The IPv6 address for the mount target.</p>"""
    network_interface_id: NotRequired[
        "capo_efs.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface that Amazon EFS created when it created the mount target.</p>"""
    availability_zone_id: NotRequired[
        "capo_efs.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The unique and consistent identifier of the Availability Zone that the mount target resides in. For example, <code>use1-az1</code> is an AZ ID for the us-east-1 Region and it has the same location in every Amazon Web Services account.</p>"""
    availability_zone_name: NotRequired[
        "capo_efs.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The name of the Availability Zone in which the mount target is located. Availability Zones are independently mapped to names for each Amazon Web Services account. For example, the Availability Zone <code>us-east-1a</code> for your Amazon Web Services account might not be the same location as <code>us-east-1a</code> for another Amazon Web Services account.</p>"""
    vpc_id: NotRequired["capo_efs.types.vpc_id.VpcId"]
    """<p>The virtual private cloud (VPC) ID that the mount target is configured in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MountTargetDescription) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    out["MountTargetId"] = value["mount_target_id"]
    out["FileSystemId"] = value["file_system_id"]
    out["SubnetId"] = value["subnet_id"]
    import capo_efs.types.life_cycle_state

    out["LifeCycleState"] = capo_efs.types.life_cycle_state.serialize_json(
        value["life_cycle_state"]
    )
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "ipv6_address" in value:
        out["Ipv6Address"] = value["ipv6_address"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "availability_zone_name" in value:
        out["AvailabilityZoneName"] = value["availability_zone_name"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> MountTargetDescription:
    out: MountTargetDescription = {}  # type: ignore[typeddict-item]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    if data.get("MountTargetId") is not None:
        out["mount_target_id"] = data["MountTargetId"]
    else:
        out["mount_target_id"] = ""
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    else:
        out["file_system_id"] = ""
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    else:
        out["subnet_id"] = ""
    if data.get("LifeCycleState") is not None:
        import capo_efs.types.life_cycle_state

        out["life_cycle_state"] = capo_efs.types.life_cycle_state.deserialize_json(
            data["LifeCycleState"]
        )
    else:
        import typing

        out["life_cycle_state"] = typing.cast(
            "capo_efs.types.life_cycle_state.LifeCycleState", ""
        )
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("Ipv6Address") is not None:
        out["ipv6_address"] = data["Ipv6Address"]
    if data.get("NetworkInterfaceId") is not None:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if data.get("AvailabilityZoneId") is not None:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if data.get("AvailabilityZoneName") is not None:
        out["availability_zone_name"] = data["AvailabilityZoneName"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    return out

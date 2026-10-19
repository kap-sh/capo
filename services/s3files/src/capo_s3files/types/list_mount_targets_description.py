"""Generated from Smithy shape ``com.amazonaws.s3files#ListMountTargetsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.availability_zone_id
    import capo_s3files.types.aws_account_id
    import capo_s3files.types.file_system_id
    import capo_s3files.types.ipv4_address
    import capo_s3files.types.ipv6_address
    import capo_s3files.types.life_cycle_state
    import capo_s3files.types.mount_target_id
    import capo_s3files.types.network_interface_id
    import capo_s3files.types.status_message
    import capo_s3files.types.subnet_id
    import capo_s3files.types.vpc_id


class ListMountTargetsDescription(TypedDict, closed=True):
    availability_zone_id: NotRequired[
        "capo_s3files.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The Availability Zone ID where the mount target is located.</p>"""
    file_system_id: NotRequired["capo_s3files.types.file_system_id.FileSystemId"]
    """<p>The ID of the S3 File System.</p>"""
    ipv4_address: NotRequired["capo_s3files.types.ipv4_address.Ipv4Address"]
    """<p>The IPv4 address of the mount target.</p>"""
    ipv6_address: NotRequired["capo_s3files.types.ipv6_address.Ipv6Address"]
    """<p>The IPv6 address of the mount target.</p>"""
    status: NotRequired["capo_s3files.types.life_cycle_state.LifeCycleState"]
    """<p>The current status of the mount target.</p>"""
    status_message: NotRequired["capo_s3files.types.status_message.StatusMessage"]
    """<p>Additional information about the mount target status.</p>"""
    mount_target_id: "capo_s3files.types.mount_target_id.MountTargetId"
    """<p>The ID of the mount target.</p>"""
    network_interface_id: NotRequired[
        "capo_s3files.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface associated with the mount target.</p>"""
    owner_id: "capo_s3files.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the mount target owner.</p>"""
    subnet_id: "capo_s3files.types.subnet_id.SubnetId"
    """<p>The ID of the subnet where the mount target is located.</p>"""
    vpc_id: NotRequired["capo_s3files.types.vpc_id.VpcId"]
    """<p>The ID of the VPC where the mount target is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMountTargetsDescription) -> dict:
    out: dict = {}
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "file_system_id" in value:
        out["fileSystemId"] = value["file_system_id"]
    if "ipv4_address" in value:
        out["ipv4Address"] = value["ipv4_address"]
    if "ipv6_address" in value:
        out["ipv6Address"] = value["ipv6_address"]
    if "status" in value:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    out["mountTargetId"] = value["mount_target_id"]
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    out["ownerId"] = value["owner_id"]
    out["subnetId"] = value["subnet_id"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> ListMountTargetsDescription:
    out: ListMountTargetsDescription = {}  # type: ignore[typeddict-item]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    if data.get("ipv4Address") is not None:
        out["ipv4_address"] = data["ipv4Address"]
    if data.get("ipv6Address") is not None:
        out["ipv6_address"] = data["ipv6Address"]
    if data.get("status") is not None:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("mountTargetId") is not None:
        out["mount_target_id"] = data["mountTargetId"]
    else:
        out["mount_target_id"] = ""
    if data.get("networkInterfaceId") is not None:
        out["network_interface_id"] = data["networkInterfaceId"]
    if data.get("ownerId") is not None:
        out["owner_id"] = data["ownerId"]
    else:
        out["owner_id"] = ""
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    else:
        out["subnet_id"] = ""
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    return out

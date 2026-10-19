"""Generated from Smithy shape ``com.amazonaws.s3files#CreateMountTargetResponse``."""

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
    import capo_s3files.types.security_groups
    import capo_s3files.types.status_message
    import capo_s3files.types.subnet_id
    import capo_s3files.types.vpc_id


class CreateMountTargetResponse(TypedDict, closed=True):
    availability_zone_id: NotRequired[
        "capo_s3files.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The unique and consistent identifier of the Availability Zone where the mount target is located. For example, <code>use1-az1</code> is an Availability Zone ID for the <code>us-east-1</code> Amazon Web Services Region, and it has the same location in every Amazon Web Services account.</p>"""
    owner_id: "capo_s3files.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the mount target owner.</p>"""
    mount_target_id: "capo_s3files.types.mount_target_id.MountTargetId"
    """<p>The ID of the mount target, assigned by S3 Files. This ID is used to reference the mount target in subsequent API calls.</p>"""
    file_system_id: NotRequired["capo_s3files.types.file_system_id.FileSystemId"]
    """<p>The ID of the S3 File System associated with the mount target.</p>"""
    subnet_id: "capo_s3files.types.subnet_id.SubnetId"
    """<p>The ID of the subnet where the mount target is located.</p>"""
    ipv4_address: NotRequired["capo_s3files.types.ipv4_address.Ipv4Address"]
    """<p>The IPv4 address assigned to the mount target.</p>"""
    ipv6_address: NotRequired["capo_s3files.types.ipv6_address.Ipv6Address"]
    """<p>The IPv6 address assigned to the mount target.</p>"""
    network_interface_id: NotRequired[
        "capo_s3files.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface that S3 Files created when it created the mount target. This network interface is managed by the service.</p>"""
    vpc_id: NotRequired["capo_s3files.types.vpc_id.VpcId"]
    """<p>The ID of the VPC where the mount target is located.</p>"""
    security_groups: NotRequired["capo_s3files.types.security_groups.SecurityGroups"]
    """<p>The security groups associated with the mount target's network interface.</p>"""
    status: NotRequired["capo_s3files.types.life_cycle_state.LifeCycleState"]
    """<p>The lifecycle state of the mount target. Valid values are: <code>AVAILABLE</code> (the mount target is available for use), <code>CREATING</code> (the mount target is being created), <code>DELETING</code> (the mount target is being deleted), <code>DELETED</code> (the mount target has been deleted), or <code>ERROR</code> (the mount target is in an error state), or <code>UPDATING</code> (the mount target is being updated).</p>"""
    status_message: NotRequired["capo_s3files.types.status_message.StatusMessage"]
    """<p>Additional information about the mount target status. This field provides more details when the status is <code>ERROR</code>, or during state transitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMountTargetResponse) -> dict:
    out: dict = {}
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    out["ownerId"] = value["owner_id"]
    out["mountTargetId"] = value["mount_target_id"]
    if "file_system_id" in value:
        out["fileSystemId"] = value["file_system_id"]
    out["subnetId"] = value["subnet_id"]
    if "ipv4_address" in value:
        out["ipv4Address"] = value["ipv4_address"]
    if "ipv6_address" in value:
        out["ipv6Address"] = value["ipv6_address"]
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "security_groups" in value:
        import capo_s3files.types.security_groups

        out["securityGroups"] = capo_s3files.types.security_groups.serialize_json(
            value["security_groups"]
        )
    if "status" in value:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> CreateMountTargetResponse:
    out: CreateMountTargetResponse = {}  # type: ignore[typeddict-item]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("ownerId") is not None:
        out["owner_id"] = data["ownerId"]
    else:
        out["owner_id"] = ""
    if data.get("mountTargetId") is not None:
        out["mount_target_id"] = data["mountTargetId"]
    else:
        out["mount_target_id"] = ""
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    else:
        out["subnet_id"] = ""
    if data.get("ipv4Address") is not None:
        out["ipv4_address"] = data["ipv4Address"]
    if data.get("ipv6Address") is not None:
        out["ipv6_address"] = data["ipv6Address"]
    if data.get("networkInterfaceId") is not None:
        out["network_interface_id"] = data["networkInterfaceId"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("securityGroups") is not None:
        import capo_s3files.types.security_groups

        out["security_groups"] = capo_s3files.types.security_groups.deserialize_json(
            data["securityGroups"]
        )
    if data.get("status") is not None:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out

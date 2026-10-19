"""Generated from Smithy shape ``com.amazonaws.s3files#CreateMountTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.file_system_id
    import capo_s3files.types.ip_address_type
    import capo_s3files.types.ipv4_address
    import capo_s3files.types.ipv6_address
    import capo_s3files.types.security_groups
    import capo_s3files.types.subnet_id


class CreateMountTargetRequest(TypedDict, closed=True):
    file_system_id: "capo_s3files.types.file_system_id.FileSystemId"
    """<p>The ID or Amazon Resource Name (ARN) of the S3 File System to create the mount target for.</p>"""
    subnet_id: "capo_s3files.types.subnet_id.SubnetId"
    """<p>The ID of the subnet where the mount target will be created. The subnet must be in the same Amazon Web Services Region as the file system. For file systems with regional availability, you can create mount targets in any subnet within the Region. The subnet determines the Availability Zone where the mount target will be located.</p>"""
    ipv4_address: NotRequired["capo_s3files.types.ipv4_address.Ipv4Address"]
    """<p>A specific IPv4 address to assign to the mount target. If not specified and the IP address type supports IPv4, an address is automatically assigned from the subnet's available IPv4 address range. The address must be within the subnet's CIDR block and not already in use.</p>"""
    ipv6_address: NotRequired["capo_s3files.types.ipv6_address.Ipv6Address"]
    """<p>A specific IPv6 address to assign to the mount target. If not specified and the IP address type supports IPv6, an address is automatically assigned from the subnet's available IPv6 address range. The address must be within the subnet's IPv6 CIDR block and not already in use.</p>"""
    ip_address_type: NotRequired["capo_s3files.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the mount target. If not specified, <code>IPV4_ONLY</code> is used. The IP address type must match the IP configuration of the specified subnet.</p>"""
    security_groups: NotRequired["capo_s3files.types.security_groups.SecurityGroups"]
    """<p>An array of VPC security group IDs to associate with the mount target's network interface. These security groups control network access to the mount target. If not specified, the default security group for the subnet's VPC is used. All security groups must belong to the same VPC as the subnet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMountTargetRequest) -> dict:
    out: dict = {}
    out["fileSystemId"] = value["file_system_id"]
    out["subnetId"] = value["subnet_id"]
    if "ipv4_address" in value:
        out["ipv4Address"] = value["ipv4_address"]
    if "ipv6_address" in value:
        out["ipv6Address"] = value["ipv6_address"]
    if "ip_address_type" in value:
        import capo_s3files.types.ip_address_type

        out["ipAddressType"] = capo_s3files.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "security_groups" in value:
        import capo_s3files.types.security_groups

        out["securityGroups"] = capo_s3files.types.security_groups.serialize_json(
            value["security_groups"]
        )
    return out


def deserialize_json(data: dict) -> CreateMountTargetRequest:
    out: CreateMountTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    else:
        out["file_system_id"] = ""
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    else:
        out["subnet_id"] = ""
    if data.get("ipv4Address") is not None:
        out["ipv4_address"] = data["ipv4Address"]
    if data.get("ipv6Address") is not None:
        out["ipv6_address"] = data["ipv6Address"]
    if data.get("ipAddressType") is not None:
        import capo_s3files.types.ip_address_type

        out["ip_address_type"] = capo_s3files.types.ip_address_type.deserialize_json(
            data["ipAddressType"]
        )
    if data.get("securityGroups") is not None:
        import capo_s3files.types.security_groups

        out["security_groups"] = capo_s3files.types.security_groups.deserialize_json(
            data["securityGroups"]
        )
    return out

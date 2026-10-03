"""Generated from Smithy shape ``com.amazonaws.efs#CreateMountTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_efs.types.file_system_id
    import capo_efs.types.ip_address
    import capo_efs.types.ip_address_type
    import capo_efs.types.ipv6_address
    import capo_efs.types.security_groups
    import capo_efs.types.subnet_id


class CreateMountTargetRequest(TypedDict, closed=True):
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system for which to create the mount target.</p>"""
    subnet_id: "capo_efs.types.subnet_id.SubnetId"
    """<p>The ID of the subnet to add the mount target in. For One Zone file systems, use the subnet that is associated with the file system's Availability Zone.</p>"""
    ip_address: NotRequired["capo_efs.types.ip_address.IpAddress"]
    """<p>If the IP address type for the mount target is IPv4, then specify the IPv4 address within the address range of the specified subnet.</p>"""
    ipv6_address: NotRequired["capo_efs.types.ipv6_address.Ipv6Address"]
    """<p>If the IP address type for the mount target is IPv6, then specify the IPv6 address within the address range of the specified subnet.</p>"""
    ip_address_type: NotRequired["capo_efs.types.ip_address_type.IpAddressType"]
    """<p>Specify the type of IP address of the mount target you are creating. Options are IPv4, dual stack, or IPv6. If you don’t specify an IpAddressType, then IPv4 is used.</p> <ul> <li> <p>IPV4_ONLY – Create mount target with IPv4 only subnet or dual-stack subnet.</p> </li> <li> <p>DUAL_STACK – Create mount target with dual-stack subnet.</p> </li> <li> <p>IPV6_ONLY – Create mount target with IPv6 only subnet.</p> </li> </ul> <note> <p>Creating IPv6 mount target only ENI in dual-stack subnet is not supported.</p> </note>"""
    security_groups: NotRequired["capo_efs.types.security_groups.SecurityGroups"]
    """<p>VPC security group IDs, of the form <code>sg-xxxxxxxx</code>. These must be for the same VPC as the subnet specified. The maximum number of security groups depends on account quota. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html">Amazon VPC Quotas</a> in the <i>Amazon VPC User Guide</i> (see the <b>Security Groups</b> table). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMountTargetRequest) -> dict:
    out: dict = {}
    out["FileSystemId"] = value["file_system_id"]
    out["SubnetId"] = value["subnet_id"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "ipv6_address" in value:
        out["Ipv6Address"] = value["ipv6_address"]
    if "ip_address_type" in value:
        import capo_efs.types.ip_address_type

        out["IpAddressType"] = capo_efs.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "security_groups" in value:
        import capo_efs.types.security_groups

        out["SecurityGroups"] = capo_efs.types.security_groups.serialize_json(
            value["security_groups"]
        )
    return out


def deserialize_json(data: dict) -> CreateMountTargetRequest:
    out: CreateMountTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    else:
        raise DeserializationError("CreateMountTargetRequest.file_system_id required")
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    else:
        raise DeserializationError("CreateMountTargetRequest.subnet_id required")
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("Ipv6Address") is not None:
        out["ipv6_address"] = data["Ipv6Address"]
    if data.get("IpAddressType") is not None:
        import capo_efs.types.ip_address_type

        out["ip_address_type"] = capo_efs.types.ip_address_type.deserialize_json(
            data["IpAddressType"]
        )
    if data.get("SecurityGroups") is not None:
        import capo_efs.types.security_groups

        out["security_groups"] = capo_efs.types.security_groups.deserialize_json(
            data["SecurityGroups"]
        )
    return out

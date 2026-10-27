"""Generated from Smithy shape ``com.amazonaws.deadline#HostPropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.host_name
    import capo_deadline.types.instance_type
    import capo_deadline.types.ip_addresses
    import capo_deadline.types.string


class HostPropertiesResponse(TypedDict, closed=True):
    ip_addresses: NotRequired["capo_deadline.types.ip_addresses.IpAddresses"]
    """The IP address of the host."""
    host_name: NotRequired["capo_deadline.types.host_name.HostName"]
    """The host name."""
    ec2_instance_arn: NotRequired["capo_deadline.types.string.String"]
    """The ARN of the host EC2 instance."""
    ec2_instance_type: NotRequired["capo_deadline.types.instance_type.InstanceType"]
    """The instance type of the host EC2 instance."""


# --- restJson1 ser/de ---
def serialize_json(value: HostPropertiesResponse) -> dict:
    out: dict = {}
    if "ip_addresses" in value:
        import capo_deadline.types.ip_addresses

        out["ipAddresses"] = capo_deadline.types.ip_addresses.serialize_json(
            value["ip_addresses"]
        )
    if "host_name" in value:
        out["hostName"] = value["host_name"]
    if "ec2_instance_arn" in value:
        out["ec2InstanceArn"] = value["ec2_instance_arn"]
    if "ec2_instance_type" in value:
        out["ec2InstanceType"] = value["ec2_instance_type"]
    return out


def deserialize_json(data: dict) -> HostPropertiesResponse:
    out: HostPropertiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ipAddresses") is not None:
        import capo_deadline.types.ip_addresses

        out["ip_addresses"] = capo_deadline.types.ip_addresses.deserialize_json(
            data["ipAddresses"]
        )
    if data.get("hostName") is not None:
        out["host_name"] = data["hostName"]
    if data.get("ec2InstanceArn") is not None:
        out["ec2_instance_arn"] = data["ec2InstanceArn"]
    if data.get("ec2InstanceType") is not None:
        out["ec2_instance_type"] = data["ec2InstanceType"]
    return out

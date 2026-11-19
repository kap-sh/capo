"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryConnectSettingsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.availability_zones
    import capo_directory_service.types.ip_addrs
    import capo_directory_service.types.ip_v6_addrs
    import capo_directory_service.types.security_group_id
    import capo_directory_service.types.subnet_ids
    import capo_directory_service.types.user_name
    import capo_directory_service.types.vpc_id


class DirectoryConnectSettingsDescription(TypedDict, closed=True):
    vpc_id: NotRequired["capo_directory_service.types.vpc_id.VpcId"]
    """<p>The identifier of the VPC that the AD Connector is in.</p>"""
    subnet_ids: NotRequired["capo_directory_service.types.subnet_ids.SubnetIds"]
    """<p>A list of subnet identifiers in the VPC that the AD Connector is in.</p>"""
    customer_user_name: NotRequired["capo_directory_service.types.user_name.UserName"]
    """<p>The user name of the service account in your self-managed directory.</p>"""
    security_group_id: NotRequired[
        "capo_directory_service.types.security_group_id.SecurityGroupId"
    ]
    """<p>The security group identifier for the AD Connector directory.</p>"""
    availability_zones: NotRequired[
        "capo_directory_service.types.availability_zones.AvailabilityZones"
    ]
    """<p>The Availability Zones that the directory is in.</p>"""
    connect_ips: NotRequired["capo_directory_service.types.ip_addrs.IpAddrs"]
    """<p>The IP addresses of the AD Connector servers.</p>"""
    connect_ips_v6: NotRequired["capo_directory_service.types.ip_v6_addrs.IpV6Addrs"]
    """<p>The IPv6 addresses of the AD Connector servers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryConnectSettingsDescription) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_directory_service.types.subnet_ids

        out["SubnetIds"] = (
            capo_directory_service.types.subnet_ids.serialize_aws_json_1_1(
                value["subnet_ids"]
            )
        )
    if "customer_user_name" in value:
        out["CustomerUserName"] = value["customer_user_name"]
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "availability_zones" in value:
        import capo_directory_service.types.availability_zones

        out["AvailabilityZones"] = (
            capo_directory_service.types.availability_zones.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    if "connect_ips" in value:
        import capo_directory_service.types.ip_addrs

        out["ConnectIps"] = (
            capo_directory_service.types.ip_addrs.serialize_aws_json_1_1(
                value["connect_ips"]
            )
        )
    if "connect_ips_v6" in value:
        import capo_directory_service.types.ip_v6_addrs

        out["ConnectIpsV6"] = (
            capo_directory_service.types.ip_v6_addrs.serialize_aws_json_1_1(
                value["connect_ips_v6"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryConnectSettingsDescription:
    out: DirectoryConnectSettingsDescription = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetIds") is not None:
        import capo_directory_service.types.subnet_ids

        out["subnet_ids"] = (
            capo_directory_service.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    if data.get("CustomerUserName") is not None:
        out["customer_user_name"] = data["CustomerUserName"]
    if data.get("SecurityGroupId") is not None:
        out["security_group_id"] = data["SecurityGroupId"]
    if data.get("AvailabilityZones") is not None:
        import capo_directory_service.types.availability_zones

        out["availability_zones"] = (
            capo_directory_service.types.availability_zones.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    if data.get("ConnectIps") is not None:
        import capo_directory_service.types.ip_addrs

        out["connect_ips"] = (
            capo_directory_service.types.ip_addrs.deserialize_aws_json_1_1(
                data["ConnectIps"]
            )
        )
    if data.get("ConnectIpsV6") is not None:
        import capo_directory_service.types.ip_v6_addrs

        out["connect_ips_v6"] = (
            capo_directory_service.types.ip_v6_addrs.deserialize_aws_json_1_1(
                data["ConnectIpsV6"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryConnectSettingsDescription) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_directory_service.types.subnet_ids

        out["SubnetIds"] = capo_directory_service.types.subnet_ids.serialize_cbor(
            value["subnet_ids"]
        )
    if "customer_user_name" in value:
        out["CustomerUserName"] = value["customer_user_name"]
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "availability_zones" in value:
        import capo_directory_service.types.availability_zones

        out["AvailabilityZones"] = (
            capo_directory_service.types.availability_zones.serialize_cbor(
                value["availability_zones"]
            )
        )
    if "connect_ips" in value:
        import capo_directory_service.types.ip_addrs

        out["ConnectIps"] = capo_directory_service.types.ip_addrs.serialize_cbor(
            value["connect_ips"]
        )
    if "connect_ips_v6" in value:
        import capo_directory_service.types.ip_v6_addrs

        out["ConnectIpsV6"] = capo_directory_service.types.ip_v6_addrs.serialize_cbor(
            value["connect_ips_v6"]
        )
    return out


def deserialize_cbor(data: dict) -> DirectoryConnectSettingsDescription:
    out: DirectoryConnectSettingsDescription = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetIds") is not None:
        import capo_directory_service.types.subnet_ids

        out["subnet_ids"] = capo_directory_service.types.subnet_ids.deserialize_cbor(
            data["SubnetIds"]
        )
    if data.get("CustomerUserName") is not None:
        out["customer_user_name"] = data["CustomerUserName"]
    if data.get("SecurityGroupId") is not None:
        out["security_group_id"] = data["SecurityGroupId"]
    if data.get("AvailabilityZones") is not None:
        import capo_directory_service.types.availability_zones

        out["availability_zones"] = (
            capo_directory_service.types.availability_zones.deserialize_cbor(
                data["AvailabilityZones"]
            )
        )
    if data.get("ConnectIps") is not None:
        import capo_directory_service.types.ip_addrs

        out["connect_ips"] = capo_directory_service.types.ip_addrs.deserialize_cbor(
            data["ConnectIps"]
        )
    if data.get("ConnectIpsV6") is not None:
        import capo_directory_service.types.ip_v6_addrs

        out["connect_ips_v6"] = (
            capo_directory_service.types.ip_v6_addrs.deserialize_cbor(
                data["ConnectIpsV6"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryVpcSettingsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.availability_zones
    import capo_directory_service.types.security_group_id
    import capo_directory_service.types.subnet_ids
    import capo_directory_service.types.vpc_id


class DirectoryVpcSettingsDescription(TypedDict, closed=True):
    vpc_id: NotRequired["capo_directory_service.types.vpc_id.VpcId"]
    """<p>The identifier of the VPC that the directory is in.</p>"""
    subnet_ids: NotRequired["capo_directory_service.types.subnet_ids.SubnetIds"]
    """<p>The identifiers of the subnets for the directory servers.</p>"""
    security_group_id: NotRequired[
        "capo_directory_service.types.security_group_id.SecurityGroupId"
    ]
    """<p>The domain controller security group identifier for the directory.</p>"""
    availability_zones: NotRequired[
        "capo_directory_service.types.availability_zones.AvailabilityZones"
    ]
    """<p>The list of Availability Zones that the directory is in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryVpcSettingsDescription) -> dict:
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
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "availability_zones" in value:
        import capo_directory_service.types.availability_zones

        out["AvailabilityZones"] = (
            capo_directory_service.types.availability_zones.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryVpcSettingsDescription:
    out: DirectoryVpcSettingsDescription = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetIds") is not None:
        import capo_directory_service.types.subnet_ids

        out["subnet_ids"] = (
            capo_directory_service.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    if data.get("SecurityGroupId") is not None:
        out["security_group_id"] = data["SecurityGroupId"]
    if data.get("AvailabilityZones") is not None:
        import capo_directory_service.types.availability_zones

        out["availability_zones"] = (
            capo_directory_service.types.availability_zones.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryVpcSettingsDescription) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_directory_service.types.subnet_ids

        out["SubnetIds"] = capo_directory_service.types.subnet_ids.serialize_cbor(
            value["subnet_ids"]
        )
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "availability_zones" in value:
        import capo_directory_service.types.availability_zones

        out["AvailabilityZones"] = (
            capo_directory_service.types.availability_zones.serialize_cbor(
                value["availability_zones"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DirectoryVpcSettingsDescription:
    out: DirectoryVpcSettingsDescription = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetIds") is not None:
        import capo_directory_service.types.subnet_ids

        out["subnet_ids"] = capo_directory_service.types.subnet_ids.deserialize_cbor(
            data["SubnetIds"]
        )
    if data.get("SecurityGroupId") is not None:
        out["security_group_id"] = data["SecurityGroupId"]
    if data.get("AvailabilityZones") is not None:
        import capo_directory_service.types.availability_zones

        out["availability_zones"] = (
            capo_directory_service.types.availability_zones.deserialize_cbor(
                data["AvailabilityZones"]
            )
        )
    return out

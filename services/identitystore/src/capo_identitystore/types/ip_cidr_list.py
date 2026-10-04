"""Generated from Smithy shape ``com.amazonaws.identitystore#IpCidrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.ip_cidr_type

IpCidrList: TypeAlias = list["capo_identitystore.types.ip_cidr_type.IpCidrType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpCidrList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IpCidrList:
    return [item for item in data if item is not None]

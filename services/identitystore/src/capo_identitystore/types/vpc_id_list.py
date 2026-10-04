"""Generated from Smithy shape ``com.amazonaws.identitystore#VpcIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.vpc_id_type

VpcIdList: TypeAlias = list["capo_identitystore.types.vpc_id_type.VpcIdType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VpcIdList:
    return [item for item in data if item is not None]

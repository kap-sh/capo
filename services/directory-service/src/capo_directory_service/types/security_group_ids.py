"""Generated from Smithy shape ``com.amazonaws.directoryservice#SecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.security_group_id

SecurityGroupIds: TypeAlias = list[
    "capo_directory_service.types.security_group_id.SecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecurityGroupIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SecurityGroupIds:
    return [item for item in data if item is not None]

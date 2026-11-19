"""Generated from Smithy shape ``com.amazonaws.codeconnections#SecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.security_group_id

SecurityGroupIds: TypeAlias = list[
    "capo_codeconnections.types.security_group_id.SecurityGroupId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SecurityGroupIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SecurityGroupIds:
    return [item for item in data if item is not None]

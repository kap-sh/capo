"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupIdFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.protection_group_id

ProtectionGroupIdFilters: TypeAlias = list[
    "capo_shield.types.protection_group_id.ProtectionGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupIdFilters) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProtectionGroupIdFilters:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionGroupIdFilters) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProtectionGroupIdFilters:
    return [item for item in data if item is not None]

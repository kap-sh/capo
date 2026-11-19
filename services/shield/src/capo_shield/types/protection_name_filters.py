"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionNameFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.protection_name

ProtectionNameFilters: TypeAlias = list[
    "capo_shield.types.protection_name.ProtectionName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionNameFilters) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProtectionNameFilters:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionNameFilters) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProtectionNameFilters:
    return [item for item in data if item is not None]

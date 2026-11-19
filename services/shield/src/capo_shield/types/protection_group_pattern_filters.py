"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupPatternFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.protection_group_pattern

ProtectionGroupPatternFilters: TypeAlias = list[
    "capo_shield.types.protection_group_pattern.ProtectionGroupPattern"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupPatternFilters) -> list:
    import capo_shield.types.protection_group_pattern

    out: list = []
    for item in value:
        out.append(
            capo_shield.types.protection_group_pattern.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectionGroupPatternFilters:
    import capo_shield.types.protection_group_pattern

    out: ProtectionGroupPatternFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_shield.types.protection_group_pattern.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionGroupPatternFilters) -> list:
    import capo_shield.types.protection_group_pattern

    out: list = []
    for item in value:
        out.append(capo_shield.types.protection_group_pattern.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProtectionGroupPatternFilters:
    import capo_shield.types.protection_group_pattern

    out: ProtectionGroupPatternFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.protection_group_pattern.deserialize_cbor(item))
    return out

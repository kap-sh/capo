"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupAggregationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.protection_group_aggregation

ProtectionGroupAggregationFilters: TypeAlias = list[
    "capo_shield.types.protection_group_aggregation.ProtectionGroupAggregation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupAggregationFilters) -> list:
    import capo_shield.types.protection_group_aggregation

    out: list = []
    for item in value:
        out.append(
            capo_shield.types.protection_group_aggregation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectionGroupAggregationFilters:
    import capo_shield.types.protection_group_aggregation

    out: ProtectionGroupAggregationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_shield.types.protection_group_aggregation.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionGroupAggregationFilters) -> list:
    import capo_shield.types.protection_group_aggregation

    out: list = []
    for item in value:
        out.append(capo_shield.types.protection_group_aggregation.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProtectionGroupAggregationFilters:
    import capo_shield.types.protection_group_aggregation

    out: ProtectionGroupAggregationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_shield.types.protection_group_aggregation.deserialize_cbor(item)
        )
    return out

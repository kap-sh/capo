"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#FilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.filter_value

FilterValueList: TypeAlias = list[
    "capo_marketplace_agreement.types.filter_value.FilterValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FilterValueList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterValueList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> FilterValueList:
    return [item for item in data if item is not None]

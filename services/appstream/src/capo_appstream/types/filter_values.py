"""Generated from Smithy shape ``com.amazonaws.appstream#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.filter_value

FilterValues: TypeAlias = list["capo_appstream.types.filter_value.FilterValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FilterValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> FilterValues:
    return [item for item in data if item is not None]

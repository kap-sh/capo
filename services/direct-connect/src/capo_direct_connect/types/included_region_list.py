"""Generated from Smithy shape ``com.amazonaws.directconnect#IncludedRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.region

IncludedRegionList: TypeAlias = list["capo_direct_connect.types.region.Region"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncludedRegionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IncludedRegionList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IncludedRegionList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> IncludedRegionList:
    return [item for item in data if item is not None]

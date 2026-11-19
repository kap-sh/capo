"""Generated from Smithy shape ``com.amazonaws.directconnect#AsPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.long_asn

AsPathList: TypeAlias = list["capo_direct_connect.types.long_asn.LongAsn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsPathList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AsPathList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AsPathList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AsPathList:
    return [item for item in data if item is not None]

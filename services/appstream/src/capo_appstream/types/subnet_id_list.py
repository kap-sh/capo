"""Generated from Smithy shape ``com.amazonaws.appstream#SubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.string

SubnetIdList: TypeAlias = list["capo_appstream.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubnetIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SubnetIdList:
    return [item for item in data if item is not None]

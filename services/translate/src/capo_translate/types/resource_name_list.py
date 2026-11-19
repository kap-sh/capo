"""Generated from Smithy shape ``com.amazonaws.translate#ResourceNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_translate.types.resource_name

ResourceNameList: TypeAlias = list["capo_translate.types.resource_name.ResourceName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceNameList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceNameList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ResourceNameList:
    return [item for item in data if item is not None]

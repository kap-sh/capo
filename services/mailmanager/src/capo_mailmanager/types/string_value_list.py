"""Generated from Smithy shape ``com.amazonaws.mailmanager#StringValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.string_value

StringValueList: TypeAlias = list["capo_mailmanager.types.string_value.StringValue"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringValueList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StringValueList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StringValueList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> StringValueList:
    return [item for item in data if item is not None]

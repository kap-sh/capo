"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StringList``."""

from typing import TypeAlias

StringList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StringList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StringList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> StringList:
    return [item for item in data if item is not None]

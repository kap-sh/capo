"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Resources``."""

from typing import TypeAlias

Resources: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Resources) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Resources:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Resources) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Resources:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AwsServicesList``."""

from typing import TypeAlias

AwsServicesList: TypeAlias = list["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AwsServicesList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AwsServicesList:
    return [item for item in data if item is not None]

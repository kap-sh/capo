"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AwsServiceFilterList``."""

from typing import TypeAlias

AwsServiceFilterList: TypeAlias = list["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AwsServiceFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AwsServiceFilterList:
    return [item for item in data if item is not None]

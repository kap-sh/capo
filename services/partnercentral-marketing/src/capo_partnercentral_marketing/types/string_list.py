"""Generated from Smithy shape ``aws.auth#StringList``."""

from typing import TypeAlias

StringList: TypeAlias = list["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StringList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> StringList:
    return [item for item in data if item is not None]

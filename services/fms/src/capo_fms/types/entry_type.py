"""Generated from Smithy shape ``com.amazonaws.fms#EntryType``."""

from typing import Literal, TypeAlias, cast

EntryType: TypeAlias = Literal[
    "FMS_MANAGED_FIRST_ENTRY",
    "FMS_MANAGED_LAST_ENTRY",
    "CUSTOM_ENTRY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntryType:
    return cast(EntryType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntryType) -> str:
    return value


def deserialize_cbor(data: str) -> EntryType:
    return cast(EntryType, data)

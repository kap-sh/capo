"""Generated from Smithy shape ``com.amazonaws.snowball#TransferOption``."""

from typing import Literal, TypeAlias, cast

TransferOption: TypeAlias = Literal[
    "IMPORT",
    "EXPORT",
    "LOCAL_USE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransferOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransferOption:
    return cast(TransferOption, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TransferOption) -> str:
    return value


def deserialize_cbor(data: str) -> TransferOption:
    return cast(TransferOption, data)

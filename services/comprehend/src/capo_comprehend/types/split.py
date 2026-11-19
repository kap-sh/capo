"""Generated from Smithy shape ``com.amazonaws.comprehend#Split``."""

from typing import Literal, TypeAlias, cast

Split: TypeAlias = Literal[
    "TRAIN",
    "TEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Split) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Split:
    return cast(Split, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Split) -> str:
    return value


def deserialize_cbor(data: str) -> Split:
    return cast(Split, data)

"""Generated from Smithy shape ``com.amazonaws.snowball#SnowballCapacity``."""

from typing import Literal, TypeAlias, cast

SnowballCapacity: TypeAlias = Literal[
    "T50",
    "T80",
    "T100",
    "T42",
    "T98",
    "T8",
    "T14",
    "T32",
    "NoPreference",
    "T240",
    "T13",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowballCapacity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnowballCapacity:
    return cast(SnowballCapacity, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnowballCapacity) -> str:
    return value


def deserialize_cbor(data: str) -> SnowballCapacity:
    return cast(SnowballCapacity, data)

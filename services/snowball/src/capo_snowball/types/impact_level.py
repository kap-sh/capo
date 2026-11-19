"""Generated from Smithy shape ``com.amazonaws.snowball#ImpactLevel``."""

from typing import Literal, TypeAlias, cast

ImpactLevel: TypeAlias = Literal[
    "IL2",
    "IL4",
    "IL5",
    "IL6",
    "IL99",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpactLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImpactLevel:
    return cast(ImpactLevel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImpactLevel) -> str:
    return value


def deserialize_cbor(data: str) -> ImpactLevel:
    return cast(ImpactLevel, data)

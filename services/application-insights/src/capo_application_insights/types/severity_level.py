"""Generated from Smithy shape ``com.amazonaws.applicationinsights#SeverityLevel``."""

from typing import Literal, TypeAlias, cast

SeverityLevel: TypeAlias = Literal[
    "Informative",
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SeverityLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SeverityLevel:
    return cast(SeverityLevel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SeverityLevel) -> str:
    return value


def deserialize_cbor(data: str) -> SeverityLevel:
    return cast(SeverityLevel, data)

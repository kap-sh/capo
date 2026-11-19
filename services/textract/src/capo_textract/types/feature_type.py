"""Generated from Smithy shape ``com.amazonaws.textract#FeatureType``."""

from typing import Literal, TypeAlias, cast

FeatureType: TypeAlias = Literal[
    "TABLES",
    "FORMS",
    "QUERIES",
    "SIGNATURES",
    "LAYOUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureType:
    return cast(FeatureType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FeatureType) -> str:
    return value


def deserialize_cbor(data: str) -> FeatureType:
    return cast(FeatureType, data)

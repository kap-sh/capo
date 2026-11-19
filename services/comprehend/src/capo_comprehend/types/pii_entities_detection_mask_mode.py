"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntitiesDetectionMaskMode``."""

from typing import Literal, TypeAlias, cast

PiiEntitiesDetectionMaskMode: TypeAlias = Literal[
    "MASK",
    "REPLACE_WITH_PII_ENTITY_TYPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PiiEntitiesDetectionMaskMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PiiEntitiesDetectionMaskMode:
    return cast(PiiEntitiesDetectionMaskMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PiiEntitiesDetectionMaskMode) -> str:
    return value


def deserialize_cbor(data: str) -> PiiEntitiesDetectionMaskMode:
    return cast(PiiEntitiesDetectionMaskMode, data)

"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntitiesDetectionMode``."""

from typing import Literal, TypeAlias, cast

PiiEntitiesDetectionMode: TypeAlias = Literal[
    "ONLY_REDACTION",
    "ONLY_OFFSETS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PiiEntitiesDetectionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PiiEntitiesDetectionMode:
    return cast(PiiEntitiesDetectionMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PiiEntitiesDetectionMode) -> str:
    return value


def deserialize_cbor(data: str) -> PiiEntitiesDetectionMode:
    return cast(PiiEntitiesDetectionMode, data)

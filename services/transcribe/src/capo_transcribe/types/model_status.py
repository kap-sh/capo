"""Generated from Smithy shape ``com.amazonaws.transcribe#ModelStatus``."""

from typing import Literal, TypeAlias, cast

ModelStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelStatus:
    return cast(ModelStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModelStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ModelStatus:
    return cast(ModelStatus, data)

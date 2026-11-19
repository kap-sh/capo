"""Generated from Smithy shape ``com.amazonaws.comprehend#ModelStatus``."""

from typing import Literal, TypeAlias, cast

ModelStatus: TypeAlias = Literal[
    "SUBMITTED",
    "TRAINING",
    "DELETING",
    "STOP_REQUESTED",
    "STOPPED",
    "IN_ERROR",
    "TRAINED",
    "TRAINED_WITH_WARNING",
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

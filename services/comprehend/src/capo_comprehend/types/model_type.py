"""Generated from Smithy shape ``com.amazonaws.comprehend#ModelType``."""

from typing import Literal, TypeAlias, cast

ModelType: TypeAlias = Literal[
    "DOCUMENT_CLASSIFIER",
    "ENTITY_RECOGNIZER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelType:
    return cast(ModelType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModelType) -> str:
    return value


def deserialize_cbor(data: str) -> ModelType:
    return cast(ModelType, data)

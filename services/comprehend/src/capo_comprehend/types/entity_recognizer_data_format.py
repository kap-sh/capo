"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerDataFormat``."""

from typing import Literal, TypeAlias, cast

EntityRecognizerDataFormat: TypeAlias = Literal[
    "COMPREHEND_CSV",
    "AUGMENTED_MANIFEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityRecognizerDataFormat:
    return cast(EntityRecognizerDataFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityRecognizerDataFormat) -> str:
    return value


def deserialize_cbor(data: str) -> EntityRecognizerDataFormat:
    return cast(EntityRecognizerDataFormat, data)

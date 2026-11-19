"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetDataFormat``."""

from typing import Literal, TypeAlias, cast

DatasetDataFormat: TypeAlias = Literal[
    "COMPREHEND_CSV",
    "AUGMENTED_MANIFEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetDataFormat:
    return cast(DatasetDataFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DatasetDataFormat) -> str:
    return value


def deserialize_cbor(data: str) -> DatasetDataFormat:
    return cast(DatasetDataFormat, data)

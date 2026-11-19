"""Generated from Smithy shape ``com.amazonaws.comprehend#InputFormat``."""

from typing import Literal, TypeAlias, cast

InputFormat: TypeAlias = Literal[
    "ONE_DOC_PER_FILE",
    "ONE_DOC_PER_LINE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputFormat:
    return cast(InputFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InputFormat) -> str:
    return value


def deserialize_cbor(data: str) -> InputFormat:
    return cast(InputFormat, data)

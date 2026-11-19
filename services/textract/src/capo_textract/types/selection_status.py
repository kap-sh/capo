"""Generated from Smithy shape ``com.amazonaws.textract#SelectionStatus``."""

from typing import Literal, TypeAlias, cast

SelectionStatus: TypeAlias = Literal[
    "SELECTED",
    "NOT_SELECTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SelectionStatus:
    return cast(SelectionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SelectionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> SelectionStatus:
    return cast(SelectionStatus, data)

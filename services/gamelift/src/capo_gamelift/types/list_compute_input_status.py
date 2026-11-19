"""Generated from Smithy shape ``com.amazonaws.gamelift#ListComputeInputStatus``."""

from typing import Literal, TypeAlias, cast

ListComputeInputStatus: TypeAlias = Literal[
    "ACTIVE",
    "IMPAIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListComputeInputStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListComputeInputStatus:
    return cast(ListComputeInputStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListComputeInputStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ListComputeInputStatus:
    return cast(ListComputeInputStatus, data)

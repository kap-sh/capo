"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderState``."""

from typing import Literal, TypeAlias, cast

AppBlockBuilderState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilderState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockBuilderState:
    return cast(AppBlockBuilderState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppBlockBuilderState) -> str:
    return value


def deserialize_cbor(data: str) -> AppBlockBuilderState:
    return cast(AppBlockBuilderState, data)

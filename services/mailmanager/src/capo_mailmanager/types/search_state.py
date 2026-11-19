"""Generated from Smithy shape ``com.amazonaws.mailmanager#SearchState``."""

from typing import Literal, TypeAlias, cast

SearchState: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SearchState:
    return cast(SearchState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchState) -> str:
    return value


def deserialize_cbor(data: str) -> SearchState:
    return cast(SearchState, data)

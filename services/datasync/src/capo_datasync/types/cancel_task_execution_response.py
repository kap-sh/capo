"""Generated from Smithy shape ``com.amazonaws.datasync#CancelTaskExecutionResponse``."""

from typing_extensions import TypedDict


class CancelTaskExecutionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelTaskExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelTaskExecutionResponse:
    out: CancelTaskExecutionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CancelTaskExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CancelTaskExecutionResponse:
    out: CancelTaskExecutionResponse = {}  # type: ignore[typeddict-item]
    return out

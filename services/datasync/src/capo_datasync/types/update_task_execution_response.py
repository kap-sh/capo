"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateTaskExecutionResponse``."""

from typing_extensions import TypedDict


class UpdateTaskExecutionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskExecutionResponse:
    out: UpdateTaskExecutionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateTaskExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateTaskExecutionResponse:
    out: UpdateTaskExecutionResponse = {}  # type: ignore[typeddict-item]
    return out

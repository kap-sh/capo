"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateTaskResponse``."""

from typing_extensions import TypedDict


class UpdateTaskResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskResponse:
    out: UpdateTaskResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateTaskResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateTaskResponse:
    out: UpdateTaskResponse = {}  # type: ignore[typeddict-item]
    return out

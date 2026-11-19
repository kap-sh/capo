"""Generated from Smithy shape ``com.amazonaws.datasync#DeleteTaskResponse``."""

from typing_extensions import TypedDict


class DeleteTaskResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTaskResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTaskResponse:
    out: DeleteTaskResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteTaskResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteTaskResponse:
    out: DeleteTaskResponse = {}  # type: ignore[typeddict-item]
    return out

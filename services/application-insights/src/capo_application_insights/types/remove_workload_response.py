"""Generated from Smithy shape ``com.amazonaws.applicationinsights#RemoveWorkloadResponse``."""

from typing_extensions import TypedDict


class RemoveWorkloadResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveWorkloadResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveWorkloadResponse:
    out: RemoveWorkloadResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RemoveWorkloadResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RemoveWorkloadResponse:
    out: RemoveWorkloadResponse = {}  # type: ignore[typeddict-item]
    return out

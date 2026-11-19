"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationObjectStorageResponse``."""

from typing_extensions import TypedDict


class UpdateLocationObjectStorageResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationObjectStorageResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationObjectStorageResponse:
    out: UpdateLocationObjectStorageResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLocationObjectStorageResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateLocationObjectStorageResponse:
    out: UpdateLocationObjectStorageResponse = {}  # type: ignore[typeddict-item]
    return out

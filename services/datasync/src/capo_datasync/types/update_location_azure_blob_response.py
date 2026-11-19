"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationAzureBlobResponse``."""

from typing_extensions import TypedDict


class UpdateLocationAzureBlobResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationAzureBlobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationAzureBlobResponse:
    out: UpdateLocationAzureBlobResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLocationAzureBlobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateLocationAzureBlobResponse:
    out: UpdateLocationAzureBlobResponse = {}  # type: ignore[typeddict-item]
    return out

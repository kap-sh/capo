"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteArchiveResponse``."""

from typing_extensions import TypedDict


class DeleteArchiveResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteArchiveResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteArchiveResponse:
    out: DeleteArchiveResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteArchiveResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteArchiveResponse:
    out: DeleteArchiveResponse = {}  # type: ignore[typeddict-item]
    return out

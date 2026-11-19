"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateArchiveResponse``."""

from typing_extensions import TypedDict


class UpdateArchiveResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateArchiveResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateArchiveResponse:
    out: UpdateArchiveResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateArchiveResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateArchiveResponse:
    out: UpdateArchiveResponse = {}  # type: ignore[typeddict-item]
    return out

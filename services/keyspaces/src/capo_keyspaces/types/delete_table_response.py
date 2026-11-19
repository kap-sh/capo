"""Generated from Smithy shape ``com.amazonaws.keyspaces#DeleteTableResponse``."""

from typing_extensions import TypedDict


class DeleteTableResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTableResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTableResponse:
    out: DeleteTableResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteTableResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteTableResponse:
    out: DeleteTableResponse = {}  # type: ignore[typeddict-item]
    return out

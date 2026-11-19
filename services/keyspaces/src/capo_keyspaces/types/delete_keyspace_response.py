"""Generated from Smithy shape ``com.amazonaws.keyspaces#DeleteKeyspaceResponse``."""

from typing_extensions import TypedDict


class DeleteKeyspaceResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteKeyspaceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteKeyspaceResponse:
    out: DeleteKeyspaceResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteKeyspaceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteKeyspaceResponse:
    out: DeleteKeyspaceResponse = {}  # type: ignore[typeddict-item]
    return out

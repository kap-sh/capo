"""Generated from Smithy shape ``com.amazonaws.datasync#DeleteLocationResponse``."""

from typing_extensions import TypedDict


class DeleteLocationResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLocationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLocationResponse:
    out: DeleteLocationResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteLocationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteLocationResponse:
    out: DeleteLocationResponse = {}  # type: ignore[typeddict-item]
    return out

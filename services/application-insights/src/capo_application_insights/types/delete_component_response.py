"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DeleteComponentResponse``."""

from typing_extensions import TypedDict


class DeleteComponentResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteComponentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteComponentResponse:
    out: DeleteComponentResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteComponentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteComponentResponse:
    out: DeleteComponentResponse = {}  # type: ignore[typeddict-item]
    return out

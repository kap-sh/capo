"""Generated from Smithy shape ``com.amazonaws.textract#DeleteAdapterResponse``."""

from typing_extensions import TypedDict


class DeleteAdapterResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAdapterResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAdapterResponse:
    out: DeleteAdapterResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAdapterResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAdapterResponse:
    out: DeleteAdapterResponse = {}  # type: ignore[typeddict-item]
    return out

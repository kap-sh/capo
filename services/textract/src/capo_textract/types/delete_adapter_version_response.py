"""Generated from Smithy shape ``com.amazonaws.textract#DeleteAdapterVersionResponse``."""

from typing_extensions import TypedDict


class DeleteAdapterVersionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAdapterVersionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAdapterVersionResponse:
    out: DeleteAdapterVersionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAdapterVersionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAdapterVersionResponse:
    out: DeleteAdapterVersionResponse = {}  # type: ignore[typeddict-item]
    return out

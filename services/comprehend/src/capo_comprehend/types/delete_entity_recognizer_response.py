"""Generated from Smithy shape ``com.amazonaws.comprehend#DeleteEntityRecognizerResponse``."""

from typing_extensions import TypedDict


class DeleteEntityRecognizerResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEntityRecognizerResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEntityRecognizerResponse:
    out: DeleteEntityRecognizerResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteEntityRecognizerResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteEntityRecognizerResponse:
    out: DeleteEntityRecognizerResponse = {}  # type: ignore[typeddict-item]
    return out

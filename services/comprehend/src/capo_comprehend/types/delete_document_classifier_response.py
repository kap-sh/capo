"""Generated from Smithy shape ``com.amazonaws.comprehend#DeleteDocumentClassifierResponse``."""

from typing_extensions import TypedDict


class DeleteDocumentClassifierResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDocumentClassifierResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDocumentClassifierResponse:
    out: DeleteDocumentClassifierResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDocumentClassifierResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteDocumentClassifierResponse:
    out: DeleteDocumentClassifierResponse = {}  # type: ignore[typeddict-item]
    return out

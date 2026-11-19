"""Generated from Smithy shape ``com.amazonaws.comprehend#StopTrainingDocumentClassifierResponse``."""

from typing_extensions import TypedDict


class StopTrainingDocumentClassifierResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTrainingDocumentClassifierResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTrainingDocumentClassifierResponse:
    out: StopTrainingDocumentClassifierResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopTrainingDocumentClassifierResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopTrainingDocumentClassifierResponse:
    out: StopTrainingDocumentClassifierResponse = {}  # type: ignore[typeddict-item]
    return out

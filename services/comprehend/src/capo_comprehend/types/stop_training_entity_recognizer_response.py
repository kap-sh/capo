"""Generated from Smithy shape ``com.amazonaws.comprehend#StopTrainingEntityRecognizerResponse``."""

from typing_extensions import TypedDict


class StopTrainingEntityRecognizerResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTrainingEntityRecognizerResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTrainingEntityRecognizerResponse:
    out: StopTrainingEntityRecognizerResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopTrainingEntityRecognizerResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopTrainingEntityRecognizerResponse:
    out: StopTrainingEntityRecognizerResponse = {}  # type: ignore[typeddict-item]
    return out

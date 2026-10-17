"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopTrainingSessionResponse``."""

from typing_extensions import TypedDict


class StopTrainingSessionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTrainingSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTrainingSessionResponse:
    out: StopTrainingSessionResponse = {}  # type: ignore[typeddict-item]
    return out

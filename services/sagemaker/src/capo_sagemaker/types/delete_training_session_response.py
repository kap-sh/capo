"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteTrainingSessionResponse``."""

from typing_extensions import TypedDict


class DeleteTrainingSessionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrainingSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrainingSessionResponse:
    out: DeleteTrainingSessionResponse = {}  # type: ignore[typeddict-item]
    return out

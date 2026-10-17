"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrainingSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_session_arn


class CreateTrainingSessionResponse(TypedDict, closed=True):
    training_session_arn: NotRequired[
        "capo_sagemaker.types.training_session_arn.TrainingSessionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrainingSessionResponse) -> dict:
    out: dict = {}
    if "training_session_arn" in value:
        out["TrainingSessionArn"] = value["training_session_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrainingSessionResponse:
    out: CreateTrainingSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrainingSessionArn") is not None:
        out["training_session_arn"] = data["TrainingSessionArn"]
    return out

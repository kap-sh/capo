"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopTrainingSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_session_name


class StopTrainingSessionRequest(TypedDict, closed=True):
    training_session_name: NotRequired[
        "capo_sagemaker.types.training_session_name.TrainingSessionName"
    ]
    """<p>The name of the training session to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTrainingSessionRequest) -> dict:
    out: dict = {}
    if "training_session_name" in value:
        out["TrainingSessionName"] = value["training_session_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTrainingSessionRequest:
    out: StopTrainingSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrainingSessionName") is not None:
        out["training_session_name"] = data["TrainingSessionName"]
    return out

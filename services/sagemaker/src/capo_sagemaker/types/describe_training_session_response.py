"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrainingSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_session_detail


class DescribeTrainingSessionResponse(TypedDict, closed=True):
    training_session_detail: NotRequired[
        "capo_sagemaker.types.training_session_detail.TrainingSessionDetail"
    ]
    """<p>The detailed information about the training session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrainingSessionResponse) -> dict:
    out: dict = {}
    if "training_session_detail" in value:
        import capo_sagemaker.types.training_session_detail

        out["TrainingSessionDetail"] = (
            capo_sagemaker.types.training_session_detail.serialize_aws_json_1_1(
                value["training_session_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrainingSessionResponse:
    out: DescribeTrainingSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrainingSessionDetail") is not None:
        import capo_sagemaker.types.training_session_detail

        out["training_session_detail"] = (
            capo_sagemaker.types.training_session_detail.deserialize_aws_json_1_1(
                data["TrainingSessionDetail"]
            )
        )
    return out

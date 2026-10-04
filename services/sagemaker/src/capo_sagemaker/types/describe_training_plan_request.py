"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrainingPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_plan_name_or_arn


class DescribeTrainingPlanRequest(TypedDict, closed=True):
    training_plan_name: NotRequired[
        "capo_sagemaker.types.training_plan_name_or_arn.TrainingPlanNameOrArn"
    ]
    """<p>The name of the training plan to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrainingPlanRequest) -> dict:
    out: dict = {}
    if "training_plan_name" in value:
        out["TrainingPlanName"] = value["training_plan_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrainingPlanRequest:
    out: DescribeTrainingPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrainingPlanName") is not None:
        out["training_plan_name"] = data["TrainingPlanName"]
    return out

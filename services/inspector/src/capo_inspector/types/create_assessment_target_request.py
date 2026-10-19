"""Generated from Smithy shape ``com.amazonaws.inspector#CreateAssessmentTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.assessment_target_name


class CreateAssessmentTargetRequest(TypedDict, closed=True):
    assessment_target_name: (
        "capo_inspector.types.assessment_target_name.AssessmentTargetName"
    )
    """<p>The user-defined name that identifies the assessment target that you want to create. The name must be unique within the AWS account.</p>"""
    resource_group_arn: NotRequired["capo_inspector.types.arn.Arn"]
    """<p>The ARN that specifies the resource group that is used to create the assessment target. If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAssessmentTargetRequest) -> dict:
    out: dict = {}
    out["assessmentTargetName"] = value["assessment_target_name"]
    if "resource_group_arn" in value:
        out["resourceGroupArn"] = value["resource_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAssessmentTargetRequest:
    out: CreateAssessmentTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTargetName") is not None:
        out["assessment_target_name"] = data["assessmentTargetName"]
    else:
        out["assessment_target_name"] = ""
    if data.get("resourceGroupArn") is not None:
        out["resource_group_arn"] = data["resourceGroupArn"]
    return out

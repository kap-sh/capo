"""Generated from Smithy shape ``com.amazonaws.inspector#UpdateAssessmentTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.assessment_target_name


class UpdateAssessmentTargetRequest(TypedDict, closed=True):
    assessment_target_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment target that you want to update.</p>"""
    assessment_target_name: (
        "capo_inspector.types.assessment_target_name.AssessmentTargetName"
    )
    """<p>The name of the assessment target that you want to update.</p>"""
    resource_group_arn: NotRequired["capo_inspector.types.arn.Arn"]
    """<p>The ARN of the resource group that is used to specify the new resource group to associate with the assessment target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAssessmentTargetRequest) -> dict:
    out: dict = {}
    out["assessmentTargetArn"] = value["assessment_target_arn"]
    out["assessmentTargetName"] = value["assessment_target_name"]
    if "resource_group_arn" in value:
        out["resourceGroupArn"] = value["resource_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAssessmentTargetRequest:
    out: UpdateAssessmentTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTargetArn") is not None:
        out["assessment_target_arn"] = data["assessmentTargetArn"]
    else:
        out["assessment_target_arn"] = ""
    if data.get("assessmentTargetName") is not None:
        out["assessment_target_name"] = data["assessmentTargetName"]
    else:
        out["assessment_target_name"] = ""
    if data.get("resourceGroupArn") is not None:
        out["resource_group_arn"] = data["resourceGroupArn"]
    return out

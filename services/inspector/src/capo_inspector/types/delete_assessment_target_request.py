"""Generated from Smithy shape ``com.amazonaws.inspector#DeleteAssessmentTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn


class DeleteAssessmentTargetRequest(TypedDict, closed=True):
    assessment_target_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the assessment target that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAssessmentTargetRequest) -> dict:
    out: dict = {}
    out["assessmentTargetArn"] = value["assessment_target_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAssessmentTargetRequest:
    out: DeleteAssessmentTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTargetArn") is not None:
        out["assessment_target_arn"] = data["assessmentTargetArn"]
    else:
        out["assessment_target_arn"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.inspector#DeleteAssessmentTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn


class DeleteAssessmentTemplateRequest(TypedDict, closed=True):
    assessment_template_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the assessment template that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAssessmentTemplateRequest) -> dict:
    out: dict = {}
    out["assessmentTemplateArn"] = value["assessment_template_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAssessmentTemplateRequest:
    out: DeleteAssessmentTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTemplateArn") is not None:
        out["assessment_template_arn"] = data["assessmentTemplateArn"]
    else:
        out["assessment_template_arn"] = ""
    return out

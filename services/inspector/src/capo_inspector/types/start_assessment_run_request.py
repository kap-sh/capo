"""Generated from Smithy shape ``com.amazonaws.inspector#StartAssessmentRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.assessment_run_name


class StartAssessmentRunRequest(TypedDict, closed=True):
    assessment_template_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment template of the assessment run that you want to start.</p>"""
    assessment_run_name: NotRequired[
        "capo_inspector.types.assessment_run_name.AssessmentRunName"
    ]
    """<p>You can specify the name for the assessment run. The name must be unique for the assessment template whose ARN is used to start the assessment run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAssessmentRunRequest) -> dict:
    out: dict = {}
    out["assessmentTemplateArn"] = value["assessment_template_arn"]
    if "assessment_run_name" in value:
        out["assessmentRunName"] = value["assessment_run_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAssessmentRunRequest:
    out: StartAssessmentRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTemplateArn") is not None:
        out["assessment_template_arn"] = data["assessmentTemplateArn"]
    else:
        out["assessment_template_arn"] = ""
    if data.get("assessmentRunName") is not None:
        out["assessment_run_name"] = data["assessmentRunName"]
    return out

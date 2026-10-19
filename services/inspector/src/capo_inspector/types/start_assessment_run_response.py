"""Generated from Smithy shape ``com.amazonaws.inspector#StartAssessmentRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn


class StartAssessmentRunResponse(TypedDict, closed=True):
    assessment_run_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment run that has been started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAssessmentRunResponse) -> dict:
    out: dict = {}
    out["assessmentRunArn"] = value["assessment_run_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAssessmentRunResponse:
    out: StartAssessmentRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessmentRunArn") is not None:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    else:
        out["assessment_run_arn"] = ""
    return out

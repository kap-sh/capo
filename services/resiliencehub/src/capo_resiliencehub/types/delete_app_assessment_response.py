"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteAppAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.assessment_status


class DeleteAppAssessmentResponse(TypedDict, closed=True):
    assessment_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    assessment_status: "capo_resiliencehub.types.assessment_status.AssessmentStatus"
    """<p>The current status of the assessment for the resiliency policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppAssessmentResponse) -> dict:
    out: dict = {}
    out["assessmentArn"] = value["assessment_arn"]
    import capo_resiliencehub.types.assessment_status

    out["assessmentStatus"] = capo_resiliencehub.types.assessment_status.serialize_json(
        value["assessment_status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteAppAssessmentResponse:
    out: DeleteAppAssessmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessmentArn") is not None:
        out["assessment_arn"] = data["assessmentArn"]
    else:
        raise DeserializationError(
            "DeleteAppAssessmentResponse.assessment_arn required"
        )
    if data.get("assessmentStatus") is not None:
        import capo_resiliencehub.types.assessment_status

        out["assessment_status"] = (
            capo_resiliencehub.types.assessment_status.deserialize_json(
                data["assessmentStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAppAssessmentResponse.assessment_status required"
        )
    return out

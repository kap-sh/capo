"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeAppAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn


class DescribeAppAssessmentRequest(TypedDict, closed=True):
    assessment_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppAssessmentRequest) -> dict:
    out: dict = {}
    out["assessmentArn"] = value["assessment_arn"]
    return out


def deserialize_json(data: dict) -> DescribeAppAssessmentRequest:
    out: DescribeAppAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentArn") is not None:
        out["assessment_arn"] = data["assessmentArn"]
    else:
        raise DeserializationError(
            "DescribeAppAssessmentRequest.assessment_arn required"
        )
    return out

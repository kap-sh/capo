"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteAppAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.client_token


class DeleteAppAssessmentRequest(TypedDict, closed=True):
    assessment_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    client_token: NotRequired["capo_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppAssessmentRequest) -> dict:
    out: dict = {}
    out["assessmentArn"] = value["assessment_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteAppAssessmentRequest:
    out: DeleteAppAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentArn") is not None:
        out["assessment_arn"] = data["assessmentArn"]
    else:
        raise DeserializationError("DeleteAppAssessmentRequest.assessment_arn required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteADAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_id


class DeleteADAssessmentRequest(TypedDict, closed=True):
    assessment_id: "capo_directory_service.types.assessment_id.AssessmentId"
    """<p>The unique identifier of the directory assessment to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteADAssessmentRequest) -> dict:
    out: dict = {}
    out["AssessmentId"] = value["assessment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteADAssessmentRequest:
    out: DeleteADAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssessmentId") is not None:
        out["assessment_id"] = data["AssessmentId"]
    else:
        out["assessment_id"] = ""
    return out

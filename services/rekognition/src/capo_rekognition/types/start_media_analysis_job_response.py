"""Generated from Smithy shape ``com.amazonaws.rekognition#StartMediaAnalysisJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.media_analysis_job_id


class StartMediaAnalysisJobResponse(TypedDict, closed=True):
    job_id: "capo_rekognition.types.media_analysis_job_id.MediaAnalysisJobId"
    """<p>Identifier for the created job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMediaAnalysisJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMediaAnalysisJobResponse:
    out: StartMediaAnalysisJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out

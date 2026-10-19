"""Generated from Smithy shape ``com.amazonaws.rekognition#GetMediaAnalysisJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.media_analysis_job_id


class GetMediaAnalysisJobRequest(TypedDict, closed=True):
    job_id: "capo_rekognition.types.media_analysis_job_id.MediaAnalysisJobId"
    """<p>Unique identifier for the media analysis job for which you want to retrieve results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMediaAnalysisJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMediaAnalysisJobRequest:
    out: GetMediaAnalysisJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out

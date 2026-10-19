"""Generated from Smithy shape ``com.amazonaws.rekognition#ListMediaAnalysisJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.extended_pagination_token
    import capo_rekognition.types.media_analysis_job_descriptions


class ListMediaAnalysisJobsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>Pagination token, if the previous response was incomplete.</p>"""
    media_analysis_jobs: "capo_rekognition.types.media_analysis_job_descriptions.MediaAnalysisJobDescriptions"
    """<p>Contains a list of all media analysis jobs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMediaAnalysisJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_rekognition.types.media_analysis_job_descriptions

    out["MediaAnalysisJobs"] = (
        capo_rekognition.types.media_analysis_job_descriptions.serialize_aws_json_1_1(
            value["media_analysis_jobs"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMediaAnalysisJobsResponse:
    out: ListMediaAnalysisJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MediaAnalysisJobs") is not None:
        import capo_rekognition.types.media_analysis_job_descriptions

        out["media_analysis_jobs"] = (
            capo_rekognition.types.media_analysis_job_descriptions.deserialize_aws_json_1_1(
                data["MediaAnalysisJobs"]
            )
        )
    else:
        out["media_analysis_jobs"] = []
    return out

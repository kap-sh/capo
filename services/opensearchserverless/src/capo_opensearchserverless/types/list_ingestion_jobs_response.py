"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListIngestionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_job_summaries


class ListIngestionJobsResponse(TypedDict, closed=True):
    ingestion_job_summaries: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_summaries.IngestionJobSummaries"
    ]
    """<p>Summary information about each ingestion job.</p>"""
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListIngestionJobsResponse) -> dict:
    out: dict = {}
    if "ingestion_job_summaries" in value:
        import capo_opensearchserverless.types.ingestion_job_summaries

        out["ingestionJobSummaries"] = (
            capo_opensearchserverless.types.ingestion_job_summaries.serialize_aws_json_1_0(
                value["ingestion_job_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListIngestionJobsResponse:
    out: ListIngestionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestionJobSummaries") is not None:
        import capo_opensearchserverless.types.ingestion_job_summaries

        out["ingestion_job_summaries"] = (
            capo_opensearchserverless.types.ingestion_job_summaries.deserialize_aws_json_1_0(
                data["ingestionJobSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

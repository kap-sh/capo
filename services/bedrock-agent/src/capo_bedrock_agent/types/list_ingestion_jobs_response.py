"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListIngestionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.ingestion_job_summaries
    import capo_bedrock_agent.types.next_token


class ListIngestionJobsResponse(TypedDict, closed=True):
    ingestion_job_summaries: (
        "capo_bedrock_agent.types.ingestion_job_summaries.IngestionJobSummaries"
    )
    """<p>A list of data ingestion jobs with information about each job.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIngestionJobsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.ingestion_job_summaries

    out["ingestionJobSummaries"] = (
        capo_bedrock_agent.types.ingestion_job_summaries.serialize_json(
            value["ingestion_job_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIngestionJobsResponse:
    out: ListIngestionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestionJobSummaries") is not None:
        import capo_bedrock_agent.types.ingestion_job_summaries

        out["ingestion_job_summaries"] = (
            capo_bedrock_agent.types.ingestion_job_summaries.deserialize_json(
                data["ingestionJobSummaries"]
            )
        )
    else:
        out["ingestion_job_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

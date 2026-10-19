"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListEnrichmentJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.enrichment_job_summaries
    import capo_iotsitewise.types.next_token


class ListEnrichmentJobsResponse(TypedDict, closed=True):
    jobs: "capo_iotsitewise.types.enrichment_job_summaries.EnrichmentJobSummaries"
    """<p>Array of job summaries matching the filter criteria, ordered by creation time descending (newest first). Each summary includes key identifiers (jobId, datasetId, propertyAlias/timeSeriesId) and status information without the full job configuration. Use DescribeEnrichmentJob to retrieve complete details.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>Pagination token to retrieve the next page of results. If present, more jobs exist that match the filter criteria. Include this token in a subsequent ListEnrichmentJobs request to retrieve the next page. If absent, you have retrieved all matching jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnrichmentJobsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.enrichment_job_summaries

    out["jobs"] = capo_iotsitewise.types.enrichment_job_summaries.serialize_json(
        value["jobs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnrichmentJobsResponse:
    out: ListEnrichmentJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_iotsitewise.types.enrichment_job_summaries

        out["jobs"] = capo_iotsitewise.types.enrichment_job_summaries.deserialize_json(
            data["jobs"]
        )
    else:
        out["jobs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

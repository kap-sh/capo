"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListBulkImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.job_summaries
    import capo_iotsitewise.types.next_token


class ListBulkImportJobsResponse(TypedDict, closed=True):
    job_summaries: "capo_iotsitewise.types.job_summaries.JobSummaries"
    """<p>One or more job summaries to list.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBulkImportJobsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.job_summaries

    out["jobSummaries"] = capo_iotsitewise.types.job_summaries.serialize_json(
        value["job_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBulkImportJobsResponse:
    out: ListBulkImportJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobSummaries") is not None:
        import capo_iotsitewise.types.job_summaries

        out["job_summaries"] = capo_iotsitewise.types.job_summaries.deserialize_json(
            data["jobSummaries"]
        )
    else:
        out["job_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

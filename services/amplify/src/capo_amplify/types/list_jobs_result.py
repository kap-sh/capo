"""Generated from Smithy shape ``com.amazonaws.amplify#ListJobsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.job_summaries
    import capo_amplify.types.next_token


class ListJobsResult(TypedDict, closed=True):
    job_summaries: "capo_amplify.types.job_summaries.JobSummaries"
    """<p>The result structure for the list job result request. </p>"""
    next_token: NotRequired["capo_amplify.types.next_token.NextToken"]
    """<p>A pagination token. If non-null the pagination token is returned in a result. Pass its value in another request to retrieve more entries. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResult) -> dict:
    out: dict = {}
    import capo_amplify.types.job_summaries

    out["jobSummaries"] = capo_amplify.types.job_summaries.serialize_json(
        value["job_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResult:
    out: ListJobsResult = {}  # type: ignore[typeddict-item]
    if data.get("jobSummaries") is not None:
        import capo_amplify.types.job_summaries

        out["job_summaries"] = capo_amplify.types.job_summaries.deserialize_json(
            data["jobSummaries"]
        )
    else:
        out["job_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

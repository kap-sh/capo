"""Generated from Smithy shape ``com.amazonaws.databrew#ListJobRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.job_run_list
    import capo_databrew.types.next_token


class ListJobRunsResponse(TypedDict, closed=True):
    job_runs: "capo_databrew.types.job_run_list.JobRunList"
    """<p>A list of job runs that have occurred for the specified job.</p>"""
    next_token: NotRequired["capo_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunsResponse) -> dict:
    out: dict = {}
    import capo_databrew.types.job_run_list

    out["JobRuns"] = capo_databrew.types.job_run_list.serialize_json(value["job_runs"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobRunsResponse:
    out: ListJobRunsResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobRuns") is not None:
        import capo_databrew.types.job_run_list

        out["job_runs"] = capo_databrew.types.job_run_list.deserialize_json(
            data["JobRuns"]
        )
    else:
        out["job_runs"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

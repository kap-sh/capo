"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListJobRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.job_runs
    import capo_emr_serverless.types.next_token


class ListJobRunsResponse(TypedDict, closed=True):
    job_runs: "capo_emr_serverless.types.job_runs.JobRuns"
    """<p>The output lists information about the specified job runs.</p>"""
    next_token: NotRequired["capo_emr_serverless.types.next_token.NextToken"]
    """<p>The output displays the token for the next set of job run results. This is required for pagination and is available as a response of the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunsResponse) -> dict:
    out: dict = {}
    import capo_emr_serverless.types.job_runs

    out["jobRuns"] = capo_emr_serverless.types.job_runs.serialize_json(
        value["job_runs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobRunsResponse:
    out: ListJobRunsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobRuns") is not None:
        import capo_emr_serverless.types.job_runs

        out["job_runs"] = capo_emr_serverless.types.job_runs.deserialize_json(
            data["jobRuns"]
        )
    else:
        out["job_runs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

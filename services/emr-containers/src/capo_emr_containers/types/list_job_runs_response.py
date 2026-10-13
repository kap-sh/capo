"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListJobRunsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.job_runs
    import capo_emr_containers.types.next_token


class ListJobRunsResponse(TypedDict, closed=True):
    job_runs: NotRequired["capo_emr_containers.types.job_runs.JobRuns"]
    """<p>This output lists information about the specified job runs.</p>"""
    next_token: NotRequired["capo_emr_containers.types.next_token.NextToken"]
    """<p>This output displays the token for the next set of job runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunsResponse) -> dict:
    out: dict = {}
    if "job_runs" in value:
        import capo_emr_containers.types.job_runs

        out["jobRuns"] = capo_emr_containers.types.job_runs.serialize_json(
            value["job_runs"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobRunsResponse:
    out: ListJobRunsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobRuns") is not None:
        import capo_emr_containers.types.job_runs

        out["job_runs"] = capo_emr_containers.types.job_runs.deserialize_json(
            data["jobRuns"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListJobRunsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_runs" in value:
        import capo_emr_containers.types.job_runs

        out["job_runs"] = capo_emr_containers.types.job_runs.redact_sensitive(
            value["job_runs"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeJobRunResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.job_run


class DescribeJobRunResponse(TypedDict, closed=True):
    job_run: NotRequired["capo_emr_containers.types.job_run.JobRun"]
    """<p>The output displays information about a job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobRunResponse) -> dict:
    out: dict = {}
    if "job_run" in value:
        import capo_emr_containers.types.job_run

        out["jobRun"] = capo_emr_containers.types.job_run.serialize_json(
            value["job_run"]
        )
    return out


def deserialize_json(data: dict) -> DescribeJobRunResponse:
    out: DescribeJobRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobRun") is not None:
        import capo_emr_containers.types.job_run

        out["job_run"] = capo_emr_containers.types.job_run.deserialize_json(
            data["jobRun"]
        )
    return out


def redact_sensitive(value: DescribeJobRunResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_run" in value:
        import capo_emr_containers.types.job_run

        out["job_run"] = capo_emr_containers.types.job_run.redact_sensitive(
            value["job_run"]
        )
    return out

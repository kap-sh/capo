"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetJobRunResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.job_run


class GetJobRunResponse(TypedDict, closed=True):
    job_run: "capo_emr_serverless.types.job_run.JobRun"
    """<p>The output displays information about the job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobRunResponse) -> dict:
    out: dict = {}
    import capo_emr_serverless.types.job_run

    out["jobRun"] = capo_emr_serverless.types.job_run.serialize_json(value["job_run"])
    return out


def deserialize_json(data: dict) -> GetJobRunResponse:
    out: GetJobRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobRun") is not None:
        import capo_emr_serverless.types.job_run

        out["job_run"] = capo_emr_serverless.types.job_run.deserialize_json(
            data["jobRun"]
        )
    else:
        raise DeserializationError("GetJobRunResponse.job_run required")
    return out


def redact_sensitive(value: GetJobRunResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_run" in value:
        import capo_emr_serverless.types.job_run

        out["job_run"] = capo_emr_serverless.types.job_run.redact_sensitive(
            value["job_run"]
        )
    return out

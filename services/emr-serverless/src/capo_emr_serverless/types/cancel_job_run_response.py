"""Generated from Smithy shape ``com.amazonaws.emrserverless#CancelJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.job_run_id


class CancelJobRunResponse(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The output contains the application ID on which the job run is cancelled.</p>"""
    job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId"
    """<p>The output contains the ID of the cancelled job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRunResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["jobRunId"] = value["job_run_id"]
    return out


def deserialize_json(data: dict) -> CancelJobRunResponse:
    out: CancelJobRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("jobRunId") is not None:
        out["job_run_id"] = data["jobRunId"]
    else:
        out["job_run_id"] = ""
    return out

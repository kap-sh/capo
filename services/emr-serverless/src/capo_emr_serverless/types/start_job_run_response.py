"""Generated from Smithy shape ``com.amazonaws.emrserverless#StartJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.job_arn
    import capo_emr_serverless.types.job_run_id


class StartJobRunResponse(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>This output displays the application ID on which the job run was submitted.</p>"""
    job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId"
    """<p>The output contains the ID of the started job run.</p>"""
    arn: "capo_emr_serverless.types.job_arn.JobArn"
    """<p>This output displays the ARN of the job run..</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRunResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["jobRunId"] = value["job_run_id"]
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StartJobRunResponse:
    out: StartJobRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("jobRunId") is not None:
        out["job_run_id"] = data["jobRunId"]
    else:
        out["job_run_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out

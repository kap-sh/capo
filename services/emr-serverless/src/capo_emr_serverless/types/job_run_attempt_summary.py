"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobRunAttemptSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.attempt_number
    import capo_emr_serverless.types.date
    import capo_emr_serverless.types.iam_role_arn
    import capo_emr_serverless.types.job_arn
    import capo_emr_serverless.types.job_run_id
    import capo_emr_serverless.types.job_run_mode
    import capo_emr_serverless.types.job_run_state
    import capo_emr_serverless.types.job_run_type
    import capo_emr_serverless.types.release_label
    import capo_emr_serverless.types.request_identity_user_arn
    import capo_emr_serverless.types.string256


class JobRunAttemptSummary(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application the job is running on.</p>"""
    id: "capo_emr_serverless.types.job_run_id.JobRunId"
    """<p>The ID of the job run attempt.</p>"""
    name: NotRequired["capo_emr_serverless.types.string256.String256"]
    """<p>The name of the job run attempt.</p>"""
    mode: NotRequired["capo_emr_serverless.types.job_run_mode.JobRunMode"]
    """<p>The mode of the job run attempt.</p>"""
    arn: "capo_emr_serverless.types.job_arn.JobArn"
    """<p>The Amazon Resource Name (ARN) of the job run.</p>"""
    created_by: (
        "capo_emr_serverless.types.request_identity_user_arn.RequestIdentityUserArn"
    )
    """<p>The user who created the job run.</p>"""
    job_created_at: "capo_emr_serverless.types.date.Date"
    """<p>The date and time of when the job run was created.</p>"""
    created_at: "capo_emr_serverless.types.date.Date"
    """<p>The date and time when the job run attempt was created.</p>"""
    updated_at: "capo_emr_serverless.types.date.Date"
    """<p>The date and time of when the job run attempt was last updated.</p>"""
    execution_role: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the execution role of the job run..</p>"""
    state: "capo_emr_serverless.types.job_run_state.JobRunState"
    """<p>The state of the job run attempt.</p>"""
    state_details: "capo_emr_serverless.types.string256.String256"
    """<p>The state details of the job run attempt.</p>"""
    release_label: "capo_emr_serverless.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release label of the job run attempt.</p>"""
    type: NotRequired["capo_emr_serverless.types.job_run_type.JobRunType"]
    """<p>The type of the job run, such as Spark or Hive.</p>"""
    attempt: NotRequired["capo_emr_serverless.types.attempt_number.AttemptNumber"]
    """<p>The attempt number of the job run execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobRunAttemptSummary) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "mode" in value:
        out["mode"] = value["mode"]
    out["arn"] = value["arn"]
    out["createdBy"] = value["created_by"]
    import capo_emr_serverless.types.date

    out["jobCreatedAt"] = capo_emr_serverless.types.date.serialize_json(
        value["job_created_at"]
    )
    import capo_emr_serverless.types.date

    out["createdAt"] = capo_emr_serverless.types.date.serialize_json(
        value["created_at"]
    )
    import capo_emr_serverless.types.date

    out["updatedAt"] = capo_emr_serverless.types.date.serialize_json(
        value["updated_at"]
    )
    out["executionRole"] = value["execution_role"]
    out["state"] = value["state"]
    out["stateDetails"] = value["state_details"]
    out["releaseLabel"] = value["release_label"]
    if "type" in value:
        out["type"] = value["type"]
    if "attempt" in value:
        out["attempt"] = value["attempt"]
    return out


def deserialize_json(data: dict) -> JobRunAttemptSummary:
    out: JobRunAttemptSummary = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("mode") is not None:
        out["mode"] = data["mode"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("jobCreatedAt") is not None:
        import capo_emr_serverless.types.date

        out["job_created_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["jobCreatedAt"]
        )
    else:
        import datetime

        out["job_created_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("createdAt") is not None:
        import capo_emr_serverless.types.date

        out["created_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_emr_serverless.types.date

        out["updated_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    else:
        out["execution_role"] = ""
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    if data.get("stateDetails") is not None:
        out["state_details"] = data["stateDetails"]
    else:
        out["state_details"] = ""
    if data.get("releaseLabel") is not None:
        out["release_label"] = data["releaseLabel"]
    else:
        out["release_label"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("attempt") is not None:
        out["attempt"] = data["attempt"]
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardSnapshotJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.non_empty_string
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.snapshot_configuration
    import capo_quicksight.types.snapshot_job_status
    import capo_quicksight.types.snapshot_user_configuration_redacted
    import capo_quicksight.types.status_code
    import capo_quicksight.types.timestamp


class DescribeDashboardSnapshotJobResponse(TypedDict, closed=True):
    aws_account_id: NotRequired["capo_quicksight.types.aws_account_id.AwsAccountId"]
    """<p> The ID of the Amazon Web Services account that the dashboard snapshot job is executed in. </p>"""
    dashboard_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the dashboard that you have started a snapshot job for.</p>"""
    snapshot_job_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the job to be described. The job ID is set when you start a new job with a <code>StartDashboardSnapshotJob</code> API call.</p>"""
    user_configuration: NotRequired[
        "capo_quicksight.types.snapshot_user_configuration_redacted.SnapshotUserConfigurationRedacted"
    ]
    """<p>The user configuration for the snapshot job. This information is provided when you make a <code>StartDashboardSnapshotJob</code> API call.</p>"""
    snapshot_configuration: NotRequired[
        "capo_quicksight.types.snapshot_configuration.SnapshotConfiguration"
    ]
    """<p>The snapshot configuration of the job. This information is provided when you make a <code>StartDashboardSnapshotJob</code> API call.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the snapshot job. The job ARN is generated when you start a new job with a <code>StartDashboardSnapshotJob</code> API call.</p>"""
    job_status: NotRequired[
        "capo_quicksight.types.snapshot_job_status.SnapshotJobStatus"
    ]
    """<p>Indicates the status of a job. The status updates as the job executes. This shows one of the following values.</p> <ul> <li> <p> <code>COMPLETED</code> - The job was completed successfully.</p> </li> <li> <p> <code>FAILED</code> - The job failed to execute.</p> </li> <li> <p> <code>QUEUED</code> - The job is queued and hasn't started yet.</p> </li> <li> <p> <code>RUNNING</code> - The job is still running.</p> </li> </ul>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p> The time that the snapshot job was created. </p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p> The time that the snapshot job status was last updated. </p>"""
    request_id: NotRequired["capo_quicksight.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Web Services request ID for this operation. </p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardSnapshotJobResponse) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "snapshot_job_id" in value:
        out["SnapshotJobId"] = value["snapshot_job_id"]
    if "user_configuration" in value:
        import capo_quicksight.types.snapshot_user_configuration_redacted

        out["UserConfiguration"] = (
            capo_quicksight.types.snapshot_user_configuration_redacted.serialize_json(
                value["user_configuration"]
            )
        )
    if "snapshot_configuration" in value:
        import capo_quicksight.types.snapshot_configuration

        out["SnapshotConfiguration"] = (
            capo_quicksight.types.snapshot_configuration.serialize_json(
                value["snapshot_configuration"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "job_status" in value:
        import capo_quicksight.types.snapshot_job_status

        out["JobStatus"] = capo_quicksight.types.snapshot_job_status.serialize_json(
            value["job_status"]
        )
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    out["Status"] = value.get("status", 0)
    return out


def deserialize_json(data: dict) -> DescribeDashboardSnapshotJobResponse:
    out: DescribeDashboardSnapshotJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    if data.get("DashboardId") is not None:
        out["dashboard_id"] = data["DashboardId"]
    if data.get("SnapshotJobId") is not None:
        out["snapshot_job_id"] = data["SnapshotJobId"]
    if data.get("UserConfiguration") is not None:
        import capo_quicksight.types.snapshot_user_configuration_redacted

        out["user_configuration"] = (
            capo_quicksight.types.snapshot_user_configuration_redacted.deserialize_json(
                data["UserConfiguration"]
            )
        )
    if data.get("SnapshotConfiguration") is not None:
        import capo_quicksight.types.snapshot_configuration

        out["snapshot_configuration"] = (
            capo_quicksight.types.snapshot_configuration.deserialize_json(
                data["SnapshotConfiguration"]
            )
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("JobStatus") is not None:
        import capo_quicksight.types.snapshot_job_status

        out["job_status"] = capo_quicksight.types.snapshot_job_status.deserialize_json(
            data["JobStatus"]
        )
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    return out


def redact_sensitive(value: DescribeDashboardSnapshotJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "snapshot_configuration" in value:
        import capo_quicksight.types.snapshot_configuration

        out["snapshot_configuration"] = (
            capo_quicksight.types.snapshot_configuration.redact_sensitive(
                value["snapshot_configuration"]
            )
        )
    return out

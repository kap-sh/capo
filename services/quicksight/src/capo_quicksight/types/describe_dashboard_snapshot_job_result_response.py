"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardSnapshotJobResultResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.non_empty_string
    import capo_quicksight.types.snapshot_job_error_info
    import capo_quicksight.types.snapshot_job_result
    import capo_quicksight.types.snapshot_job_status
    import capo_quicksight.types.status_code
    import capo_quicksight.types.timestamp


class DescribeDashboardSnapshotJobResultResponse(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the snapshot job. The job ARN is generated when you start a new job with a <code>StartDashboardSnapshotJob</code> API call.</p>"""
    job_status: NotRequired[
        "capo_quicksight.types.snapshot_job_status.SnapshotJobStatus"
    ]
    """<p>Indicates the status of a job after it has reached a terminal state. A finished snapshot job will retuen a <code>COMPLETED</code> or <code>FAILED</code> status.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that a snapshot job was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that a snapshot job status was last updated.</p>"""
    result: NotRequired["capo_quicksight.types.snapshot_job_result.SnapshotJobResult"]
    """<p>The result of the snapshot job. Jobs that have successfully completed will return the S3Uri where they are located. Jobs that have failedwill return information on the error that caused the job to fail.</p>"""
    error_info: NotRequired[
        "capo_quicksight.types.snapshot_job_error_info.SnapshotJobErrorInfo"
    ]
    """<p>Displays information for the error that caused a job to fail.</p>"""
    request_id: NotRequired["capo_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardSnapshotJobResultResponse) -> dict:
    out: dict = {}
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
    if "result" in value:
        import capo_quicksight.types.snapshot_job_result

        out["Result"] = capo_quicksight.types.snapshot_job_result.serialize_json(
            value["result"]
        )
    if "error_info" in value:
        import capo_quicksight.types.snapshot_job_error_info

        out["ErrorInfo"] = capo_quicksight.types.snapshot_job_error_info.serialize_json(
            value["error_info"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDashboardSnapshotJobResultResponse:
    out: DescribeDashboardSnapshotJobResultResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("Result") is not None:
        import capo_quicksight.types.snapshot_job_result

        out["result"] = capo_quicksight.types.snapshot_job_result.deserialize_json(
            data["Result"]
        )
    if data.get("ErrorInfo") is not None:
        import capo_quicksight.types.snapshot_job_error_info

        out["error_info"] = (
            capo_quicksight.types.snapshot_job_error_info.deserialize_json(
                data["ErrorInfo"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(
    value: DescribeDashboardSnapshotJobResultResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "result" in value:
        import capo_quicksight.types.snapshot_job_result

        out["result"] = capo_quicksight.types.snapshot_job_result.redact_sensitive(
            value["result"]
        )
    return out

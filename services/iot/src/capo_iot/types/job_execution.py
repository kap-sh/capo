"""Generated from Smithy shape ``com.amazonaws.iot#JobExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.approximate_seconds_before_timed_out
    import capo_iot.types.date_type
    import capo_iot.types.execution_number
    import capo_iot.types.forced
    import capo_iot.types.job_execution_status
    import capo_iot.types.job_execution_status_details
    import capo_iot.types.job_id
    import capo_iot.types.thing_arn
    import capo_iot.types.version_number


class JobExecution(TypedDict, closed=True):
    job_id: NotRequired["capo_iot.types.job_id.JobId"]
    """<p>The unique identifier you assigned to the job when it was created.</p>"""
    status: NotRequired["capo_iot.types.job_execution_status.JobExecutionStatus"]
    """<p>The status of the job execution (IN_PROGRESS, QUEUED, FAILED, SUCCEEDED, TIMED_OUT, CANCELED, or REJECTED).</p>"""
    force_canceled: NotRequired["capo_iot.types.forced.Forced"]
    """<p>Will be <code>true</code> if the job execution was canceled with the optional <code>force</code> parameter set to <code>true</code>.</p>"""
    status_details: NotRequired[
        "capo_iot.types.job_execution_status_details.JobExecutionStatusDetails"
    ]
    """<p>A collection of name/value pairs that describe the status of the job execution.</p>"""
    thing_arn: NotRequired["capo_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing on which the job execution is running.</p>"""
    queued_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job execution was queued.</p>"""
    started_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job execution started.</p>"""
    last_updated_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job execution was last updated.</p>"""
    execution_number: NotRequired["capo_iot.types.execution_number.ExecutionNumber"]
    """<p>A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used in commands which return or update job execution information. </p>"""
    version_number: "capo_iot.types.version_number.VersionNumber"
    """<p>The version of the job execution. Job execution versions are incremented each time they are updated by a device.</p>"""
    approximate_seconds_before_timed_out: NotRequired[
        "capo_iot.types.approximate_seconds_before_timed_out.ApproximateSecondsBeforeTimedOut"
    ]
    """<p>The estimated number of seconds that remain before the job execution status will be changed to <code>TIMED_OUT</code>. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The actual job execution timeout can occur up to 60 seconds later than the estimated duration. This value will not be included if the job execution has reached a terminal status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecution) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "status" in value:
        import capo_iot.types.job_execution_status

        out["status"] = capo_iot.types.job_execution_status.serialize_json(
            value["status"]
        )
    if "force_canceled" in value:
        out["forceCanceled"] = value["force_canceled"]
    if "status_details" in value:
        import capo_iot.types.job_execution_status_details

        out["statusDetails"] = (
            capo_iot.types.job_execution_status_details.serialize_json(
                value["status_details"]
            )
        )
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    if "queued_at" in value:
        import capo_iot.types.date_type

        out["queuedAt"] = capo_iot.types.date_type.serialize_json(value["queued_at"])
    if "started_at" in value:
        import capo_iot.types.date_type

        out["startedAt"] = capo_iot.types.date_type.serialize_json(value["started_at"])
    if "last_updated_at" in value:
        import capo_iot.types.date_type

        out["lastUpdatedAt"] = capo_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    if "execution_number" in value:
        out["executionNumber"] = value["execution_number"]
    out["versionNumber"] = value.get("version_number", 0)
    if "approximate_seconds_before_timed_out" in value:
        out["approximateSecondsBeforeTimedOut"] = value[
            "approximate_seconds_before_timed_out"
        ]
    return out


def deserialize_json(data: dict) -> JobExecution:
    out: JobExecution = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("status") is not None:
        import capo_iot.types.job_execution_status

        out["status"] = capo_iot.types.job_execution_status.deserialize_json(
            data["status"]
        )
    if data.get("forceCanceled") is not None:
        out["force_canceled"] = data["forceCanceled"]
    if data.get("statusDetails") is not None:
        import capo_iot.types.job_execution_status_details

        out["status_details"] = (
            capo_iot.types.job_execution_status_details.deserialize_json(
                data["statusDetails"]
            )
        )
    if data.get("thingArn") is not None:
        out["thing_arn"] = data["thingArn"]
    if data.get("queuedAt") is not None:
        import capo_iot.types.date_type

        out["queued_at"] = capo_iot.types.date_type.deserialize_json(data["queuedAt"])
    if data.get("startedAt") is not None:
        import capo_iot.types.date_type

        out["started_at"] = capo_iot.types.date_type.deserialize_json(data["startedAt"])
    if data.get("lastUpdatedAt") is not None:
        import capo_iot.types.date_type

        out["last_updated_at"] = capo_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    if data.get("executionNumber") is not None:
        out["execution_number"] = data["executionNumber"]
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    else:
        out["version_number"] = 0
    if data.get("approximateSecondsBeforeTimedOut") is not None:
        out["approximate_seconds_before_timed_out"] = data[
            "approximateSecondsBeforeTimedOut"
        ]
    return out

"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#UpdateJobExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.details_map
    import capo_iot_jobs_data_plane.types.execution_number
    import capo_iot_jobs_data_plane.types.expected_version
    import capo_iot_jobs_data_plane.types.include_execution_state
    import capo_iot_jobs_data_plane.types.include_job_document
    import capo_iot_jobs_data_plane.types.job_execution_status
    import capo_iot_jobs_data_plane.types.job_id
    import capo_iot_jobs_data_plane.types.step_timeout_in_minutes
    import capo_iot_jobs_data_plane.types.thing_name


class UpdateJobExecutionRequest(TypedDict, closed=True):
    job_id: "capo_iot_jobs_data_plane.types.job_id.JobId"
    """<p>The unique identifier assigned to this job when it was created.</p>"""
    thing_name: "capo_iot_jobs_data_plane.types.thing_name.ThingName"
    """<p>The name of the thing associated with the device.</p>"""
    status: "capo_iot_jobs_data_plane.types.job_execution_status.JobExecutionStatus"
    """<p>The new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update.</p>"""
    status_details: NotRequired["capo_iot_jobs_data_plane.types.details_map.DetailsMap"]
    """<p> Optional. A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.</p> <p>The maximum length of the value in the name/value pair is 1,024 characters.</p>"""
    step_timeout_in_minutes: NotRequired[
        "capo_iot_jobs_data_plane.types.step_timeout_in_minutes.StepTimeoutInMinutes"
    ]
    """<p>Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by again calling <code>UpdateJobExecution</code>, setting the status to <code>IN_PROGRESS</code>, and specifying a new timeout value in this field) the job execution status will be automatically set to <code>TIMED_OUT</code>. Note that setting or resetting the step timeout has no effect on the in progress timeout that may have been specified when the job was created (<code>CreateJob</code> using field <code>timeoutConfig</code>).</p> <p>Valid values for this parameter range from 1 to 10080 (1 minute to 7 days). A value of -1 is also valid and will cancel the current step timer (created by an earlier use of <code>UpdateJobExecutionRequest</code>).</p>"""
    expected_version: NotRequired[
        "capo_iot_jobs_data_plane.types.expected_version.ExpectedVersion"
    ]
    """<p>Optional. The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)</p>"""
    include_job_execution_state: NotRequired[
        "capo_iot_jobs_data_plane.types.include_execution_state.IncludeExecutionState"
    ]
    """<p>Optional. When included and set to true, the response contains the JobExecutionState data. The default is false.</p>"""
    include_job_document: NotRequired[
        "capo_iot_jobs_data_plane.types.include_job_document.IncludeJobDocument"
    ]
    """<p>Optional. When set to true, the response contains the job document. The default is false.</p>"""
    execution_number: NotRequired[
        "capo_iot_jobs_data_plane.types.execution_number.ExecutionNumber"
    ]
    """<p>Optional. A number that identifies a particular job execution on a particular device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJobExecutionRequest) -> dict:
    out: dict = {}
    import capo_iot_jobs_data_plane.types.job_execution_status

    out["status"] = capo_iot_jobs_data_plane.types.job_execution_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        import capo_iot_jobs_data_plane.types.details_map

        out["statusDetails"] = (
            capo_iot_jobs_data_plane.types.details_map.serialize_json(
                value["status_details"]
            )
        )
    if "step_timeout_in_minutes" in value:
        out["stepTimeoutInMinutes"] = value["step_timeout_in_minutes"]
    if "expected_version" in value:
        out["expectedVersion"] = value["expected_version"]
    if "include_job_execution_state" in value:
        out["includeJobExecutionState"] = value["include_job_execution_state"]
    if "include_job_document" in value:
        out["includeJobDocument"] = value["include_job_document"]
    if "execution_number" in value:
        out["executionNumber"] = value["execution_number"]
    return out


def deserialize_json(data: dict) -> UpdateJobExecutionRequest:
    out: UpdateJobExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_iot_jobs_data_plane.types.job_execution_status

        out["status"] = (
            capo_iot_jobs_data_plane.types.job_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iot_jobs_data_plane.types.job_execution_status.JobExecutionStatus", ""
        )
    if data.get("statusDetails") is not None:
        import capo_iot_jobs_data_plane.types.details_map

        out["status_details"] = (
            capo_iot_jobs_data_plane.types.details_map.deserialize_json(
                data["statusDetails"]
            )
        )
    if data.get("stepTimeoutInMinutes") is not None:
        out["step_timeout_in_minutes"] = data["stepTimeoutInMinutes"]
    if data.get("expectedVersion") is not None:
        out["expected_version"] = data["expectedVersion"]
    if data.get("includeJobExecutionState") is not None:
        out["include_job_execution_state"] = data["includeJobExecutionState"]
    if data.get("includeJobDocument") is not None:
        out["include_job_document"] = data["includeJobDocument"]
    if data.get("executionNumber") is not None:
        out["execution_number"] = data["executionNumber"]
    return out

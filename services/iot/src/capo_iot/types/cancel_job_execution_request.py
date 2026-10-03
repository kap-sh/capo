"""Generated from Smithy shape ``com.amazonaws.iot#CancelJobExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.details_map
    import capo_iot.types.expected_version
    import capo_iot.types.force_flag
    import capo_iot.types.job_id
    import capo_iot.types.thing_name


class CancelJobExecutionRequest(TypedDict, closed=True):
    job_id: "capo_iot.types.job_id.JobId"
    """<p>The ID of the job to be canceled.</p>"""
    thing_name: "capo_iot.types.thing_name.ThingName"
    """<p>The name of the thing whose execution of the job will be canceled.</p>"""
    force: "capo_iot.types.force_flag.ForceFlag"
    """<p>(Optional) If <code>true</code> the job execution will be canceled if it has status IN_PROGRESS or QUEUED, otherwise the job execution will be canceled only if it has status QUEUED. If you attempt to cancel a job execution that is IN_PROGRESS, and you do not set <code>force</code> to <code>true</code>, then an <code>InvalidStateTransitionException</code> will be thrown. The default is <code>false</code>.</p> <p>Canceling a job execution which is "IN_PROGRESS", will cause the device to be unable to update the job execution status. Use caution and ensure that the device is able to recover to a valid state.</p>"""
    expected_version: NotRequired["capo_iot.types.expected_version.ExpectedVersion"]
    """<p>(Optional) The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)</p>"""
    status_details: NotRequired["capo_iot.types.details_map.DetailsMap"]
    """<p>A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged. You can specify at most 10 name/value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobExecutionRequest) -> dict:
    out: dict = {}
    if "expected_version" in value:
        out["expectedVersion"] = value["expected_version"]
    if "status_details" in value:
        import capo_iot.types.details_map

        out["statusDetails"] = capo_iot.types.details_map.serialize_json(
            value["status_details"]
        )
    return out


def deserialize_json(data: dict) -> CancelJobExecutionRequest:
    out: CancelJobExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("expectedVersion") is not None:
        out["expected_version"] = data["expectedVersion"]
    if data.get("statusDetails") is not None:
        import capo_iot.types.details_map

        out["status_details"] = capo_iot.types.details_map.deserialize_json(
            data["statusDetails"]
        )
    return out

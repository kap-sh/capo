"""Generated from Smithy shape ``com.amazonaws.iot#SchedulingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_end_behavior
    import capo_iot.types.maintenance_windows
    import capo_iot.types.string_date_time


class SchedulingConfig(TypedDict, closed=True):
    start_time: NotRequired["capo_iot.types.string_date_time.StringDateTime"]
    """<p>The time a job will begin rollout of the job document to all devices in the target group for a job. The <code>startTime</code> can be scheduled up to a year in advance and must be scheduled a minimum of thirty minutes from the current time. The date and time format for the <code>startTime</code> is YYYY-MM-DD for the date and HH:MM for the time.</p> <p>For more information on the syntax for <code>startTime</code> when using an API command or the Command Line Interface, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp">Timestamp</a>.</p>"""
    end_time: NotRequired["capo_iot.types.string_date_time.StringDateTime"]
    """<p>The time a job will stop rollout of the job document to all devices in the target group for a job. The <code>endTime</code> must take place no later than two years from the current time and be scheduled a minimum of thirty minutes from the current time. The minimum duration between <code>startTime</code> and <code>endTime</code> is thirty minutes. The maximum duration between <code>startTime</code> and <code>endTime</code> is two years. The date and time format for the <code>endTime</code> is YYYY-MM-DD for the date and HH:MM for the time.</p> <p>For more information on the syntax for <code>endTime</code> when using an API command or the Command Line Interface, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp">Timestamp</a>.</p>"""
    end_behavior: NotRequired["capo_iot.types.job_end_behavior.JobEndBehavior"]
    """<p>Specifies the end behavior for all job executions after a job reaches the selected <code>endTime</code>. If <code>endTime</code> is not selected when creating the job, then <code>endBehavior</code> does not apply.</p>"""
    maintenance_windows: NotRequired[
        "capo_iot.types.maintenance_windows.MaintenanceWindows"
    ]
    """<p>An optional configuration within the <code>SchedulingConfig</code> to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingConfig) -> dict:
    out: dict = {}
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "end_time" in value:
        out["endTime"] = value["end_time"]
    if "end_behavior" in value:
        import capo_iot.types.job_end_behavior

        out["endBehavior"] = capo_iot.types.job_end_behavior.serialize_json(
            value["end_behavior"]
        )
    if "maintenance_windows" in value:
        import capo_iot.types.maintenance_windows

        out["maintenanceWindows"] = capo_iot.types.maintenance_windows.serialize_json(
            value["maintenance_windows"]
        )
    return out


def deserialize_json(data: dict) -> SchedulingConfig:
    out: SchedulingConfig = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        out["start_time"] = data["startTime"]
    if data.get("endTime") is not None:
        out["end_time"] = data["endTime"]
    if data.get("endBehavior") is not None:
        import capo_iot.types.job_end_behavior

        out["end_behavior"] = capo_iot.types.job_end_behavior.deserialize_json(
            data["endBehavior"]
        )
    if data.get("maintenanceWindows") is not None:
        import capo_iot.types.maintenance_windows

        out["maintenance_windows"] = (
            capo_iot.types.maintenance_windows.deserialize_json(
                data["maintenanceWindows"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.datasync#TaskScheduleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.schedule_disabled_by
    import capo_datasync.types.schedule_disabled_reason
    import capo_datasync.types.time


class TaskScheduleDetails(TypedDict, closed=True):
    status_update_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>Indicates the last time the status of your task schedule changed. For example, if DataSync automatically disables your schedule because of a repeated error, you can see when the schedule was disabled.</p>"""
    disabled_reason: NotRequired[
        "capo_datasync.types.schedule_disabled_reason.ScheduleDisabledReason"
    ]
    """<p>Provides a reason if the task schedule is disabled.</p> <p>If your schedule is disabled by <code>USER</code>, you see a <code>Manually disabled by user.</code> message.</p> <p>If your schedule is disabled by <code>SERVICE</code>, you see an error message to help you understand why the task keeps failing. For information on resolving DataSync errors, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html">Troubleshooting issues with DataSync transfers</a>.</p>"""
    disabled_by: NotRequired[
        "capo_datasync.types.schedule_disabled_by.ScheduleDisabledBy"
    ]
    """<p>Indicates how your task schedule was disabled.</p> <ul> <li> <p> <code>USER</code> - Your schedule was manually disabled by using the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTask.html">UpdateTask</a> operation or DataSync console.</p> </li> <li> <p> <code>SERVICE</code> - Your schedule was automatically disabled by DataSync because the task failed repeatedly with the same error.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskScheduleDetails) -> dict:
    out: dict = {}
    if "status_update_time" in value:
        import capo_datasync.types.time

        out["StatusUpdateTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["status_update_time"]
        )
    if "disabled_reason" in value:
        out["DisabledReason"] = value["disabled_reason"]
    if "disabled_by" in value:
        import capo_datasync.types.schedule_disabled_by

        out["DisabledBy"] = (
            capo_datasync.types.schedule_disabled_by.serialize_aws_json_1_1(
                value["disabled_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskScheduleDetails:
    out: TaskScheduleDetails = {}  # type: ignore[typeddict-item]
    if data.get("StatusUpdateTime") is not None:
        import capo_datasync.types.time

        out["status_update_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["StatusUpdateTime"]
        )
    if data.get("DisabledReason") is not None:
        out["disabled_reason"] = data["DisabledReason"]
    if data.get("DisabledBy") is not None:
        import capo_datasync.types.schedule_disabled_by

        out["disabled_by"] = (
            capo_datasync.types.schedule_disabled_by.deserialize_aws_json_1_1(
                data["DisabledBy"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateMaintenanceWindowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.maintenance_window_allow_unassociated_targets
    import capo_ssm.types.maintenance_window_cutoff
    import capo_ssm.types.maintenance_window_description
    import capo_ssm.types.maintenance_window_duration_hours
    import capo_ssm.types.maintenance_window_enabled
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_name
    import capo_ssm.types.maintenance_window_offset
    import capo_ssm.types.maintenance_window_schedule
    import capo_ssm.types.maintenance_window_string_date_time
    import capo_ssm.types.maintenance_window_timezone


class UpdateMaintenanceWindowRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The ID of the maintenance window to update.</p>"""
    name: NotRequired["capo_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The name of the maintenance window.</p>"""
    description: NotRequired[
        "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>An optional description for the update request.</p>"""
    start_date: NotRequired[
        "capo_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become active. <code>StartDate</code> allows you to delay activation of the maintenance window until the specified future date.</p> <note> <p>When using a rate schedule, if you provide a start date that occurs in the past, the current date and time are used as the start date. </p> </note>"""
    end_date: NotRequired[
        "capo_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become inactive. <code>EndDate</code> allows you to set a date and time in the future when the maintenance window will no longer run.</p>"""
    schedule: NotRequired[
        "capo_ssm.types.maintenance_window_schedule.MaintenanceWindowSchedule"
    ]
    """<p>The schedule of the maintenance window in the form of a cron or rate expression.</p>"""
    schedule_timezone: NotRequired[
        "capo_ssm.types.maintenance_window_timezone.MaintenanceWindowTimezone"
    ]
    """<p>The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the <a href="https://www.iana.org/time-zones">Time Zone Database</a> on the IANA website.</p>"""
    schedule_offset: NotRequired[
        "capo_ssm.types.maintenance_window_offset.MaintenanceWindowOffset"
    ]
    """<p>The number of days to wait after the date and time specified by a cron expression before running the maintenance window.</p> <p>For example, the following cron expression schedules a maintenance window to run the third Tuesday of every month at 11:30 PM.</p> <p> <code>cron(30 23 ? * TUE#3 *)</code> </p> <p>If the schedule offset is <code>2</code>, the maintenance window won't run until two days later.</p>"""
    duration: NotRequired[
        "capo_ssm.types.maintenance_window_duration_hours.MaintenanceWindowDurationHours"
    ]
    """<p>The duration of the maintenance window in hours.</p>"""
    cutoff: NotRequired[
        "capo_ssm.types.maintenance_window_cutoff.MaintenanceWindowCutoff"
    ]
    """<p>The number of hours before the end of the maintenance window that Amazon Web Services Systems Manager stops scheduling new tasks for execution.</p>"""
    allow_unassociated_targets: NotRequired[
        "capo_ssm.types.maintenance_window_allow_unassociated_targets.MaintenanceWindowAllowUnassociatedTargets"
    ]
    """<p>Whether targets must be registered with the maintenance window before tasks can be defined for those targets.</p>"""
    enabled: NotRequired[
        "capo_ssm.types.maintenance_window_enabled.MaintenanceWindowEnabled"
    ]
    """<p>Whether the maintenance window is enabled.</p>"""
    replace: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>If <code>True</code>, then all fields that are required by the <a>CreateMaintenanceWindow</a> operation are also required for this API request. Optional fields that aren't specified are set to null. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMaintenanceWindowRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "start_date" in value:
        out["StartDate"] = value["start_date"]
    if "end_date" in value:
        out["EndDate"] = value["end_date"]
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "schedule_timezone" in value:
        out["ScheduleTimezone"] = value["schedule_timezone"]
    if "schedule_offset" in value:
        out["ScheduleOffset"] = value["schedule_offset"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "cutoff" in value:
        out["Cutoff"] = value["cutoff"]
    if "allow_unassociated_targets" in value:
        out["AllowUnassociatedTargets"] = value["allow_unassociated_targets"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "replace" in value:
        out["Replace"] = value["replace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMaintenanceWindowRequest:
    out: UpdateMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError("UpdateMaintenanceWindowRequest.window_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("StartDate") is not None:
        out["start_date"] = data["StartDate"]
    if data.get("EndDate") is not None:
        out["end_date"] = data["EndDate"]
    if data.get("Schedule") is not None:
        out["schedule"] = data["Schedule"]
    if data.get("ScheduleTimezone") is not None:
        out["schedule_timezone"] = data["ScheduleTimezone"]
    if data.get("ScheduleOffset") is not None:
        out["schedule_offset"] = data["ScheduleOffset"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("Cutoff") is not None:
        out["cutoff"] = data["Cutoff"]
    if data.get("AllowUnassociatedTargets") is not None:
        out["allow_unassociated_targets"] = data["AllowUnassociatedTargets"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("Replace") is not None:
        out["replace"] = data["Replace"]
    return out

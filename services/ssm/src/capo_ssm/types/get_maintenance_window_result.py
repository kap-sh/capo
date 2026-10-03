"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
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


class GetMaintenanceWindowResult(TypedDict, closed=True):
    window_id: NotRequired["capo_ssm.types.maintenance_window_id.MaintenanceWindowId"]
    """<p>The ID of the created maintenance window.</p>"""
    name: NotRequired["capo_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The name of the maintenance window.</p>"""
    description: NotRequired[
        "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>The description of the maintenance window.</p>"""
    start_date: NotRequired[
        "capo_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. The maintenance window won't run before this specified time.</p>"""
    end_date: NotRequired[
        "capo_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive. The maintenance window won't run after this specified time.</p>"""
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
    """<p>The number of days to wait to run a maintenance window after the scheduled cron expression date and time.</p>"""
    next_execution_time: NotRequired[
        "capo_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The next time the maintenance window will actually run, taking into account any specified times for the maintenance window to become active or inactive.</p>"""
    duration: NotRequired[
        "capo_ssm.types.maintenance_window_duration_hours.MaintenanceWindowDurationHours"
    ]
    """<p>The duration of the maintenance window in hours.</p>"""
    cutoff: "capo_ssm.types.maintenance_window_cutoff.MaintenanceWindowCutoff"
    """<p>The number of hours before the end of the maintenance window that Amazon Web Services Systems Manager stops scheduling new tasks for execution.</p>"""
    allow_unassociated_targets: "capo_ssm.types.maintenance_window_allow_unassociated_targets.MaintenanceWindowAllowUnassociatedTargets"
    """<p>Whether targets must be registered with the maintenance window before tasks can be defined for those targets.</p>"""
    enabled: "capo_ssm.types.maintenance_window_enabled.MaintenanceWindowEnabled"
    """<p>Indicates whether the maintenance window is enabled.</p>"""
    created_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the maintenance window was created.</p>"""
    modified_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the maintenance window was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowResult) -> dict:
    out: dict = {}
    if "window_id" in value:
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
    if "next_execution_time" in value:
        out["NextExecutionTime"] = value["next_execution_time"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    out["Cutoff"] = value.get("cutoff", 0)
    out["AllowUnassociatedTargets"] = value.get("allow_unassociated_targets", False)
    out["Enabled"] = value.get("enabled", False)
    if "created_date" in value:
        import capo_ssm.types.date_time

        out["CreatedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "modified_date" in value:
        import capo_ssm.types.date_time

        out["ModifiedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["modified_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowResult:
    out: GetMaintenanceWindowResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
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
    if data.get("NextExecutionTime") is not None:
        out["next_execution_time"] = data["NextExecutionTime"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("Cutoff") is not None:
        out["cutoff"] = data["Cutoff"]
    else:
        out["cutoff"] = 0
    if data.get("AllowUnassociatedTargets") is not None:
        out["allow_unassociated_targets"] = data["AllowUnassociatedTargets"]
    else:
        out["allow_unassociated_targets"] = False
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("CreatedDate") is not None:
        import capo_ssm.types.date_time

        out["created_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("ModifiedDate") is not None:
        import capo_ssm.types.date_time

        out["modified_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ModifiedDate"]
        )
    return out

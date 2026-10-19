"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#MaintenanceWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.apply_time_of
    import capo_workspaces_thin_client.types.day_of_week_list
    import capo_workspaces_thin_client.types.hour
    import capo_workspaces_thin_client.types.maintenance_window_type
    import capo_workspaces_thin_client.types.minute


class MaintenanceWindow(TypedDict, closed=True):
    type: "capo_workspaces_thin_client.types.maintenance_window_type.MaintenanceWindowType"
    """<p>An option to select the default or custom maintenance window.</p>"""
    start_time_hour: NotRequired["capo_workspaces_thin_client.types.hour.Hour"]
    """<p>The hour for the maintenance window start (<code>00</code>-<code>23</code>).</p>"""
    start_time_minute: NotRequired["capo_workspaces_thin_client.types.minute.Minute"]
    """<p>The minutes past the hour for the maintenance window start (<code>00</code>-<code>59</code>).</p>"""
    end_time_hour: NotRequired["capo_workspaces_thin_client.types.hour.Hour"]
    """<p>The hour for the maintenance window end (<code>00</code>-<code>23</code>).</p>"""
    end_time_minute: NotRequired["capo_workspaces_thin_client.types.minute.Minute"]
    """<p>The minutes for the maintenance window end (<code>00</code>-<code>59</code>).</p>"""
    days_of_the_week: NotRequired[
        "capo_workspaces_thin_client.types.day_of_week_list.DayOfWeekList"
    ]
    """<p>The days of the week during which the maintenance window is open.</p>"""
    apply_time_of: NotRequired[
        "capo_workspaces_thin_client.types.apply_time_of.ApplyTimeOf"
    ]
    """<p>The option to set the maintenance window during the device local time or Universal Coordinated Time (UTC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceWindow) -> dict:
    out: dict = {}
    import capo_workspaces_thin_client.types.maintenance_window_type

    out["type"] = (
        capo_workspaces_thin_client.types.maintenance_window_type.serialize_json(
            value["type"]
        )
    )
    if "start_time_hour" in value:
        out["startTimeHour"] = value["start_time_hour"]
    if "start_time_minute" in value:
        out["startTimeMinute"] = value["start_time_minute"]
    if "end_time_hour" in value:
        out["endTimeHour"] = value["end_time_hour"]
    if "end_time_minute" in value:
        out["endTimeMinute"] = value["end_time_minute"]
    if "days_of_the_week" in value:
        import capo_workspaces_thin_client.types.day_of_week_list

        out["daysOfTheWeek"] = (
            capo_workspaces_thin_client.types.day_of_week_list.serialize_json(
                value["days_of_the_week"]
            )
        )
    if "apply_time_of" in value:
        import capo_workspaces_thin_client.types.apply_time_of

        out["applyTimeOf"] = (
            capo_workspaces_thin_client.types.apply_time_of.serialize_json(
                value["apply_time_of"]
            )
        )
    return out


def deserialize_json(data: dict) -> MaintenanceWindow:
    out: MaintenanceWindow = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_workspaces_thin_client.types.maintenance_window_type

        out["type"] = (
            capo_workspaces_thin_client.types.maintenance_window_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_workspaces_thin_client.types.maintenance_window_type.MaintenanceWindowType",
            "",
        )
    if data.get("startTimeHour") is not None:
        out["start_time_hour"] = data["startTimeHour"]
    if data.get("startTimeMinute") is not None:
        out["start_time_minute"] = data["startTimeMinute"]
    if data.get("endTimeHour") is not None:
        out["end_time_hour"] = data["endTimeHour"]
    if data.get("endTimeMinute") is not None:
        out["end_time_minute"] = data["endTimeMinute"]
    if data.get("daysOfTheWeek") is not None:
        import capo_workspaces_thin_client.types.day_of_week_list

        out["days_of_the_week"] = (
            capo_workspaces_thin_client.types.day_of_week_list.deserialize_json(
                data["daysOfTheWeek"]
            )
        )
    if data.get("applyTimeOf") is not None:
        import capo_workspaces_thin_client.types.apply_time_of

        out["apply_time_of"] = (
            capo_workspaces_thin_client.types.apply_time_of.deserialize_json(
                data["applyTimeOf"]
            )
        )
    return out

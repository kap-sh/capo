"""Generated from Smithy shape ``com.amazonaws.backupgateway#MaintenanceStartTime``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.day_of_month
    import capo_backup_gateway.types.day_of_week
    import capo_backup_gateway.types.hour_of_day
    import capo_backup_gateway.types.minute_of_hour


class MaintenanceStartTime(TypedDict, closed=True):
    day_of_month: NotRequired["capo_backup_gateway.types.day_of_month.DayOfMonth"]
    """<p>The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month and 28 represents the last day of the month.</p>"""
    day_of_week: NotRequired["capo_backup_gateway.types.day_of_week.DayOfWeek"]
    """<p>An ordinal number between 0 and 6 that represents the day of the week, where 0 represents Sunday and 6 represents Saturday. The day of week is in the time zone of the gateway.</p>"""
    hour_of_day: "capo_backup_gateway.types.hour_of_day.HourOfDay"
    """<p>The hour component of the maintenance start time represented as <i>hh</i>, where <i>hh</i> is the hour (0 to 23). The hour of the day is in the time zone of the gateway.</p>"""
    minute_of_hour: "capo_backup_gateway.types.minute_of_hour.MinuteOfHour"
    """<p>The minute component of the maintenance start time represented as <i>mm</i>, where <i>mm</i> is the minute (0 to 59). The minute of the hour is in the time zone of the gateway.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MaintenanceStartTime) -> dict:
    out: dict = {}
    if "day_of_month" in value:
        out["DayOfMonth"] = value["day_of_month"]
    if "day_of_week" in value:
        out["DayOfWeek"] = value["day_of_week"]
    out["HourOfDay"] = value["hour_of_day"]
    out["MinuteOfHour"] = value["minute_of_hour"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MaintenanceStartTime:
    out: MaintenanceStartTime = {}  # type: ignore[typeddict-item]
    if data.get("DayOfMonth") is not None:
        out["day_of_month"] = data["DayOfMonth"]
    if data.get("DayOfWeek") is not None:
        out["day_of_week"] = data["DayOfWeek"]
    if data.get("HourOfDay") is not None:
        out["hour_of_day"] = data["HourOfDay"]
    else:
        out["hour_of_day"] = 0
    if data.get("MinuteOfHour") is not None:
        out["minute_of_hour"] = data["MinuteOfHour"]
    else:
        out["minute_of_hour"] = 0
    return out

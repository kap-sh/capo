"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateMaintenanceStartTimeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.day_of_month
    import capo_storage_gateway.types.day_of_week
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.hour_of_day
    import capo_storage_gateway.types.minute_of_hour
    import capo_storage_gateway.types.software_update_preferences


class UpdateMaintenanceStartTimeInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    hour_of_day: NotRequired["capo_storage_gateway.types.hour_of_day.HourOfDay"]
    """<p>The hour component of the maintenance start time represented as <i>hh</i>, where <i>hh</i> is the hour (00 to 23). The hour of the day is in the time zone of the gateway.</p>"""
    minute_of_hour: NotRequired[
        "capo_storage_gateway.types.minute_of_hour.MinuteOfHour"
    ]
    """<p>The minute component of the maintenance start time represented as <i>mm</i>, where <i>mm</i> is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.</p>"""
    day_of_week: NotRequired["capo_storage_gateway.types.day_of_week.DayOfWeek"]
    """<p>The day of the week component of the maintenance start time week represented as an ordinal number from 0 to 6, where 0 represents Sunday and 6 represents Saturday.</p>"""
    day_of_month: NotRequired["capo_storage_gateway.types.day_of_month.DayOfMonth"]
    """<p>The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month. It is not possible to set the maintenance schedule to start on days 29 through 31.</p>"""
    software_update_preferences: NotRequired[
        "capo_storage_gateway.types.software_update_preferences.SoftwareUpdatePreferences"
    ]
    """<p>A set of variables indicating the software update preferences for the gateway.</p> <p>Includes <code>AutomaticUpdatePolicy</code> field with the following inputs:</p> <p> <code>ALL_VERSIONS</code> - Enables regular gateway maintenance updates.</p> <p> <code>EMERGENCY_VERSIONS_ONLY</code> - Disables regular gateway maintenance updates. The gateway will still receive emergency version updates on rare occasions if necessary to remedy highly critical security or durability issues. You will be notified before an emergency version update is applied. These updates are applied during your gateway's scheduled maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMaintenanceStartTimeInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    if "hour_of_day" in value:
        out["HourOfDay"] = value["hour_of_day"]
    if "minute_of_hour" in value:
        out["MinuteOfHour"] = value["minute_of_hour"]
    if "day_of_week" in value:
        out["DayOfWeek"] = value["day_of_week"]
    if "day_of_month" in value:
        out["DayOfMonth"] = value["day_of_month"]
    if "software_update_preferences" in value:
        import capo_storage_gateway.types.software_update_preferences

        out["SoftwareUpdatePreferences"] = (
            capo_storage_gateway.types.software_update_preferences.serialize_aws_json_1_1(
                value["software_update_preferences"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMaintenanceStartTimeInput:
    out: UpdateMaintenanceStartTimeInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("HourOfDay") is not None:
        out["hour_of_day"] = data["HourOfDay"]
    if data.get("MinuteOfHour") is not None:
        out["minute_of_hour"] = data["MinuteOfHour"]
    if data.get("DayOfWeek") is not None:
        out["day_of_week"] = data["DayOfWeek"]
    if data.get("DayOfMonth") is not None:
        out["day_of_month"] = data["DayOfMonth"]
    if data.get("SoftwareUpdatePreferences") is not None:
        import capo_storage_gateway.types.software_update_preferences

        out["software_update_preferences"] = (
            capo_storage_gateway.types.software_update_preferences.deserialize_aws_json_1_1(
                data["SoftwareUpdatePreferences"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppCallHours``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.iana_timezone
    import capo_socialmessaging.types.whats_app_holiday_schedule_list
    import capo_socialmessaging.types.whats_app_weekly_operating_hours_list


class WhatsAppCallHours(TypedDict, closed=True):
    enabled: "bool"
    """<p>Specifies whether call hours are enforced. When disabled, the business accepts calls at any time.</p>"""
    timezone: "capo_socialmessaging.types.iana_timezone.IanaTimezone"
    """<p>The IANA time zone in which the operating hours are interpreted, such as <code>America/New_York</code>.</p>"""
    weekly_operating_hours: "capo_socialmessaging.types.whats_app_weekly_operating_hours_list.WhatsAppWeeklyOperatingHoursList"
    """<p>The weekly schedule of hours during which the business accepts calls.</p>"""
    holiday_schedule: NotRequired[
        "capo_socialmessaging.types.whats_app_holiday_schedule_list.WhatsAppHolidayScheduleList"
    ]
    """<p>Date-specific overrides to the weekly operating hours, such as holidays.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppCallHours) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    out["timezone"] = value["timezone"]
    import capo_socialmessaging.types.whats_app_weekly_operating_hours_list

    out["weeklyOperatingHours"] = (
        capo_socialmessaging.types.whats_app_weekly_operating_hours_list.serialize_json(
            value["weekly_operating_hours"]
        )
    )
    if "holiday_schedule" in value:
        import capo_socialmessaging.types.whats_app_holiday_schedule_list

        out["holidaySchedule"] = (
            capo_socialmessaging.types.whats_app_holiday_schedule_list.serialize_json(
                value["holiday_schedule"]
            )
        )
    return out


def deserialize_json(data: dict) -> WhatsAppCallHours:
    out: WhatsAppCallHours = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("timezone") is not None:
        out["timezone"] = data["timezone"]
    else:
        out["timezone"] = ""
    if data.get("weeklyOperatingHours") is not None:
        import capo_socialmessaging.types.whats_app_weekly_operating_hours_list

        out["weekly_operating_hours"] = (
            capo_socialmessaging.types.whats_app_weekly_operating_hours_list.deserialize_json(
                data["weeklyOperatingHours"]
            )
        )
    else:
        out["weekly_operating_hours"] = []
    if data.get("holidaySchedule") is not None:
        import capo_socialmessaging.types.whats_app_holiday_schedule_list

        out["holiday_schedule"] = (
            capo_socialmessaging.types.whats_app_holiday_schedule_list.deserialize_json(
                data["holidaySchedule"]
            )
        )
    return out

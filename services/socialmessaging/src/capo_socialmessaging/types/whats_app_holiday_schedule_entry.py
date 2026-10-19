"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppHolidayScheduleEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_date
    import capo_socialmessaging.types.whats_app_time_of_day


class WhatsAppHolidayScheduleEntry(TypedDict, closed=True):
    date: "capo_socialmessaging.types.whats_app_date.WhatsAppDate"
    """<p>The date that the override applies to, in ISO 8601 format (<code>YYYY-MM-DD</code>).</p>"""
    start_time: "capo_socialmessaging.types.whats_app_time_of_day.WhatsAppTimeOfDay"
    """<p>The time of day when the business begins accepting calls on the override date.</p>"""
    end_time: "capo_socialmessaging.types.whats_app_time_of_day.WhatsAppTimeOfDay"
    """<p>The time of day when the business stops accepting calls on the override date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppHolidayScheduleEntry) -> dict:
    out: dict = {}
    out["date"] = value["date"]
    import capo_socialmessaging.types.whats_app_time_of_day

    out["startTime"] = capo_socialmessaging.types.whats_app_time_of_day.serialize_json(
        value["start_time"]
    )
    import capo_socialmessaging.types.whats_app_time_of_day

    out["endTime"] = capo_socialmessaging.types.whats_app_time_of_day.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> WhatsAppHolidayScheduleEntry:
    out: WhatsAppHolidayScheduleEntry = {}  # type: ignore[typeddict-item]
    if data.get("date") is not None:
        out["date"] = data["date"]
    else:
        out["date"] = ""
    if data.get("startTime") is not None:
        import capo_socialmessaging.types.whats_app_time_of_day

        out["start_time"] = (
            capo_socialmessaging.types.whats_app_time_of_day.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("WhatsAppHolidayScheduleEntry.start_time required")
    if data.get("endTime") is not None:
        import capo_socialmessaging.types.whats_app_time_of_day

        out["end_time"] = (
            capo_socialmessaging.types.whats_app_time_of_day.deserialize_json(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError("WhatsAppHolidayScheduleEntry.end_time required")
    return out

"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppWeeklyOperatingHoursEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_day_of_week
    import capo_socialmessaging.types.whats_app_time_of_day


class WhatsAppWeeklyOperatingHoursEntry(TypedDict, closed=True):
    day_of_week: "capo_socialmessaging.types.whats_app_day_of_week.WhatsAppDayOfWeek"
    """<p>The day of the week that the entry applies to.</p>"""
    open_time: "capo_socialmessaging.types.whats_app_time_of_day.WhatsAppTimeOfDay"
    """<p>The time of day when the business begins accepting calls.</p>"""
    close_time: "capo_socialmessaging.types.whats_app_time_of_day.WhatsAppTimeOfDay"
    """<p>The time of day when the business stops accepting calls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppWeeklyOperatingHoursEntry) -> dict:
    out: dict = {}
    import capo_socialmessaging.types.whats_app_day_of_week

    out["dayOfWeek"] = capo_socialmessaging.types.whats_app_day_of_week.serialize_json(
        value["day_of_week"]
    )
    import capo_socialmessaging.types.whats_app_time_of_day

    out["openTime"] = capo_socialmessaging.types.whats_app_time_of_day.serialize_json(
        value["open_time"]
    )
    import capo_socialmessaging.types.whats_app_time_of_day

    out["closeTime"] = capo_socialmessaging.types.whats_app_time_of_day.serialize_json(
        value["close_time"]
    )
    return out


def deserialize_json(data: dict) -> WhatsAppWeeklyOperatingHoursEntry:
    out: WhatsAppWeeklyOperatingHoursEntry = {}  # type: ignore[typeddict-item]
    if data.get("dayOfWeek") is not None:
        import capo_socialmessaging.types.whats_app_day_of_week

        out["day_of_week"] = (
            capo_socialmessaging.types.whats_app_day_of_week.deserialize_json(
                data["dayOfWeek"]
            )
        )
    else:
        import typing

        out["day_of_week"] = typing.cast(
            "capo_socialmessaging.types.whats_app_day_of_week.WhatsAppDayOfWeek", ""
        )
    if data.get("openTime") is not None:
        import capo_socialmessaging.types.whats_app_time_of_day

        out["open_time"] = (
            capo_socialmessaging.types.whats_app_time_of_day.deserialize_json(
                data["openTime"]
            )
        )
    else:
        raise DeserializationError(
            "WhatsAppWeeklyOperatingHoursEntry.open_time required"
        )
    if data.get("closeTime") is not None:
        import capo_socialmessaging.types.whats_app_time_of_day

        out["close_time"] = (
            capo_socialmessaging.types.whats_app_time_of_day.deserialize_json(
                data["closeTime"]
            )
        )
    else:
        raise DeserializationError(
            "WhatsAppWeeklyOperatingHoursEntry.close_time required"
        )
    return out

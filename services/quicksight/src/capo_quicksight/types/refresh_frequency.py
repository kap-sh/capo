"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshFrequency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.refresh_interval
    import capo_quicksight.types.schedule_refresh_on_entity
    import capo_quicksight.types.string


class RefreshFrequency(TypedDict, closed=True):
    interval: "capo_quicksight.types.refresh_interval.RefreshInterval"
    """<p>The interval between scheduled refreshes. Valid values are as follows:</p> <ul> <li> <p> <code>MINUTE15</code>: The dataset refreshes every 15 minutes. This value is only supported for incremental refreshes. This interval can only be used for one schedule per dataset.</p> </li> <li> <p> <code>MINUTE30</code>:The dataset refreshes every 30 minutes. This value is only supported for incremental refreshes. This interval can only be used for one schedule per dataset.</p> </li> <li> <p> <code>HOURLY</code>: The dataset refreshes every hour. This interval can only be used for one schedule per dataset.</p> </li> <li> <p> <code>DAILY</code>: The dataset refreshes every day.</p> </li> <li> <p> <code>WEEKLY</code>: The dataset refreshes every week.</p> </li> <li> <p> <code>MONTHLY</code>: The dataset refreshes every month.</p> </li> </ul>"""
    refresh_on_day: NotRequired[
        "capo_quicksight.types.schedule_refresh_on_entity.ScheduleRefreshOnEntity"
    ]
    """<p>The day of the week that you want to schedule the refresh on. This value is required for weekly and monthly refresh intervals.</p>"""
    timezone: NotRequired["capo_quicksight.types.string.String"]
    """<p>The timezone that you want the refresh schedule to use. The timezone ID must match a corresponding ID found on <code>java.util.time.getAvailableIDs()</code>.</p>"""
    time_of_the_day: NotRequired["capo_quicksight.types.string.String"]
    """<p>The time of day that you want the datset to refresh. This value is expressed in HH:MM format. This field is not required for schedules that refresh hourly.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshFrequency) -> dict:
    out: dict = {}
    import capo_quicksight.types.refresh_interval

    out["Interval"] = capo_quicksight.types.refresh_interval.serialize_json(
        value["interval"]
    )
    if "refresh_on_day" in value:
        import capo_quicksight.types.schedule_refresh_on_entity

        out["RefreshOnDay"] = (
            capo_quicksight.types.schedule_refresh_on_entity.serialize_json(
                value["refresh_on_day"]
            )
        )
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "time_of_the_day" in value:
        out["TimeOfTheDay"] = value["time_of_the_day"]
    return out


def deserialize_json(data: dict) -> RefreshFrequency:
    out: RefreshFrequency = {}  # type: ignore[typeddict-item]
    if data.get("Interval") is not None:
        import capo_quicksight.types.refresh_interval

        out["interval"] = capo_quicksight.types.refresh_interval.deserialize_json(
            data["Interval"]
        )
    else:
        import typing

        out["interval"] = typing.cast(
            "capo_quicksight.types.refresh_interval.RefreshInterval", ""
        )
    if data.get("RefreshOnDay") is not None:
        import capo_quicksight.types.schedule_refresh_on_entity

        out["refresh_on_day"] = (
            capo_quicksight.types.schedule_refresh_on_entity.deserialize_json(
                data["RefreshOnDay"]
            )
        )
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    if data.get("TimeOfTheDay") is not None:
        out["time_of_the_day"] = data["TimeOfTheDay"]
    return out

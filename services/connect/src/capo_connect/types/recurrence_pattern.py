"""Generated from Smithy shape ``com.amazonaws.connect#RecurrencePattern``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.interval_positive_integer
    import capo_connect.types.month_day_list
    import capo_connect.types.month_list
    import capo_connect.types.recurrence_frequency
    import capo_connect.types.weekday_occurrence_list


class RecurrencePattern(TypedDict, closed=True):
    frequency: "capo_connect.types.recurrence_frequency.RecurrenceFrequency"
    """<p>Defines how often the pattern repeats. This is the base unit for the recurrence schedule and works in conjunction with the Interval field to determine the exact repetition sequence.</p>"""
    interval: "capo_connect.types.interval_positive_integer.IntervalPositiveInteger"
    """<p>Specifies the number of frequency units between each occurrence. Must be a positive integer. </p> <p> Examples: To repeat every week, set Interval=1 with WEEKLY frequency. To repeat every two months, set Interval=2 with MONTHLY frequency.</p>"""
    by_month: NotRequired["capo_connect.types.month_list.MonthList"]
    """<p>Specifies which month the event should occur in (1-12, where 1=January, 12=December). Used with YEARLY frequency to schedule events in specific month. </p> <p>Note: It does not accept multiple values in the same list</p>"""
    by_month_day: NotRequired["capo_connect.types.month_day_list.MonthDayList"]
    """<p>Specifies which day of the month the event should occur on (1-31). Used with MONTHLY or YEARLY frequency to schedule events on specific date within a month.</p> <p> Examples: [15] for events on the 15th of each month, [-1] for events on the last day of month. </p> <p>Note: It does not accept multiple values in the same list. If a specified day doesn't exist in a particular month (e.g., day 31 in February), the event will be skipped for that month. This field cannot be used simultaneously with ByWeekdayOccurrence as they represent different scheduling approaches (specific dates vs. relative weekday positions).</p>"""
    by_weekday_occurrence: NotRequired[
        "capo_connect.types.weekday_occurrence_list.WeekdayOccurrenceList"
    ]
    """<p>Specifies which occurrence of a weekday within the month the event should occur on. Must be used with MONTHLY or YEARLY frequency. </p> <p>Example: 2 corresponds to second occurrence of the weekday in the month. -1 corresponds to last occurrence of the weekday in the month </p> <p>The weekday itself is specified separately in the HoursOfOperationConfig. Example: To schedule the recurring event for the 2nd Thursday of April every year, set ByWeekdayOccurrence=[2], Day=THURSDAY, ByMonth=[4], Frequency: YEARLY and INTERVAL=1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecurrencePattern) -> dict:
    out: dict = {}
    import capo_connect.types.recurrence_frequency

    out["Frequency"] = capo_connect.types.recurrence_frequency.serialize_json(
        value["frequency"]
    )
    out["Interval"] = value["interval"]
    if "by_month" in value:
        import capo_connect.types.month_list

        out["ByMonth"] = capo_connect.types.month_list.serialize_json(value["by_month"])
    if "by_month_day" in value:
        import capo_connect.types.month_day_list

        out["ByMonthDay"] = capo_connect.types.month_day_list.serialize_json(
            value["by_month_day"]
        )
    if "by_weekday_occurrence" in value:
        import capo_connect.types.weekday_occurrence_list

        out["ByWeekdayOccurrence"] = (
            capo_connect.types.weekday_occurrence_list.serialize_json(
                value["by_weekday_occurrence"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecurrencePattern:
    out: RecurrencePattern = {}  # type: ignore[typeddict-item]
    if data.get("Frequency") is not None:
        import capo_connect.types.recurrence_frequency

        out["frequency"] = capo_connect.types.recurrence_frequency.deserialize_json(
            data["Frequency"]
        )
    else:
        import typing

        out["frequency"] = typing.cast(
            "capo_connect.types.recurrence_frequency.RecurrenceFrequency", ""
        )
    if data.get("Interval") is not None:
        out["interval"] = data["Interval"]
    else:
        out["interval"] = 0
    if data.get("ByMonth") is not None:
        import capo_connect.types.month_list

        out["by_month"] = capo_connect.types.month_list.deserialize_json(
            data["ByMonth"]
        )
    if data.get("ByMonthDay") is not None:
        import capo_connect.types.month_day_list

        out["by_month_day"] = capo_connect.types.month_day_list.deserialize_json(
            data["ByMonthDay"]
        )
    if data.get("ByWeekdayOccurrence") is not None:
        import capo_connect.types.weekday_occurrence_list

        out["by_weekday_occurrence"] = (
            capo_connect.types.weekday_occurrence_list.deserialize_json(
                data["ByWeekdayOccurrence"]
            )
        )
    return out

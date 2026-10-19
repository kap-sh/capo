"""Generated from Smithy shape ``com.amazonaws.customerprofiles#JobSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.job_schedule_day_of_the_week
    import capo_customer_profiles.types.job_schedule_time


class JobSchedule(TypedDict, closed=True):
    day_of_the_week: "capo_customer_profiles.types.job_schedule_day_of_the_week.JobScheduleDayOfTheWeek"
    """<p>The day when the Identity Resolution Job should run every week.</p>"""
    time: "capo_customer_profiles.types.job_schedule_time.JobScheduleTime"
    """<p>The time when the Identity Resolution Job should run every week.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSchedule) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.job_schedule_day_of_the_week

    out["DayOfTheWeek"] = (
        capo_customer_profiles.types.job_schedule_day_of_the_week.serialize_json(
            value["day_of_the_week"]
        )
    )
    out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> JobSchedule:
    out: JobSchedule = {}  # type: ignore[typeddict-item]
    if data.get("DayOfTheWeek") is not None:
        import capo_customer_profiles.types.job_schedule_day_of_the_week

        out["day_of_the_week"] = (
            capo_customer_profiles.types.job_schedule_day_of_the_week.deserialize_json(
                data["DayOfTheWeek"]
            )
        )
    else:
        import typing

        out["day_of_the_week"] = typing.cast(
            "capo_customer_profiles.types.job_schedule_day_of_the_week.JobScheduleDayOfTheWeek",
            "",
        )
    if data.get("Time") is not None:
        out["time"] = data["Time"]
    else:
        out["time"] = ""
    return out

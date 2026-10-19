"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ScheduledTriggerProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.data_pull_mode
    import capo_customer_profiles.types.date
    import capo_customer_profiles.types.schedule_expression
    import capo_customer_profiles.types.schedule_offset
    import capo_customer_profiles.types.timezone


class ScheduledTriggerProperties(TypedDict, closed=True):
    schedule_expression: (
        "capo_customer_profiles.types.schedule_expression.ScheduleExpression"
    )
    """<p>The scheduling expression that determines the rate at which the schedule will run, for example rate (5 minutes).</p>"""
    data_pull_mode: NotRequired[
        "capo_customer_profiles.types.data_pull_mode.DataPullMode"
    ]
    """<p>Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.</p>"""
    schedule_start_time: NotRequired["capo_customer_profiles.types.date.Date"]
    """<p>Specifies the scheduled start time for a scheduled-trigger flow.</p>"""
    schedule_end_time: NotRequired["capo_customer_profiles.types.date.Date"]
    """<p>Specifies the scheduled end time for a scheduled-trigger flow.</p>"""
    timezone: NotRequired["capo_customer_profiles.types.timezone.Timezone"]
    """<p>Specifies the time zone used when referring to the date and time of a scheduled-triggered flow, such as America/New_York.</p>"""
    schedule_offset: NotRequired[
        "capo_customer_profiles.types.schedule_offset.ScheduleOffset"
    ]
    """<p>Specifies the optional offset that is added to the time interval for a schedule-triggered flow.</p>"""
    first_execution_from: NotRequired["capo_customer_profiles.types.date.Date"]
    """<p>Specifies the date range for the records to import from the connector in the first flow run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledTriggerProperties) -> dict:
    out: dict = {}
    out["ScheduleExpression"] = value["schedule_expression"]
    if "data_pull_mode" in value:
        import capo_customer_profiles.types.data_pull_mode

        out["DataPullMode"] = (
            capo_customer_profiles.types.data_pull_mode.serialize_json(
                value["data_pull_mode"]
            )
        )
    if "schedule_start_time" in value:
        import capo_customer_profiles.types.date

        out["ScheduleStartTime"] = capo_customer_profiles.types.date.serialize_json(
            value["schedule_start_time"]
        )
    if "schedule_end_time" in value:
        import capo_customer_profiles.types.date

        out["ScheduleEndTime"] = capo_customer_profiles.types.date.serialize_json(
            value["schedule_end_time"]
        )
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "schedule_offset" in value:
        out["ScheduleOffset"] = value["schedule_offset"]
    if "first_execution_from" in value:
        import capo_customer_profiles.types.date

        out["FirstExecutionFrom"] = capo_customer_profiles.types.date.serialize_json(
            value["first_execution_from"]
        )
    return out


def deserialize_json(data: dict) -> ScheduledTriggerProperties:
    out: ScheduledTriggerProperties = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    else:
        out["schedule_expression"] = ""
    if data.get("DataPullMode") is not None:
        import capo_customer_profiles.types.data_pull_mode

        out["data_pull_mode"] = (
            capo_customer_profiles.types.data_pull_mode.deserialize_json(
                data["DataPullMode"]
            )
        )
    if data.get("ScheduleStartTime") is not None:
        import capo_customer_profiles.types.date

        out["schedule_start_time"] = capo_customer_profiles.types.date.deserialize_json(
            data["ScheduleStartTime"]
        )
    if data.get("ScheduleEndTime") is not None:
        import capo_customer_profiles.types.date

        out["schedule_end_time"] = capo_customer_profiles.types.date.deserialize_json(
            data["ScheduleEndTime"]
        )
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    if data.get("ScheduleOffset") is not None:
        out["schedule_offset"] = data["ScheduleOffset"]
    if data.get("FirstExecutionFrom") is not None:
        import capo_customer_profiles.types.date

        out["first_execution_from"] = (
            capo_customer_profiles.types.date.deserialize_json(
                data["FirstExecutionFrom"]
            )
        )
    return out

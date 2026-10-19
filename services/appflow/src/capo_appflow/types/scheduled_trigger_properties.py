"""Generated from Smithy shape ``com.amazonaws.appflow#ScheduledTriggerProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.data_pull_mode
    import capo_appflow.types.date
    import capo_appflow.types.flow_error_deactivation_threshold
    import capo_appflow.types.schedule_expression
    import capo_appflow.types.schedule_offset
    import capo_appflow.types.timezone


class ScheduledTriggerProperties(TypedDict, closed=True):
    schedule_expression: "capo_appflow.types.schedule_expression.ScheduleExpression"
    """<p> The scheduling expression that determines the rate at which the schedule will run, for example <code>rate(5minutes)</code>. </p>"""
    data_pull_mode: NotRequired["capo_appflow.types.data_pull_mode.DataPullMode"]
    """<p> Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run. </p>"""
    schedule_start_time: NotRequired["capo_appflow.types.date.Date"]
    """<p>The time at which the scheduled flow starts. The time is formatted as a timestamp that follows the ISO 8601 standard, such as <code>2022-04-26T13:00:00-07:00</code>.</p>"""
    schedule_end_time: NotRequired["capo_appflow.types.date.Date"]
    """<p>The time at which the scheduled flow ends. The time is formatted as a timestamp that follows the ISO 8601 standard, such as <code>2022-04-27T13:00:00-07:00</code>.</p>"""
    timezone: NotRequired["capo_appflow.types.timezone.Timezone"]
    """<p>Specifies the time zone used when referring to the dates and times of a scheduled flow, such as <code>America/New_York</code>. This time zone is only a descriptive label. It doesn't affect how Amazon AppFlow interprets the timestamps that you specify to schedule the flow.</p> <p>If you want to schedule a flow by using times in a particular time zone, indicate the time zone as a UTC offset in your timestamps. For example, the UTC offsets for the <code>America/New_York</code> timezone are <code>-04:00</code> EDT and <code>-05:00 EST</code>.</p>"""
    schedule_offset: NotRequired["capo_appflow.types.schedule_offset.ScheduleOffset"]
    """<p> Specifies the optional offset that is added to the time interval for a schedule-triggered flow. </p>"""
    first_execution_from: NotRequired["capo_appflow.types.date.Date"]
    """<p> Specifies the date range for the records to import from the connector in the first flow run. </p>"""
    flow_error_deactivation_threshold: NotRequired[
        "capo_appflow.types.flow_error_deactivation_threshold.FlowErrorDeactivationThreshold"
    ]
    """<p>Defines how many times a scheduled flow fails consecutively before Amazon AppFlow deactivates it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledTriggerProperties) -> dict:
    out: dict = {}
    out["scheduleExpression"] = value["schedule_expression"]
    if "data_pull_mode" in value:
        import capo_appflow.types.data_pull_mode

        out["dataPullMode"] = capo_appflow.types.data_pull_mode.serialize_json(
            value["data_pull_mode"]
        )
    if "schedule_start_time" in value:
        import capo_appflow.types.date

        out["scheduleStartTime"] = capo_appflow.types.date.serialize_json(
            value["schedule_start_time"]
        )
    if "schedule_end_time" in value:
        import capo_appflow.types.date

        out["scheduleEndTime"] = capo_appflow.types.date.serialize_json(
            value["schedule_end_time"]
        )
    if "timezone" in value:
        out["timezone"] = value["timezone"]
    if "schedule_offset" in value:
        out["scheduleOffset"] = value["schedule_offset"]
    if "first_execution_from" in value:
        import capo_appflow.types.date

        out["firstExecutionFrom"] = capo_appflow.types.date.serialize_json(
            value["first_execution_from"]
        )
    if "flow_error_deactivation_threshold" in value:
        out["flowErrorDeactivationThreshold"] = value[
            "flow_error_deactivation_threshold"
        ]
    return out


def deserialize_json(data: dict) -> ScheduledTriggerProperties:
    out: ScheduledTriggerProperties = {}  # type: ignore[typeddict-item]
    if data.get("scheduleExpression") is not None:
        out["schedule_expression"] = data["scheduleExpression"]
    else:
        out["schedule_expression"] = ""
    if data.get("dataPullMode") is not None:
        import capo_appflow.types.data_pull_mode

        out["data_pull_mode"] = capo_appflow.types.data_pull_mode.deserialize_json(
            data["dataPullMode"]
        )
    if data.get("scheduleStartTime") is not None:
        import capo_appflow.types.date

        out["schedule_start_time"] = capo_appflow.types.date.deserialize_json(
            data["scheduleStartTime"]
        )
    if data.get("scheduleEndTime") is not None:
        import capo_appflow.types.date

        out["schedule_end_time"] = capo_appflow.types.date.deserialize_json(
            data["scheduleEndTime"]
        )
    if data.get("timezone") is not None:
        out["timezone"] = data["timezone"]
    if data.get("scheduleOffset") is not None:
        out["schedule_offset"] = data["scheduleOffset"]
    if data.get("firstExecutionFrom") is not None:
        import capo_appflow.types.date

        out["first_execution_from"] = capo_appflow.types.date.deserialize_json(
            data["firstExecutionFrom"]
        )
    if data.get("flowErrorDeactivationThreshold") is not None:
        out["flow_error_deactivation_threshold"] = data[
            "flowErrorDeactivationThreshold"
        ]
    return out

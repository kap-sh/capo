"""Generated from Smithy shape ``com.amazonaws.glue#Schedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.cron_expression
    import capo_glue.types.schedule_state


class Schedule(TypedDict, closed=True):
    schedule_expression: NotRequired["capo_glue.types.cron_expression.CronExpression"]
    """<p>A <code>cron</code> expression used to specify the schedule (see <a href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p>"""
    state: NotRequired["capo_glue.types.schedule_state.ScheduleState"]
    """<p>The state of the schedule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Schedule) -> dict:
    out: dict = {}
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "state" in value:
        import capo_glue.types.schedule_state

        out["State"] = capo_glue.types.schedule_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("State") is not None:
        import capo_glue.types.schedule_state

        out["state"] = capo_glue.types.schedule_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.cron_expression
    import capo_databrew.types.job_name_list
    import capo_databrew.types.schedule_name


class UpdateScheduleRequest(TypedDict, closed=True):
    job_names: NotRequired["capo_databrew.types.job_name_list.JobNameList"]
    """<p>The name or names of one or more jobs to be run for this schedule.</p>"""
    cron_expression: "capo_databrew.types.cron_expression.CronExpression"
    """<p>The date or dates and time or times when the jobs are to be run. For more information, see <a href="https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html">Cron expressions</a> in the <i>Glue DataBrew Developer Guide</i>.</p>"""
    name: "capo_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScheduleRequest) -> dict:
    out: dict = {}
    if "job_names" in value:
        import capo_databrew.types.job_name_list

        out["JobNames"] = capo_databrew.types.job_name_list.serialize_json(
            value["job_names"]
        )
    out["CronExpression"] = value["cron_expression"]
    return out


def deserialize_json(data: dict) -> UpdateScheduleRequest:
    out: UpdateScheduleRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobNames") is not None:
        import capo_databrew.types.job_name_list

        out["job_names"] = capo_databrew.types.job_name_list.deserialize_json(
            data["JobNames"]
        )
    if data.get("CronExpression") is not None:
        out["cron_expression"] = data["CronExpression"]
    else:
        raise DeserializationError("UpdateScheduleRequest.cron_expression required")
    return out

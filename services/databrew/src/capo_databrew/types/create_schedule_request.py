"""Generated from Smithy shape ``com.amazonaws.databrew#CreateScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.cron_expression
    import capo_databrew.types.job_name_list
    import capo_databrew.types.schedule_name
    import capo_databrew.types.tag_map


class CreateScheduleRequest(TypedDict, closed=True):
    job_names: NotRequired["capo_databrew.types.job_name_list.JobNameList"]
    """<p>The name or names of one or more jobs to be run.</p>"""
    cron_expression: "capo_databrew.types.cron_expression.CronExpression"
    """<p>The date or dates and time or times when the jobs are to be run. For more information, see <a href="https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html">Cron expressions</a> in the <i>Glue DataBrew Developer Guide</i>.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to this schedule.</p>"""
    name: "capo_databrew.types.schedule_name.ScheduleName"
    """<p>A unique name for the schedule. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleRequest) -> dict:
    out: dict = {}
    if "job_names" in value:
        import capo_databrew.types.job_name_list

        out["JobNames"] = capo_databrew.types.job_name_list.serialize_json(
            value["job_names"]
        )
    out["CronExpression"] = value["cron_expression"]
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateScheduleRequest:
    out: CreateScheduleRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobNames") is not None:
        import capo_databrew.types.job_name_list

        out["job_names"] = capo_databrew.types.job_name_list.deserialize_json(
            data["JobNames"]
        )
    if data.get("CronExpression") is not None:
        out["cron_expression"] = data["CronExpression"]
    else:
        raise DeserializationError("CreateScheduleRequest.cron_expression required")
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateScheduleRequest.name required")
    return out

"""Generated from Smithy shape ``com.amazonaws.databrew#Schedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.account_id
    import capo_databrew.types.arn
    import capo_databrew.types.created_by
    import capo_databrew.types.cron_expression
    import capo_databrew.types.date
    import capo_databrew.types.job_name_list
    import capo_databrew.types.last_modified_by
    import capo_databrew.types.schedule_name
    import capo_databrew.types.tag_map


class Schedule(TypedDict, closed=True):
    account_id: NotRequired["capo_databrew.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the schedule.</p>"""
    created_by: NotRequired["capo_databrew.types.created_by.CreatedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who created the schedule.</p>"""
    create_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time that the schedule was created.</p>"""
    job_names: NotRequired["capo_databrew.types.job_name_list.JobNameList"]
    """<p>A list of jobs to be run, according to the schedule.</p>"""
    last_modified_by: NotRequired["capo_databrew.types.last_modified_by.LastModifiedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who last modified the schedule.</p>"""
    last_modified_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time when the schedule was last modified.</p>"""
    resource_arn: NotRequired["capo_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the schedule.</p>"""
    cron_expression: NotRequired["capo_databrew.types.cron_expression.CronExpression"]
    """<p>The dates and times when the job is to run. For more information, see <a href="https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html">Cron expressions</a> in the <i>Glue DataBrew Developer Guide</i>.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags that have been applied to the schedule.</p>"""
    name: "capo_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Schedule) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "create_date" in value:
        import capo_databrew.types.date

        out["CreateDate"] = capo_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "job_names" in value:
        import capo_databrew.types.job_name_list

        out["JobNames"] = capo_databrew.types.job_name_list.serialize_json(
            value["job_names"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        import capo_databrew.types.date

        out["LastModifiedDate"] = capo_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "cron_expression" in value:
        out["CronExpression"] = value["cron_expression"]
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("CreateDate") is not None:
        import capo_databrew.types.date

        out["create_date"] = capo_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if data.get("JobNames") is not None:
        import capo_databrew.types.job_name_list

        out["job_names"] = capo_databrew.types.job_name_list.deserialize_json(
            data["JobNames"]
        )
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("LastModifiedDate") is not None:
        import capo_databrew.types.date

        out["last_modified_date"] = capo_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("CronExpression") is not None:
        out["cron_expression"] = data["CronExpression"]
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Schedule.name required")
    return out

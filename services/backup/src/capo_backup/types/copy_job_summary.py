"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.account_id
    import capo_backup.types.copy_job_status
    import capo_backup.types.integer
    import capo_backup.types.message_category
    import capo_backup.types.region
    import capo_backup.types.resource_type
    import capo_backup.types.timestamp


class CopyJobSummary(TypedDict, closed=True):
    region: NotRequired["capo_backup.types.region.Region"]
    """<p>The Amazon Web Services Regions within the job summary.</p>"""
    account_id: NotRequired["capo_backup.types.account_id.AccountId"]
    """<p>The account ID that owns the jobs within the summary.</p>"""
    state: NotRequired["capo_backup.types.copy_job_status.CopyJobStatus"]
    """<p>This value is job count for jobs with the specified state.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>This value is the job count for the specified resource type. The request <code>GetSupportedResourceTypes</code> returns strings for supported resource types</p>"""
    message_category: NotRequired["capo_backup.types.message_category.MessageCategory"]
    """<p>This parameter is the job count for the specified message category.</p> <p>Example strings include <code>AccessDenied</code>, <code>Success</code>, and <code>InvalidParameters</code>. See <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> for a list of MessageCategory strings.</p> <p>The the value ANY returns count of all message categories.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all message categories and returns the sum.</p>"""
    count: "capo_backup.types.integer.integer"
    """<p>The value as a number of jobs in a job summary.</p>"""
    start_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The value of time in number format of a job start time.</p> <p>This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    end_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The value of time in number format of a job end time.</p> <p>This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobSummary) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "state" in value:
        import capo_backup.types.copy_job_status

        out["State"] = capo_backup.types.copy_job_status.serialize_json(value["state"])
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "message_category" in value:
        out["MessageCategory"] = value["message_category"]
    out["Count"] = value.get("count", 0)
    if "start_time" in value:
        import capo_backup.types.timestamp

        out["StartTime"] = capo_backup.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_backup.types.timestamp

        out["EndTime"] = capo_backup.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> CopyJobSummary:
    out: CopyJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("State") is not None:
        import capo_backup.types.copy_job_status

        out["state"] = capo_backup.types.copy_job_status.deserialize_json(data["State"])
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("MessageCategory") is not None:
        out["message_category"] = data["MessageCategory"]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if data.get("StartTime") is not None:
        import capo_backup.types.timestamp

        out["start_time"] = capo_backup.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_backup.types.timestamp

        out["end_time"] = capo_backup.types.timestamp.deserialize_json(data["EndTime"])
    return out

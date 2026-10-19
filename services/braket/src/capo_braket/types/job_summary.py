"""Generated from Smithy shape ``com.amazonaws.braket#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_braket.types.job_arn
    import capo_braket.types.job_primary_status
    import capo_braket.types.string256
    import capo_braket.types.tags_map


class JobSummary(TypedDict, closed=True):
    status: "capo_braket.types.job_primary_status.JobPrimaryStatus"
    """<p>The status of the Amazon Braket hybrid job.</p>"""
    job_arn: "capo_braket.types.job_arn.JobArn"
    """<p>The ARN of the Amazon Braket hybrid job.</p>"""
    job_name: "str"
    """<p>The name of the Amazon Braket hybrid job.</p>"""
    device: "capo_braket.types.string256.String256"
    """<p>The primary device used by an Amazon Braket hybrid job.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the Amazon Braket hybrid job was created.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job was started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job ended.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>Displays the key, value pairs of tags associated with this hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    out["device"] = value["device"]
    import capo_braket._protocol.serialize

    out["createdAt"] = capo_braket._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "started_at" in value:
        import capo_braket._protocol.serialize

        out["startedAt"] = capo_braket._protocol.serialize.fmt_date_time(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_braket._protocol.serialize

        out["endedAt"] = capo_braket._protocol.serialize.fmt_date_time(
            value["ended_at"]
        )
    if "tags" in value:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("device") is not None:
        out["device"] = data["device"]
    else:
        out["device"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("startedAt") is not None:
        import datetime

        out["started_at"] = datetime.datetime.fromisoformat(
            data["startedAt"].replace("Z", "+00:00")
        )
    if data.get("endedAt") is not None:
        import datetime

        out["ended_at"] = datetime.datetime.fromisoformat(
            data["endedAt"].replace("Z", "+00:00")
        )
    if data.get("tags") is not None:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    return out

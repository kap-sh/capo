"""Generated from Smithy shape ``com.amazonaws.mgn#Job``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.initiated_by
    import capo_mgn.types.iso8601_datetime_string
    import capo_mgn.types.job_id
    import capo_mgn.types.job_status
    import capo_mgn.types.job_type
    import capo_mgn.types.participating_servers
    import capo_mgn.types.tags_map


class Job(TypedDict, closed=True):
    job_id: "capo_mgn.types.job_id.JobID"
    """<p>Job ID.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>the ARN of the specific Job.</p>"""
    type: NotRequired["capo_mgn.types.job_type.JobType"]
    """<p>Job type.</p>"""
    initiated_by: NotRequired["capo_mgn.types.initiated_by.InitiatedBy"]
    """<p>Job initiated by field.</p>"""
    creation_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Job creation time.</p>"""
    end_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Job end time.</p>"""
    status: NotRequired["capo_mgn.types.job_status.JobStatus"]
    """<p>Job status.</p>"""
    participating_servers: NotRequired[
        "capo_mgn.types.participating_servers.ParticipatingServers"
    ]
    """<p>Servers participating in a specific Job.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags associated with specific Job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        out["type"] = value["type"]
    if "initiated_by" in value:
        out["initiatedBy"] = value["initiated_by"]
    if "creation_date_time" in value:
        out["creationDateTime"] = value["creation_date_time"]
    if "end_date_time" in value:
        out["endDateTime"] = value["end_date_time"]
    if "status" in value:
        out["status"] = value["status"]
    if "participating_servers" in value:
        import capo_mgn.types.participating_servers

        out["participatingServers"] = (
            capo_mgn.types.participating_servers.serialize_json(
                value["participating_servers"]
            )
        )
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    else:
        out["job_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("initiatedBy") is not None:
        out["initiated_by"] = data["initiatedBy"]
    if data.get("creationDateTime") is not None:
        out["creation_date_time"] = data["creationDateTime"]
    if data.get("endDateTime") is not None:
        out["end_date_time"] = data["endDateTime"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("participatingServers") is not None:
        import capo_mgn.types.participating_servers

        out["participating_servers"] = (
            capo_mgn.types.participating_servers.deserialize_json(
                data["participatingServers"]
            )
        )
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: Job) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out

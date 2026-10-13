"""Generated from Smithy shape ``com.amazonaws.drs#Job``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.arn
    import capo_drs.types.initiated_by
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.job_id
    import capo_drs.types.job_status
    import capo_drs.types.job_type
    import capo_drs.types.participating_resources
    import capo_drs.types.participating_servers
    import capo_drs.types.tags_map


class Job(TypedDict, closed=True):
    job_id: "capo_drs.types.job_id.JobID"
    """<p>The ID of the Job.</p>"""
    arn: NotRequired["capo_drs.types.arn.ARN"]
    """<p>The ARN of a Job.</p>"""
    type: NotRequired["capo_drs.types.job_type.JobType"]
    """<p>The type of the Job.</p>"""
    initiated_by: NotRequired["capo_drs.types.initiated_by.InitiatedBy"]
    """<p>A string representing who initiated the Job.</p>"""
    creation_date_time: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time of when the Job was created.</p>"""
    end_date_time: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time of when the Job ended.</p>"""
    status: NotRequired["capo_drs.types.job_status.JobStatus"]
    """<p>The status of the Job.</p>"""
    participating_servers: NotRequired[
        "capo_drs.types.participating_servers.ParticipatingServers"
    ]
    """<p>A list of servers that the Job is acting upon.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>A list of tags associated with the Job.</p>"""
    participating_resources: NotRequired[
        "capo_drs.types.participating_resources.ParticipatingResources"
    ]
    """<p>A list of resources that the Job is acting upon.</p>"""


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
        import capo_drs.types.participating_servers

        out["participatingServers"] = (
            capo_drs.types.participating_servers.serialize_json(
                value["participating_servers"]
            )
        )
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    if "participating_resources" in value:
        import capo_drs.types.participating_resources

        out["participatingResources"] = (
            capo_drs.types.participating_resources.serialize_json(
                value["participating_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    else:
        raise DeserializationError("Job.job_id required")
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
        import capo_drs.types.participating_servers

        out["participating_servers"] = (
            capo_drs.types.participating_servers.deserialize_json(
                data["participatingServers"]
            )
        )
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    if data.get("participatingResources") is not None:
        import capo_drs.types.participating_resources

        out["participating_resources"] = (
            capo_drs.types.participating_resources.deserialize_json(
                data["participatingResources"]
            )
        )
    return out


def redact_sensitive(value: Job) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out

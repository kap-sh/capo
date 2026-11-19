"""Generated from Smithy shape ``com.amazonaws.snowball#JobListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.boolean
    import capo_snowball.types.job_state
    import capo_snowball.types.job_type
    import capo_snowball.types.snowball_type
    import capo_snowball.types.string
    import capo_snowball.types.timestamp


class JobListEntry(TypedDict, closed=True):
    job_id: NotRequired["capo_snowball.types.string.String"]
    """<p>The automatically generated ID for a job, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    job_state: NotRequired["capo_snowball.types.job_state.JobState"]
    """<p>The current state of this job.</p>"""
    is_master: "capo_snowball.types.boolean.Boolean"
    """<p>A value that indicates that this job is a main job. A main job represents a successful request to create an export job. Main jobs aren't associated with any Snowballs. Instead, each main job will have at least one job part, and each job part is associated with a Snowball. It might take some time before the job parts associated with a particular main job are listed, because they are created after the main job is created.</p>"""
    job_type: NotRequired["capo_snowball.types.job_type.JobType"]
    """<p>The type of job.</p>"""
    snowball_type: NotRequired["capo_snowball.types.snowball_type.SnowballType"]
    """<p>The type of device used with this job.</p>"""
    creation_date: NotRequired["capo_snowball.types.timestamp.Timestamp"]
    """<p>The creation date for this job.</p>"""
    description: NotRequired["capo_snowball.types.string.String"]
    """<p>The optional description of this specific job, for example <code>Important Photos 2016-08-11</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobListEntry) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_state" in value:
        import capo_snowball.types.job_state

        out["JobState"] = capo_snowball.types.job_state.serialize_aws_json_1_1(
            value["job_state"]
        )
    out["IsMaster"] = value.get("is_master", False)
    if "job_type" in value:
        import capo_snowball.types.job_type

        out["JobType"] = capo_snowball.types.job_type.serialize_aws_json_1_1(
            value["job_type"]
        )
    if "snowball_type" in value:
        import capo_snowball.types.snowball_type

        out["SnowballType"] = capo_snowball.types.snowball_type.serialize_aws_json_1_1(
            value["snowball_type"]
        )
    if "creation_date" in value:
        import capo_snowball.types.timestamp

        out["CreationDate"] = capo_snowball.types.timestamp.serialize_aws_json_1_1(
            value["creation_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobListEntry:
    out: JobListEntry = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobState") is not None:
        import capo_snowball.types.job_state

        out["job_state"] = capo_snowball.types.job_state.deserialize_aws_json_1_1(
            data["JobState"]
        )
    if data.get("IsMaster") is not None:
        out["is_master"] = data["IsMaster"]
    else:
        out["is_master"] = False
    if data.get("JobType") is not None:
        import capo_snowball.types.job_type

        out["job_type"] = capo_snowball.types.job_type.deserialize_aws_json_1_1(
            data["JobType"]
        )
    if data.get("SnowballType") is not None:
        import capo_snowball.types.snowball_type

        out["snowball_type"] = (
            capo_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    if data.get("CreationDate") is not None:
        import capo_snowball.types.timestamp

        out["creation_date"] = capo_snowball.types.timestamp.deserialize_aws_json_1_1(
            data["CreationDate"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JobListEntry) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_state" in value:
        import capo_snowball.types.job_state

        out["JobState"] = capo_snowball.types.job_state.serialize_cbor(
            value["job_state"]
        )
    out["IsMaster"] = value.get("is_master", False)
    if "job_type" in value:
        import capo_snowball.types.job_type

        out["JobType"] = capo_snowball.types.job_type.serialize_cbor(value["job_type"])
    if "snowball_type" in value:
        import capo_snowball.types.snowball_type

        out["SnowballType"] = capo_snowball.types.snowball_type.serialize_cbor(
            value["snowball_type"]
        )
    if "creation_date" in value:
        import capo_snowball.types.timestamp

        out["CreationDate"] = capo_snowball.types.timestamp.serialize_cbor(
            value["creation_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> JobListEntry:
    out: JobListEntry = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobState") is not None:
        import capo_snowball.types.job_state

        out["job_state"] = capo_snowball.types.job_state.deserialize_cbor(
            data["JobState"]
        )
    if data.get("IsMaster") is not None:
        out["is_master"] = data["IsMaster"]
    else:
        out["is_master"] = False
    if data.get("JobType") is not None:
        import capo_snowball.types.job_type

        out["job_type"] = capo_snowball.types.job_type.deserialize_cbor(data["JobType"])
    if data.get("SnowballType") is not None:
        import capo_snowball.types.snowball_type

        out["snowball_type"] = capo_snowball.types.snowball_type.deserialize_cbor(
            data["SnowballType"]
        )
    if data.get("CreationDate") is not None:
        import capo_snowball.types.timestamp

        out["creation_date"] = capo_snowball.types.timestamp.deserialize_cbor(
            data["CreationDate"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#CopyJobTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.s3_location


class CopyJobTemplateRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID to copy."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID to copy."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID to copy."""
    target_s3_location: "capo_deadline.types.s3_location.S3Location"
    """The Amazon S3 bucket name and key where you would like to add a copy of the job template."""


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobTemplateRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.s3_location

    out["targetS3Location"] = capo_deadline.types.s3_location.serialize_json(
        value["target_s3_location"]
    )
    return out


def deserialize_json(data: dict) -> CopyJobTemplateRequest:
    out: CopyJobTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("targetS3Location") is not None:
        import capo_deadline.types.s3_location

        out["target_s3_location"] = capo_deadline.types.s3_location.deserialize_json(
            data["targetS3Location"]
        )
    else:
        raise DeserializationError("CopyJobTemplateRequest.target_s3_location required")
    return out

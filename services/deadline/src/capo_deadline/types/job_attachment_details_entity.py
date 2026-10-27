"""Generated from Smithy shape ``com.amazonaws.deadline#JobAttachmentDetailsEntity``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.attachments
    import capo_deadline.types.job_id


class JobAttachmentDetailsEntity(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID."""
    attachments: "capo_deadline.types.attachments.Attachments"
    """The job attachments."""


# --- restJson1 ser/de ---
def serialize_json(value: JobAttachmentDetailsEntity) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_deadline.types.attachments

    out["attachments"] = capo_deadline.types.attachments.serialize_json(
        value["attachments"]
    )
    return out


def deserialize_json(data: dict) -> JobAttachmentDetailsEntity:
    out: JobAttachmentDetailsEntity = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("attachments") is not None:
        import capo_deadline.types.attachments

        out["attachments"] = capo_deadline.types.attachments.deserialize_json(
            data["attachments"]
        )
    else:
        raise DeserializationError("JobAttachmentDetailsEntity.attachments required")
    return out


def redact_sensitive(value: JobAttachmentDetailsEntity) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attachments" in value:
        import capo_deadline.types.attachments

        out["attachments"] = capo_deadline.types.attachments.redact_sensitive(
            value["attachments"]
        )
    return out

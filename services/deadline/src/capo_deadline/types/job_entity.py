"""Generated from Smithy shape ``com.amazonaws.deadline#JobEntity``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.environment_details_entity
    import capo_deadline.types.job_attachment_details_entity
    import capo_deadline.types.job_details_entity
    import capo_deadline.types.step_details_entity


class _JobEntity_jobDetails(TypedDict, closed=True):
    jobDetails: "capo_deadline.types.job_details_entity.JobDetailsEntity"


class _JobEntity_jobAttachmentDetails(TypedDict, closed=True):
    jobAttachmentDetails: (
        "capo_deadline.types.job_attachment_details_entity.JobAttachmentDetailsEntity"
    )


class _JobEntity_stepDetails(TypedDict, closed=True):
    stepDetails: "capo_deadline.types.step_details_entity.StepDetailsEntity"


class _JobEntity_environmentDetails(TypedDict, closed=True):
    environmentDetails: (
        "capo_deadline.types.environment_details_entity.EnvironmentDetailsEntity"
    )


JobEntity: TypeAlias = (
    _JobEntity_jobDetails
    | _JobEntity_jobAttachmentDetails
    | _JobEntity_stepDetails
    | _JobEntity_environmentDetails
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: JobEntity) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"JobEntity: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "jobDetails" in value:
        import capo_deadline.types.job_details_entity

        return {
            "jobDetails": capo_deadline.types.job_details_entity.serialize_json(
                value["jobDetails"]
            )
        }
    elif "jobAttachmentDetails" in value:
        import capo_deadline.types.job_attachment_details_entity

        return {
            "jobAttachmentDetails": capo_deadline.types.job_attachment_details_entity.serialize_json(
                value["jobAttachmentDetails"]
            )
        }
    elif "stepDetails" in value:
        import capo_deadline.types.step_details_entity

        return {
            "stepDetails": capo_deadline.types.step_details_entity.serialize_json(
                value["stepDetails"]
            )
        }
    elif "environmentDetails" in value:
        import capo_deadline.types.environment_details_entity

        return {
            "environmentDetails": capo_deadline.types.environment_details_entity.serialize_json(
                value["environmentDetails"]
            )
        }
    else:
        raise SerializationError("JobEntity: no variant present")


def deserialize_json(data: dict) -> JobEntity:
    if data.get("jobDetails") is not None:
        import capo_deadline.types.job_details_entity

        return {
            "jobDetails": capo_deadline.types.job_details_entity.deserialize_json(
                data["jobDetails"]
            )
        }
    elif data.get("jobAttachmentDetails") is not None:
        import capo_deadline.types.job_attachment_details_entity

        return {
            "jobAttachmentDetails": capo_deadline.types.job_attachment_details_entity.deserialize_json(
                data["jobAttachmentDetails"]
            )
        }
    elif data.get("stepDetails") is not None:
        import capo_deadline.types.step_details_entity

        return {
            "stepDetails": capo_deadline.types.step_details_entity.deserialize_json(
                data["stepDetails"]
            )
        }
    elif data.get("environmentDetails") is not None:
        import capo_deadline.types.environment_details_entity

        return {
            "environmentDetails": capo_deadline.types.environment_details_entity.deserialize_json(
                data["environmentDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("JobEntity: no recognized variant key")


def redact_sensitive(value: JobEntity) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "jobDetails" in value:
        import capo_deadline.types.job_details_entity

        out["jobDetails"] = capo_deadline.types.job_details_entity.redact_sensitive(
            value["jobDetails"]
        )
    if "jobAttachmentDetails" in value:
        import capo_deadline.types.job_attachment_details_entity

        out["jobAttachmentDetails"] = (
            capo_deadline.types.job_attachment_details_entity.redact_sensitive(
                value["jobAttachmentDetails"]
            )
        )
    if "stepDetails" in value:
        import capo_deadline.types.step_details_entity

        out["stepDetails"] = capo_deadline.types.step_details_entity.redact_sensitive(
            value["stepDetails"]
        )
    if "environmentDetails" in value:
        import capo_deadline.types.environment_details_entity

        out["environmentDetails"] = (
            capo_deadline.types.environment_details_entity.redact_sensitive(
                value["environmentDetails"]
            )
        )
    return out

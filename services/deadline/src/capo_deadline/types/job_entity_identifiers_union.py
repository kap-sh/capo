"""Generated from Smithy shape ``com.amazonaws.deadline#JobEntityIdentifiersUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.environment_details_identifiers
    import capo_deadline.types.job_attachment_details_identifiers
    import capo_deadline.types.job_details_identifiers
    import capo_deadline.types.step_details_identifiers


class _JobEntityIdentifiersUnion_jobDetails(TypedDict, closed=True):
    jobDetails: "capo_deadline.types.job_details_identifiers.JobDetailsIdentifiers"


class _JobEntityIdentifiersUnion_jobAttachmentDetails(TypedDict, closed=True):
    jobAttachmentDetails: "capo_deadline.types.job_attachment_details_identifiers.JobAttachmentDetailsIdentifiers"


class _JobEntityIdentifiersUnion_stepDetails(TypedDict, closed=True):
    stepDetails: "capo_deadline.types.step_details_identifiers.StepDetailsIdentifiers"


class _JobEntityIdentifiersUnion_environmentDetails(TypedDict, closed=True):
    environmentDetails: "capo_deadline.types.environment_details_identifiers.EnvironmentDetailsIdentifiers"


JobEntityIdentifiersUnion: TypeAlias = (
    _JobEntityIdentifiersUnion_jobDetails
    | _JobEntityIdentifiersUnion_jobAttachmentDetails
    | _JobEntityIdentifiersUnion_stepDetails
    | _JobEntityIdentifiersUnion_environmentDetails
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: JobEntityIdentifiersUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"JobEntityIdentifiersUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "jobDetails" in value:
        import capo_deadline.types.job_details_identifiers

        return {
            "jobDetails": capo_deadline.types.job_details_identifiers.serialize_json(
                value["jobDetails"]
            )
        }
    elif "jobAttachmentDetails" in value:
        import capo_deadline.types.job_attachment_details_identifiers

        return {
            "jobAttachmentDetails": capo_deadline.types.job_attachment_details_identifiers.serialize_json(
                value["jobAttachmentDetails"]
            )
        }
    elif "stepDetails" in value:
        import capo_deadline.types.step_details_identifiers

        return {
            "stepDetails": capo_deadline.types.step_details_identifiers.serialize_json(
                value["stepDetails"]
            )
        }
    elif "environmentDetails" in value:
        import capo_deadline.types.environment_details_identifiers

        return {
            "environmentDetails": capo_deadline.types.environment_details_identifiers.serialize_json(
                value["environmentDetails"]
            )
        }
    else:
        raise SerializationError("JobEntityIdentifiersUnion: no variant present")


def deserialize_json(data: dict) -> JobEntityIdentifiersUnion:
    if data.get("jobDetails") is not None:
        import capo_deadline.types.job_details_identifiers

        return {
            "jobDetails": capo_deadline.types.job_details_identifiers.deserialize_json(
                data["jobDetails"]
            )
        }
    elif data.get("jobAttachmentDetails") is not None:
        import capo_deadline.types.job_attachment_details_identifiers

        return {
            "jobAttachmentDetails": capo_deadline.types.job_attachment_details_identifiers.deserialize_json(
                data["jobAttachmentDetails"]
            )
        }
    elif data.get("stepDetails") is not None:
        import capo_deadline.types.step_details_identifiers

        return {
            "stepDetails": capo_deadline.types.step_details_identifiers.deserialize_json(
                data["stepDetails"]
            )
        }
    elif data.get("environmentDetails") is not None:
        import capo_deadline.types.environment_details_identifiers

        return {
            "environmentDetails": capo_deadline.types.environment_details_identifiers.deserialize_json(
                data["environmentDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "JobEntityIdentifiersUnion: no recognized variant key"
        )

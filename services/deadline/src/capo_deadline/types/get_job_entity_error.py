"""Generated from Smithy shape ``com.amazonaws.deadline#GetJobEntityError``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.environment_details_error
    import capo_deadline.types.job_attachment_details_error
    import capo_deadline.types.job_details_error
    import capo_deadline.types.step_details_error


class _GetJobEntityError_jobDetails(TypedDict, closed=True):
    jobDetails: "capo_deadline.types.job_details_error.JobDetailsError"


class _GetJobEntityError_jobAttachmentDetails(TypedDict, closed=True):
    jobAttachmentDetails: (
        "capo_deadline.types.job_attachment_details_error.JobAttachmentDetailsError"
    )


class _GetJobEntityError_stepDetails(TypedDict, closed=True):
    stepDetails: "capo_deadline.types.step_details_error.StepDetailsError"


class _GetJobEntityError_environmentDetails(TypedDict, closed=True):
    environmentDetails: (
        "capo_deadline.types.environment_details_error.EnvironmentDetailsError"
    )


GetJobEntityError: TypeAlias = (
    _GetJobEntityError_jobDetails
    | _GetJobEntityError_jobAttachmentDetails
    | _GetJobEntityError_stepDetails
    | _GetJobEntityError_environmentDetails
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GetJobEntityError) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"GetJobEntityError: cannot serialize unknown variant {value.name!r}"
        )
    elif "jobDetails" in value:
        import capo_deadline.types.job_details_error

        return {
            "jobDetails": capo_deadline.types.job_details_error.serialize_json(
                value["jobDetails"]
            )
        }
    elif "jobAttachmentDetails" in value:
        import capo_deadline.types.job_attachment_details_error

        return {
            "jobAttachmentDetails": capo_deadline.types.job_attachment_details_error.serialize_json(
                value["jobAttachmentDetails"]
            )
        }
    elif "stepDetails" in value:
        import capo_deadline.types.step_details_error

        return {
            "stepDetails": capo_deadline.types.step_details_error.serialize_json(
                value["stepDetails"]
            )
        }
    elif "environmentDetails" in value:
        import capo_deadline.types.environment_details_error

        return {
            "environmentDetails": capo_deadline.types.environment_details_error.serialize_json(
                value["environmentDetails"]
            )
        }
    else:
        raise SerializationError("GetJobEntityError: no variant present")


def deserialize_json(data: dict) -> GetJobEntityError:
    if data.get("jobDetails") is not None:
        import capo_deadline.types.job_details_error

        return {
            "jobDetails": capo_deadline.types.job_details_error.deserialize_json(
                data["jobDetails"]
            )
        }
    elif data.get("jobAttachmentDetails") is not None:
        import capo_deadline.types.job_attachment_details_error

        return {
            "jobAttachmentDetails": capo_deadline.types.job_attachment_details_error.deserialize_json(
                data["jobAttachmentDetails"]
            )
        }
    elif data.get("stepDetails") is not None:
        import capo_deadline.types.step_details_error

        return {
            "stepDetails": capo_deadline.types.step_details_error.deserialize_json(
                data["stepDetails"]
            )
        }
    elif data.get("environmentDetails") is not None:
        import capo_deadline.types.environment_details_error

        return {
            "environmentDetails": capo_deadline.types.environment_details_error.deserialize_json(
                data["environmentDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("GetJobEntityError: no recognized variant key")

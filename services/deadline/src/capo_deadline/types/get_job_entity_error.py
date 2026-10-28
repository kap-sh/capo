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


class GetJobEntityErrorJobDetailsMember(TypedDict, closed=True):
    jobDetails: "capo_deadline.types.job_details_error.JobDetailsError"


class GetJobEntityErrorJobAttachmentDetailsMember(TypedDict, closed=True):
    jobAttachmentDetails: (
        "capo_deadline.types.job_attachment_details_error.JobAttachmentDetailsError"
    )


class GetJobEntityErrorStepDetailsMember(TypedDict, closed=True):
    stepDetails: "capo_deadline.types.step_details_error.StepDetailsError"


class GetJobEntityErrorEnvironmentDetailsMember(TypedDict, closed=True):
    environmentDetails: (
        "capo_deadline.types.environment_details_error.EnvironmentDetailsError"
    )


GetJobEntityError: TypeAlias = (
    GetJobEntityErrorJobDetailsMember
    | GetJobEntityErrorJobAttachmentDetailsMember
    | GetJobEntityErrorStepDetailsMember
    | GetJobEntityErrorEnvironmentDetailsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GetJobEntityError) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GetJobEntityError: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("GetJobEntityError: no recognized variant key")

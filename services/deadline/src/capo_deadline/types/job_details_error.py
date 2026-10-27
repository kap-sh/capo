"""Generated from Smithy shape ``com.amazonaws.deadline#JobDetailsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.job_entity_error_code
    import capo_deadline.types.job_id
    import capo_deadline.types.string


class JobDetailsError(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID."""
    code: "capo_deadline.types.job_entity_error_code.JobEntityErrorCode"
    """The error code."""
    message: "capo_deadline.types.string.String"
    """The error message detailing the error's cause."""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetailsError) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_deadline.types.job_entity_error_code

    out["code"] = capo_deadline.types.job_entity_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> JobDetailsError:
    out: JobDetailsError = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("code") is not None:
        import capo_deadline.types.job_entity_error_code

        out["code"] = capo_deadline.types.job_entity_error_code.deserialize_json(
            data["code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_deadline.types.job_entity_error_code.JobEntityErrorCode", ""
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out

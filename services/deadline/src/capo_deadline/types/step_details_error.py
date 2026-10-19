"""Generated from Smithy shape ``com.amazonaws.deadline#StepDetailsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.job_entity_error_code
    import capo_deadline.types.job_id
    import capo_deadline.types.step_id
    import capo_deadline.types.string


class StepDetailsError(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    code: "capo_deadline.types.job_entity_error_code.JobEntityErrorCode"
    """<p>The error code.</p>"""
    message: "capo_deadline.types.string.String"
    """<p>The error message detailing the error's cause.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepDetailsError) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    import capo_deadline.types.job_entity_error_code

    out["code"] = capo_deadline.types.job_entity_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StepDetailsError:
    out: StepDetailsError = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    else:
        out["step_id"] = ""
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

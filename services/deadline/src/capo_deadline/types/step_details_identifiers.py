"""Generated from Smithy shape ``com.amazonaws.deadline#StepDetailsIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.job_id
    import capo_deadline.types.step_id


class StepDetailsIdentifiers(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepDetailsIdentifiers) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    return out


def deserialize_json(data: dict) -> StepDetailsIdentifiers:
    out: StepDetailsIdentifiers = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    else:
        out["step_id"] = ""
    return out

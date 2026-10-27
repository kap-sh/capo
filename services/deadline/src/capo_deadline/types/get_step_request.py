"""Generated from Smithy shape ``com.amazonaws.deadline#GetStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.step_id


class GetStepRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID for the step."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID for the step."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID for the step."""
    step_id: "capo_deadline.types.step_id.StepId"
    """The step ID."""


# --- restJson1 ser/de ---
def serialize_json(value: GetStepRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStepRequest:
    out: GetStepRequest = {}  # type: ignore[typeddict-item]
    return out

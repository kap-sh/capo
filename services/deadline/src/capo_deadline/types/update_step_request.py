"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.step_id
    import capo_deadline.types.step_target_task_run_status


class UpdateStepRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID to update."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID to update."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID to update."""
    step_id: "capo_deadline.types.step_id.StepId"
    """The step ID to update."""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The unique token which the server uses to recognize retries of the same request."""
    target_task_run_status: (
        "capo_deadline.types.step_target_task_run_status.StepTargetTaskRunStatus"
    )
    """The task status to update the step's tasks to."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStepRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.step_target_task_run_status

    out["targetTaskRunStatus"] = (
        capo_deadline.types.step_target_task_run_status.serialize_json(
            value["target_task_run_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateStepRequest:
    out: UpdateStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("targetTaskRunStatus") is not None:
        import capo_deadline.types.step_target_task_run_status

        out["target_task_run_status"] = (
            capo_deadline.types.step_target_task_run_status.deserialize_json(
                data["targetTaskRunStatus"]
            )
        )
    else:
        import typing

        out["target_task_run_status"] = typing.cast(
            "capo_deadline.types.step_target_task_run_status.StepTargetTaskRunStatus",
            "",
        )
    return out

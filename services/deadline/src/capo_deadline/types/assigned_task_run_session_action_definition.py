"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedTaskRunSessionActionDefinition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.step_id
    import capo_deadline.types.task_id
    import capo_deadline.types.task_parameters


class AssignedTaskRunSessionActionDefinition(TypedDict, closed=True):
    task_id: NotRequired["capo_deadline.types.task_id.TaskId"]
    """<p>The task ID.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    parameters: "capo_deadline.types.task_parameters.TaskParameters"
    """<p>The parameters to include.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssignedTaskRunSessionActionDefinition) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    out["stepId"] = value["step_id"]
    import capo_deadline.types.task_parameters

    out["parameters"] = capo_deadline.types.task_parameters.serialize_json(
        value["parameters"]
    )
    return out


def deserialize_json(data: dict) -> AssignedTaskRunSessionActionDefinition:
    out: AssignedTaskRunSessionActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError(
            "AssignedTaskRunSessionActionDefinition.step_id required"
        )
    if data.get("parameters") is not None:
        import capo_deadline.types.task_parameters

        out["parameters"] = capo_deadline.types.task_parameters.deserialize_json(
            data["parameters"]
        )
    else:
        raise DeserializationError(
            "AssignedTaskRunSessionActionDefinition.parameters required"
        )
    return out


def redact_sensitive(value: AssignedTaskRunSessionActionDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    return out

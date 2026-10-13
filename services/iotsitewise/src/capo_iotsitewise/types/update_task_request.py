"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateTaskRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.task_configuration
    import capo_iotsitewise.types.workspace_name


class UpdateTaskRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    task_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the task to update.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A new description for the task.</p>"""
    task_configuration: NotRequired[
        "capo_iotsitewise.types.task_configuration.TaskConfiguration"
    ]
    """<p>The updated task execution configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTaskRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "task_configuration" in value:
        import capo_iotsitewise.types.task_configuration

        out["taskConfiguration"] = (
            capo_iotsitewise.types.task_configuration.serialize_json(
                value["task_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTaskRequest:
    out: UpdateTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("taskConfiguration") is not None:
        import capo_iotsitewise.types.task_configuration

        out["task_configuration"] = (
            capo_iotsitewise.types.task_configuration.deserialize_json(
                data["taskConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateTaskRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "task_configuration" in value:
        import capo_iotsitewise.types.task_configuration

        out["task_configuration"] = (
            capo_iotsitewise.types.task_configuration.redact_sensitive(
                value["task_configuration"]
            )
        )
    return out

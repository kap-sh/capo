"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateBacklogTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.backlog_task_description
    import capo_devops_agent.types.backlog_task_title
    import capo_devops_agent.types.priority
    import capo_devops_agent.types.reference_input
    import capo_devops_agent.types.task_type


class CreateBacklogTaskRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space where the task will be created</p>"""
    reference: NotRequired["capo_devops_agent.types.reference_input.ReferenceInput"]
    """<p>Optional reference information for the task</p>"""
    task_type: "capo_devops_agent.types.task_type.TaskType"
    """<p>The type of task being created</p>"""
    title: "capo_devops_agent.types.backlog_task_title.BacklogTaskTitle"
    """<p>The title of the backlog task</p>"""
    description: NotRequired[
        "capo_devops_agent.types.backlog_task_description.BacklogTaskDescription"
    ]
    """<p>Optional detailed description of the task</p>"""
    priority: "capo_devops_agent.types.priority.Priority"
    """<p>The priority level of the task</p>"""
    client_token: NotRequired["str"]
    """<p>Client-provided token for idempotent operations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBacklogTaskRequest) -> dict:
    out: dict = {}
    if "reference" in value:
        import capo_devops_agent.types.reference_input

        out["reference"] = capo_devops_agent.types.reference_input.serialize_json(
            value["reference"]
        )
    import capo_devops_agent.types.task_type

    out["taskType"] = capo_devops_agent.types.task_type.serialize_json(
        value["task_type"]
    )
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_devops_agent.types.priority

    out["priority"] = capo_devops_agent.types.priority.serialize_json(value["priority"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateBacklogTaskRequest:
    out: CreateBacklogTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("reference") is not None:
        import capo_devops_agent.types.reference_input

        out["reference"] = capo_devops_agent.types.reference_input.deserialize_json(
            data["reference"]
        )
    if data.get("taskType") is not None:
        import capo_devops_agent.types.task_type

        out["task_type"] = capo_devops_agent.types.task_type.deserialize_json(
            data["taskType"]
        )
    else:
        import typing

        out["task_type"] = typing.cast("capo_devops_agent.types.task_type.TaskType", "")
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("priority") is not None:
        import capo_devops_agent.types.priority

        out["priority"] = capo_devops_agent.types.priority.deserialize_json(
            data["priority"]
        )
    else:
        import typing

        out["priority"] = typing.cast("capo_devops_agent.types.priority.Priority", "")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

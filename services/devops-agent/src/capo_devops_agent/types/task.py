"""Generated from Smithy shape ``com.amazonaws.devopsagent#Task``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.back_log_timestamp
    import capo_devops_agent.types.priority
    import capo_devops_agent.types.reference_output
    import capo_devops_agent.types.task_status
    import capo_devops_agent.types.task_type


class Task(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier for the agent space containing this task</p>"""
    task_id: "str"
    """<p>The unique identifier for this task</p>"""
    execution_id: NotRequired["str"]
    """<p>The execution ID associated with this task, if any</p>"""
    title: "str"
    """<p>The title of the task</p>"""
    description: NotRequired["str"]
    """<p>Optional detailed description of the task</p>"""
    reference: NotRequired["capo_devops_agent.types.reference_output.ReferenceOutput"]
    """<p>Optional reference information linking this task to external systems</p>"""
    task_type: "capo_devops_agent.types.task_type.TaskType"
    """<p>The type of this task</p>"""
    priority: "capo_devops_agent.types.priority.Priority"
    """<p>The priority level of this task</p>"""
    status: "capo_devops_agent.types.task_status.TaskStatus"
    """<p>The current status of this task</p>"""
    created_at: "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this task was created</p>"""
    updated_at: "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this task was last updated</p>"""
    version: "int"
    """<p>Version number for optimistic locking</p>"""
    support_metadata: NotRequired["object"]
    """<p>Optional support metadata for the task</p>"""
    metadata: NotRequired["object"]
    """<p>Optional metadata for the task</p>"""
    primary_task_id: NotRequired["str"]
    """<p>The task ID of the primary investigation this task is linked to</p>"""
    status_reason: NotRequired["str"]
    """<p>Explanation for why the task status was changed (e.g., linked reason)</p>"""
    has_linked_tasks: "bool"
    """<p>Indicates if this task has other tasks linked to it</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Task) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["taskId"] = value["task_id"]
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "reference" in value:
        import capo_devops_agent.types.reference_output

        out["reference"] = capo_devops_agent.types.reference_output.serialize_json(
            value["reference"]
        )
    import capo_devops_agent.types.task_type

    out["taskType"] = capo_devops_agent.types.task_type.serialize_json(
        value["task_type"]
    )
    import capo_devops_agent.types.priority

    out["priority"] = capo_devops_agent.types.priority.serialize_json(value["priority"])
    import capo_devops_agent.types.task_status

    out["status"] = capo_devops_agent.types.task_status.serialize_json(value["status"])
    import capo_devops_agent.types.back_log_timestamp

    out["createdAt"] = capo_devops_agent.types.back_log_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_devops_agent.types.back_log_timestamp

    out["updatedAt"] = capo_devops_agent.types.back_log_timestamp.serialize_json(
        value["updated_at"]
    )
    out["version"] = value["version"]
    if "support_metadata" in value:
        out["supportMetadata"] = value["support_metadata"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    if "primary_task_id" in value:
        out["primaryTaskId"] = value["primary_task_id"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["hasLinkedTasks"] = value.get("has_linked_tasks", False)
    return out


def deserialize_json(data: dict) -> Task:
    out: Task = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("reference") is not None:
        import capo_devops_agent.types.reference_output

        out["reference"] = capo_devops_agent.types.reference_output.deserialize_json(
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
    if data.get("priority") is not None:
        import capo_devops_agent.types.priority

        out["priority"] = capo_devops_agent.types.priority.deserialize_json(
            data["priority"]
        )
    else:
        import typing

        out["priority"] = typing.cast("capo_devops_agent.types.priority.Priority", "")
    if data.get("status") is not None:
        import capo_devops_agent.types.task_status

        out["status"] = capo_devops_agent.types.task_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_devops_agent.types.task_status.TaskStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_devops_agent.types.back_log_timestamp

        out["created_at"] = capo_devops_agent.types.back_log_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_devops_agent.types.back_log_timestamp

        out["updated_at"] = capo_devops_agent.types.back_log_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if data.get("supportMetadata") is not None:
        out["support_metadata"] = data["supportMetadata"]
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    if data.get("primaryTaskId") is not None:
        out["primary_task_id"] = data["primaryTaskId"]
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("hasLinkedTasks") is not None:
        out["has_linked_tasks"] = data["hasLinkedTasks"]
    else:
        out["has_linked_tasks"] = False
    return out

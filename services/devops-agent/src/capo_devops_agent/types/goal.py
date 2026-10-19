"""Generated from Smithy shape ``com.amazonaws.devopsagent#Goal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.back_log_timestamp
    import capo_devops_agent.types.goal_content
    import capo_devops_agent.types.goal_schedule
    import capo_devops_agent.types.goal_status
    import capo_devops_agent.types.goal_type


class Goal(TypedDict, closed=True):
    agent_space_arn: "str"
    """<p>The unique identifier for the agent space containing this goal</p>"""
    goal_id: "str"
    """<p>The unique identifier for this goal</p>"""
    title: "str"
    """<p>The title of the goal</p>"""
    content: "capo_devops_agent.types.goal_content.GoalContent"
    """<p>Content of the goal</p>"""
    status: "capo_devops_agent.types.goal_status.GoalStatus"
    """<p>Current status of the goal itself</p>"""
    goal_type: "capo_devops_agent.types.goal_type.GoalType"
    """<p>Type of goal based on its origin</p>"""
    created_at: "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this goal was created</p>"""
    updated_at: "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this goal was last updated</p>"""
    last_evaluated_at: NotRequired[
        "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    ]
    """<p>Timestamp when the goal was last evaluated</p>"""
    last_task_id: NotRequired["str"]
    """<p>ID of the most recent task associated with this goal</p>"""
    last_successful_task_id: NotRequired["str"]
    """<p>ID of the most recent successful task associated with this goal</p>"""
    version: "int"
    """<p>Version number for optimistic locking</p>"""
    evaluation_schedule: NotRequired[
        "capo_devops_agent.types.goal_schedule.GoalSchedule"
    ]
    """<p>Goal Schedule. Allows to schedule the goal to run periodically, as well as disable a goal temporarily</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Goal) -> dict:
    out: dict = {}
    out["agentSpaceArn"] = value["agent_space_arn"]
    out["goalId"] = value["goal_id"]
    out["title"] = value["title"]
    import capo_devops_agent.types.goal_content

    out["content"] = capo_devops_agent.types.goal_content.serialize_json(
        value["content"]
    )
    import capo_devops_agent.types.goal_status

    out["status"] = capo_devops_agent.types.goal_status.serialize_json(value["status"])
    import capo_devops_agent.types.goal_type

    out["goalType"] = capo_devops_agent.types.goal_type.serialize_json(
        value.get("goal_type", "ONCALL_REPORT")
    )
    import capo_devops_agent.types.back_log_timestamp

    out["createdAt"] = capo_devops_agent.types.back_log_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_devops_agent.types.back_log_timestamp

    out["updatedAt"] = capo_devops_agent.types.back_log_timestamp.serialize_json(
        value["updated_at"]
    )
    if "last_evaluated_at" in value:
        import capo_devops_agent.types.back_log_timestamp

        out["lastEvaluatedAt"] = (
            capo_devops_agent.types.back_log_timestamp.serialize_json(
                value["last_evaluated_at"]
            )
        )
    if "last_task_id" in value:
        out["lastTaskId"] = value["last_task_id"]
    if "last_successful_task_id" in value:
        out["lastSuccessfulTaskId"] = value["last_successful_task_id"]
    out["version"] = value["version"]
    if "evaluation_schedule" in value:
        import capo_devops_agent.types.goal_schedule

        out["evaluationSchedule"] = (
            capo_devops_agent.types.goal_schedule.serialize_json(
                value["evaluation_schedule"]
            )
        )
    return out


def deserialize_json(data: dict) -> Goal:
    out: Goal = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceArn") is not None:
        out["agent_space_arn"] = data["agentSpaceArn"]
    else:
        out["agent_space_arn"] = ""
    if data.get("goalId") is not None:
        out["goal_id"] = data["goalId"]
    else:
        out["goal_id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("content") is not None:
        import capo_devops_agent.types.goal_content

        out["content"] = capo_devops_agent.types.goal_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("Goal.content required")
    if data.get("status") is not None:
        import capo_devops_agent.types.goal_status

        out["status"] = capo_devops_agent.types.goal_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_devops_agent.types.goal_status.GoalStatus", ""
        )
    if data.get("goalType") is not None:
        import capo_devops_agent.types.goal_type

        out["goal_type"] = capo_devops_agent.types.goal_type.deserialize_json(
            data["goalType"]
        )
    else:
        out["goal_type"] = "ONCALL_REPORT"
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
    if data.get("lastEvaluatedAt") is not None:
        import capo_devops_agent.types.back_log_timestamp

        out["last_evaluated_at"] = (
            capo_devops_agent.types.back_log_timestamp.deserialize_json(
                data["lastEvaluatedAt"]
            )
        )
    if data.get("lastTaskId") is not None:
        out["last_task_id"] = data["lastTaskId"]
    if data.get("lastSuccessfulTaskId") is not None:
        out["last_successful_task_id"] = data["lastSuccessfulTaskId"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if data.get("evaluationSchedule") is not None:
        import capo_devops_agent.types.goal_schedule

        out["evaluation_schedule"] = (
            capo_devops_agent.types.goal_schedule.deserialize_json(
                data["evaluationSchedule"]
            )
        )
    return out

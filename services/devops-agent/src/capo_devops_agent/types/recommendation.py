"""Generated from Smithy shape ``com.amazonaws.devopsagent#Recommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.back_log_timestamp
    import capo_devops_agent.types.recommendation_content
    import capo_devops_agent.types.recommendation_priority
    import capo_devops_agent.types.recommendation_status


class Recommendation(TypedDict, closed=True):
    agent_space_arn: "str"
    """<p>ARN of the agent space this recommendation belongs to</p>"""
    recommendation_id: "str"
    """<p>The unique identifier for this recommendation</p>"""
    task_id: "str"
    """<p>ID of the task that generated the recommendation</p>"""
    goal_id: NotRequired["str"]
    """<p>ID of the goal this recommendation is associated with</p>"""
    title: "str"
    """<p>The title of the recommendation</p>"""
    content: "capo_devops_agent.types.recommendation_content.RecommendationContent"
    """<p>Content of the recommendation</p>"""
    status: "capo_devops_agent.types.recommendation_status.RecommendationStatus"
    """<p>Current status of the recommendation</p>"""
    priority: "capo_devops_agent.types.recommendation_priority.RecommendationPriority"
    """<p>Priority level of the recommendation</p>"""
    goal_version: NotRequired["int"]
    """<p>Version of the goal at the time this recommendation was generated</p>"""
    additional_context: NotRequired["str"]
    """<p>Additional context for recommendation</p>"""
    rank_position: NotRequired["int"]
    """<p>Position in ranked list (1 = highest priority)</p>"""
    ranked_at: NotRequired[
        "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    ]
    """<p>Timestamp when the recommendation was last ranked</p>"""
    created_at: "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this recommendation was created</p>"""
    updated_at: "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this recommendation was last updated</p>"""
    version: "int"
    """<p>Version number for optimistic locking</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    out["agentSpaceArn"] = value["agent_space_arn"]
    out["recommendationId"] = value["recommendation_id"]
    out["taskId"] = value["task_id"]
    if "goal_id" in value:
        out["goalId"] = value["goal_id"]
    out["title"] = value["title"]
    import capo_devops_agent.types.recommendation_content

    out["content"] = capo_devops_agent.types.recommendation_content.serialize_json(
        value["content"]
    )
    import capo_devops_agent.types.recommendation_status

    out["status"] = capo_devops_agent.types.recommendation_status.serialize_json(
        value["status"]
    )
    import capo_devops_agent.types.recommendation_priority

    out["priority"] = capo_devops_agent.types.recommendation_priority.serialize_json(
        value["priority"]
    )
    if "goal_version" in value:
        out["goalVersion"] = value["goal_version"]
    if "additional_context" in value:
        out["additionalContext"] = value["additional_context"]
    if "rank_position" in value:
        out["rankPosition"] = value["rank_position"]
    if "ranked_at" in value:
        import capo_devops_agent.types.back_log_timestamp

        out["rankedAt"] = capo_devops_agent.types.back_log_timestamp.serialize_json(
            value["ranked_at"]
        )
    import capo_devops_agent.types.back_log_timestamp

    out["createdAt"] = capo_devops_agent.types.back_log_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_devops_agent.types.back_log_timestamp

    out["updatedAt"] = capo_devops_agent.types.back_log_timestamp.serialize_json(
        value["updated_at"]
    )
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceArn") is not None:
        out["agent_space_arn"] = data["agentSpaceArn"]
    else:
        out["agent_space_arn"] = ""
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    else:
        out["recommendation_id"] = ""
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("goalId") is not None:
        out["goal_id"] = data["goalId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("content") is not None:
        import capo_devops_agent.types.recommendation_content

        out["content"] = (
            capo_devops_agent.types.recommendation_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("Recommendation.content required")
    if data.get("status") is not None:
        import capo_devops_agent.types.recommendation_status

        out["status"] = capo_devops_agent.types.recommendation_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_devops_agent.types.recommendation_status.RecommendationStatus", ""
        )
    if data.get("priority") is not None:
        import capo_devops_agent.types.recommendation_priority

        out["priority"] = (
            capo_devops_agent.types.recommendation_priority.deserialize_json(
                data["priority"]
            )
        )
    else:
        import typing

        out["priority"] = typing.cast(
            "capo_devops_agent.types.recommendation_priority.RecommendationPriority", ""
        )
    if data.get("goalVersion") is not None:
        out["goal_version"] = data["goalVersion"]
    if data.get("additionalContext") is not None:
        out["additional_context"] = data["additionalContext"]
    if data.get("rankPosition") is not None:
        out["rank_position"] = data["rankPosition"]
    if data.get("rankedAt") is not None:
        import capo_devops_agent.types.back_log_timestamp

        out["ranked_at"] = capo_devops_agent.types.back_log_timestamp.deserialize_json(
            data["rankedAt"]
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
    return out

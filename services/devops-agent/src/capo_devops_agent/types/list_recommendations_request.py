"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.recommendation_priority
    import capo_devops_agent.types.recommendation_status
    import capo_devops_agent.types.resource_id


class ListRecommendationsRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space containing the recommendations</p>"""
    task_id: NotRequired["capo_devops_agent.types.resource_id.ResourceId"]
    """<p>Optional task ID to filter recommendations by specific task</p>"""
    goal_id: NotRequired["capo_devops_agent.types.resource_id.ResourceId"]
    """<p>Optional goal ID to filter recommendations by specific goal</p>"""
    status: NotRequired[
        "capo_devops_agent.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Optional status to filter recommendations by their current status</p>"""
    priority: NotRequired[
        "capo_devops_agent.types.recommendation_priority.RecommendationPriority"
    ]
    """<p>Optional priority to filter recommendations by priority level</p>"""
    limit: NotRequired["int"]
    """<p>Maximum number of recommendations to return in a single response</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsRequest) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "goal_id" in value:
        out["goalId"] = value["goal_id"]
    if "status" in value:
        import capo_devops_agent.types.recommendation_status

        out["status"] = capo_devops_agent.types.recommendation_status.serialize_json(
            value["status"]
        )
    if "priority" in value:
        import capo_devops_agent.types.recommendation_priority

        out["priority"] = (
            capo_devops_agent.types.recommendation_priority.serialize_json(
                value["priority"]
            )
        )
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommendationsRequest:
    out: ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("goalId") is not None:
        out["goal_id"] = data["goalId"]
    if data.get("status") is not None:
        import capo_devops_agent.types.recommendation_status

        out["status"] = capo_devops_agent.types.recommendation_status.deserialize_json(
            data["status"]
        )
    if data.get("priority") is not None:
        import capo_devops_agent.types.recommendation_priority

        out["priority"] = (
            capo_devops_agent.types.recommendation_priority.deserialize_json(
                data["priority"]
            )
        )
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListBacklogTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.task_filter
    import capo_devops_agent.types.task_sort_field
    import capo_devops_agent.types.task_sort_order


class ListBacklogTasksRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space containing the tasks</p>"""
    filter: NotRequired["capo_devops_agent.types.task_filter.TaskFilter"]
    """<p>Filter criteria to apply when listing tasks Filtering restrictions: - Each filter field list is limited to a single value - Filtering by Priority and Status at the same time when not filtering by Type is not permitted - Timestamp filters (createdAfter, createdBefore) can be combined with other filters when not sorting by priority</p>"""
    limit: NotRequired["int"]
    """<p>Maximum number of tasks to return in a single response (1-1000, default: 100)</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results</p>"""
    sort_field: NotRequired["capo_devops_agent.types.task_sort_field.TaskSortField"]
    """<p>Field to sort by Sorting restrictions: - Only sorting on createdAt is supported when using priority or status filters alone. - Sorting by priority is not supported when using Timestamp filters (createdAfter, createdBefore)</p>"""
    order: NotRequired["capo_devops_agent.types.task_sort_order.TaskSortOrder"]
    """<p>Sort order for the tasks based on sortField (default: DESC)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBacklogTasksRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_devops_agent.types.task_filter

        out["filter"] = capo_devops_agent.types.task_filter.serialize_json(
            value["filter"]
        )
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_field" in value:
        import capo_devops_agent.types.task_sort_field

        out["sortField"] = capo_devops_agent.types.task_sort_field.serialize_json(
            value["sort_field"]
        )
    if "order" in value:
        import capo_devops_agent.types.task_sort_order

        out["order"] = capo_devops_agent.types.task_sort_order.serialize_json(
            value["order"]
        )
    return out


def deserialize_json(data: dict) -> ListBacklogTasksRequest:
    out: ListBacklogTasksRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_devops_agent.types.task_filter

        out["filter"] = capo_devops_agent.types.task_filter.deserialize_json(
            data["filter"]
        )
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("sortField") is not None:
        import capo_devops_agent.types.task_sort_field

        out["sort_field"] = capo_devops_agent.types.task_sort_field.deserialize_json(
            data["sortField"]
        )
    if data.get("order") is not None:
        import capo_devops_agent.types.task_sort_order

        out["order"] = capo_devops_agent.types.task_sort_order.deserialize_json(
            data["order"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ListMemoriesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id_list
    import capo_opensearchmemory.types.max_results
    import capo_opensearchmemory.types.memory_sort_field
    import capo_opensearchmemory.types.pagination_token
    import capo_opensearchmemory.types.session_id_list
    import capo_opensearchmemory.types.sort_order
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.strategy_selector_list


class ListMemoriesInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The space whose memories to list.</p>"""
    memory_strategies: NotRequired[
        "capo_opensearchmemory.types.strategy_selector_list.StrategySelectorList"
    ]
    """<p>The strategies to list, as selectors. A selector without <code>memoryStrategyNames</code> lists every strategy of its type, and omitting <code>memoryStrategies</code> lists every strategy in the space. A name that is not a declared strategy of that type fails with <code>ValidationException</code>.</p>"""
    actor_ids: NotRequired["capo_opensearchmemory.types.actor_id_list.ActorIdList"]
    """<p>Lists only memories owned by one of these actors. Combined with <code>sessionIds</code> by AND: a memory must match both filters when both are given. Omit for no actor filter. An empty list fails validation. A memory stored without an actor never matches an actor filter.</p>"""
    session_ids: NotRequired[
        "capo_opensearchmemory.types.session_id_list.SessionIdList"
    ]
    """<p>Lists only memories from one of these sessions. Combined with <code>actorIds</code> by AND. Omit for no session filter. An empty list fails validation. A memory stored without a session never matches a session filter.</p>"""
    sort_by: NotRequired[
        "capo_opensearchmemory.types.memory_sort_field.MemorySortField"
    ]
    """<p>The timestamp to sort by, as returned in <code>systemMetadata</code>: <code>CREATED_AT</code> (the default) or <code>UPDATED_AT</code>.</p>"""
    sort_order: NotRequired["capo_opensearchmemory.types.sort_order.SortOrder"]
    """<p>The sort order: <code>ASC</code> or <code>DESC</code>. The default is <code>DESC</code>, most recent first.</p>"""
    max_results: NotRequired["capo_opensearchmemory.types.max_results.MaxResults"]
    """<p>The maximum number of memories to return, from 1 to 100. The default is 20.</p>"""
    next_token: NotRequired[
        "capo_opensearchmemory.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMemoriesInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "memory_strategies" in value:
        import capo_opensearchmemory.types.strategy_selector_list

        out["memoryStrategies"] = (
            capo_opensearchmemory.types.strategy_selector_list.serialize_aws_json_1_0(
                value["memory_strategies"]
            )
        )
    if "actor_ids" in value:
        import capo_opensearchmemory.types.actor_id_list

        out["actorIds"] = (
            capo_opensearchmemory.types.actor_id_list.serialize_aws_json_1_0(
                value["actor_ids"]
            )
        )
    if "session_ids" in value:
        import capo_opensearchmemory.types.session_id_list

        out["sessionIds"] = (
            capo_opensearchmemory.types.session_id_list.serialize_aws_json_1_0(
                value["session_ids"]
            )
        )
    if "sort_by" in value:
        import capo_opensearchmemory.types.memory_sort_field

        out["sortBy"] = (
            capo_opensearchmemory.types.memory_sort_field.serialize_aws_json_1_0(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_opensearchmemory.types.sort_order

        out["sortOrder"] = (
            capo_opensearchmemory.types.sort_order.serialize_aws_json_1_0(
                value["sort_order"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMemoriesInput:
    out: ListMemoriesInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("memoryStrategies") is not None:
        import capo_opensearchmemory.types.strategy_selector_list

        out["memory_strategies"] = (
            capo_opensearchmemory.types.strategy_selector_list.deserialize_aws_json_1_0(
                data["memoryStrategies"]
            )
        )
    if data.get("actorIds") is not None:
        import capo_opensearchmemory.types.actor_id_list

        out["actor_ids"] = (
            capo_opensearchmemory.types.actor_id_list.deserialize_aws_json_1_0(
                data["actorIds"]
            )
        )
    if data.get("sessionIds") is not None:
        import capo_opensearchmemory.types.session_id_list

        out["session_ids"] = (
            capo_opensearchmemory.types.session_id_list.deserialize_aws_json_1_0(
                data["sessionIds"]
            )
        )
    if data.get("sortBy") is not None:
        import capo_opensearchmemory.types.memory_sort_field

        out["sort_by"] = (
            capo_opensearchmemory.types.memory_sort_field.deserialize_aws_json_1_0(
                data["sortBy"]
            )
        )
    if data.get("sortOrder") is not None:
        import capo_opensearchmemory.types.sort_order

        out["sort_order"] = (
            capo_opensearchmemory.types.sort_order.deserialize_aws_json_1_0(
                data["sortOrder"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

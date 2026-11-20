"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SearchMemoriesInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.max_results
    import capo_opensearchmemory.types.pagination_token
    import capo_opensearchmemory.types.search_query
    import capo_opensearchmemory.types.search_sort
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.strategy_selector_list


class SearchMemoriesInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The space to search. Use <code>actorId</code> to narrow the search within it.</p>"""
    memory_strategies: NotRequired[
        "capo_opensearchmemory.types.strategy_selector_list.StrategySelectorList"
    ]
    """<p>The strategies to search, as a list of selectors. Each selector names a memory type and, optionally, specific strategy names of that type. A space can hold several strategies of the same type. A selector without <code>memoryStrategyNames</code> searches every strategy of its type, and omitting <code>memoryStrategies</code> searches every strategy in the space. A name that is not a declared strategy of that type fails with <code>ValidationException</code>.</p>"""
    actor_id: "capo_opensearchmemory.types.actor_id.ActorId"
    """<p>The actor whose memories to search (exact match). Required: every search covers exactly one actor, and a memory stored without an actor is never returned. This is the only way to filter by actor: a query that references <code>system_metadata.actor_id</code> fails with <code>ValidationException</code> (reason <code>nonFilterableField</code>).</p>"""
    query: "capo_opensearchmemory.types.search_query.SearchQuery"
    """<p>The query: a subset of the OpenSearch Query DSL (see <code>SearchQuery</code>). You can't use the actor and session fields <code>system_metadata.actor_id</code> and <code>system_metadata.session_id</code> here. Use the top-level <code>actorId</code> to filter by actor. Searching memories doesn't filter by session.</p>"""
    sort: NotRequired["capo_opensearchmemory.types.search_sort.SearchSort"]
    """<p>The sort order (see <code>SearchSort</code>). Omit to return the most relevant memories first.</p>"""
    max_results: NotRequired["capo_opensearchmemory.types.max_results.MaxResults"]
    """<p>The maximum number of memories to return, from 1 to 100. The default is 20.</p>"""
    next_token: NotRequired[
        "capo_opensearchmemory.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchMemoriesInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "memory_strategies" in value:
        import capo_opensearchmemory.types.strategy_selector_list

        out["memoryStrategies"] = (
            capo_opensearchmemory.types.strategy_selector_list.serialize_aws_json_1_0(
                value["memory_strategies"]
            )
        )
    out["actorId"] = value["actor_id"]
    out["query"] = value["query"]
    if "sort" in value:
        out["sort"] = value["sort"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchMemoriesInput:
    out: SearchMemoriesInput = {}  # type: ignore[typeddict-item]
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
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        out["actor_id"] = ""
    if data.get("query") is not None:
        out["query"] = data["query"]
    else:
        out["query"] = None
    if data.get("sort") is not None:
        out["sort"] = data["sort"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: SearchMemoriesInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query" in value:
        out["query"] = "*** Sensitive Data Redacted ***"
    if "sort" in value:
        out["sort"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SearchEventsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.max_results
    import capo_opensearchmemory.types.pagination_token
    import capo_opensearchmemory.types.search_query
    import capo_opensearchmemory.types.search_sort
    import capo_opensearchmemory.types.session_id_list
    import capo_opensearchmemory.types.space_id


class SearchEventsInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The space whose events to search. Use <code>actorId</code> and <code>sessionIds</code> to narrow the search within it.</p>"""
    actor_id: "capo_opensearchmemory.types.actor_id.ActorId"
    """<p>The actor whose events to search (exact match). Required: every search covers exactly one actor, and an event stored without an actor is never returned. Narrow the search further with <code>sessionIds</code>, combined by AND. This is the only way to filter by actor: a query that references <code>system_metadata.actor_id</code> fails with <code>ValidationException</code> (reason <code>nonFilterableField</code>).</p>"""
    session_ids: NotRequired[
        "capo_opensearchmemory.types.session_id_list.SessionIdList"
    ]
    """<p>Returns only events from one of these sessions (exact match). Combined with <code>actorId</code> by AND. Omit for no session filter. An empty list fails validation. An event stored without a session never matches a session filter. This is the only way to filter by session: a query that references <code>system_metadata.session_id</code> fails with <code>ValidationException</code> (reason <code>nonFilterableField</code>).</p>"""
    query: "capo_opensearchmemory.types.search_query.SearchQuery"
    """<p>The query: a subset of the OpenSearch Query DSL (see <code>SearchQuery</code>), validated by the same rules as on <code>SearchMemories</code>. Query event text as <code>text</code> and embeddings as <code>vector</code>. A search covers both conversation turns and chunks of documents submitted as a <code>blob</code>. You can't use actor and session fields here. Use the top-level <code>actorId</code> and <code>sessionIds</code>.</p> <p>To search only the content of particular events, filter on <code>event_ids</code> with <code>term</code> or <code>terms</code>, for example with the <code>sourceEventIds</code> that a <code>SearchMemories</code> result returns. A <code>terms</code> clause on <code>event_ids</code> can list up to 10 event IDs. More IDs fail with <code>ValidationException</code> (reason <code>queryBodyTooLarge</code>). You can use <code>event_ids</code> only in <code>term</code>, <code>terms</code>, and <code>exists</code> queries.</p>"""
    sort: NotRequired["capo_opensearchmemory.types.search_sort.SearchSort"]
    """<p>The sort order (see <code>SearchSort</code>). Omit to return the most relevant events first.</p>"""
    max_results: NotRequired["capo_opensearchmemory.types.max_results.MaxResults"]
    """<p>The maximum number of events to return, from 1 to 100. The default is 20.</p>"""
    next_token: NotRequired[
        "capo_opensearchmemory.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchEventsInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["actorId"] = value["actor_id"]
    if "session_ids" in value:
        import capo_opensearchmemory.types.session_id_list

        out["sessionIds"] = (
            capo_opensearchmemory.types.session_id_list.serialize_aws_json_1_0(
                value["session_ids"]
            )
        )
    out["query"] = value["query"]
    if "sort" in value:
        out["sort"] = value["sort"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchEventsInput:
    out: SearchEventsInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        out["actor_id"] = ""
    if data.get("sessionIds") is not None:
        import capo_opensearchmemory.types.session_id_list

        out["session_ids"] = (
            capo_opensearchmemory.types.session_id_list.deserialize_aws_json_1_0(
                data["sessionIds"]
            )
        )
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


def redact_sensitive(value: SearchEventsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query" in value:
        out["query"] = "*** Sensitive Data Redacted ***"
    if "sort" in value:
        out["sort"] = "*** Sensitive Data Redacted ***"
    return out

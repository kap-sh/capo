"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ListEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.event_timestamp
    import capo_opensearchmemory.types.max_results
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.pagination_token
    import capo_opensearchmemory.types.session_id
    import capo_opensearchmemory.types.sort_order
    import capo_opensearchmemory.types.space_id


class ListEventsInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""
    actor_id: "capo_opensearchmemory.types.actor_id.ActorId"
    """<p>The actor whose events to list.</p>"""
    session_id: "capo_opensearchmemory.types.session_id.SessionId"
    """<p>The session whose events to list. To find events across sessions, use <code>SearchEvents</code>.</p>"""
    event_timestamp_before: NotRequired[
        "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
    ]
    """<p>Inclusive upper bound on <code>eventTimestamp</code>: only events at or before this time are returned. Omit for no upper bound.</p>"""
    event_timestamp_after: NotRequired[
        "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
    ]
    """<p>Inclusive lower bound on <code>eventTimestamp</code>: only events at or after this time are returned. Omit for no lower bound.</p> <p>If it's later than <code>eventTimestampBefore</code>, the request fails with <code>ValidationException</code>.</p>"""
    sort_order: NotRequired["capo_opensearchmemory.types.sort_order.SortOrder"]
    """<p>The order of the results by <code>eventTimestamp</code>: <code>ASC</code> or <code>DESC</code>. The default is <code>DESC</code>, most recent first.</p>"""
    metadata_filters: NotRequired[
        "capo_opensearchmemory.types.metadata_map.MetadataMap"
    ]
    """<p>Returns only events whose metadata contains every one of these key-value pairs. Omit, or leave empty, for no metadata filter. The service applies the filter after it reads events, so a page can hold fewer than <code>maxResults</code> events, or none, and still return a <code>nextToken</code>. Keep paging until <code>nextToken</code> is absent.</p>"""
    max_results: NotRequired["capo_opensearchmemory.types.max_results.MaxResults"]
    """<p>The maximum number of events to return, from 1 to 100. The default is 20.</p>"""
    next_token: NotRequired[
        "capo_opensearchmemory.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEventsInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["actorId"] = value["actor_id"]
    out["sessionId"] = value["session_id"]
    if "event_timestamp_before" in value:
        import capo_opensearchmemory.types.event_timestamp

        out["eventTimestampBefore"] = (
            capo_opensearchmemory.types.event_timestamp.serialize_aws_json_1_0(
                value["event_timestamp_before"]
            )
        )
    if "event_timestamp_after" in value:
        import capo_opensearchmemory.types.event_timestamp

        out["eventTimestampAfter"] = (
            capo_opensearchmemory.types.event_timestamp.serialize_aws_json_1_0(
                value["event_timestamp_after"]
            )
        )
    if "sort_order" in value:
        import capo_opensearchmemory.types.sort_order

        out["sortOrder"] = (
            capo_opensearchmemory.types.sort_order.serialize_aws_json_1_0(
                value["sort_order"]
            )
        )
    if "metadata_filters" in value:
        import capo_opensearchmemory.types.metadata_map

        out["metadataFilters"] = (
            capo_opensearchmemory.types.metadata_map.serialize_aws_json_1_0(
                value["metadata_filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEventsInput:
    out: ListEventsInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        out["actor_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("eventTimestampBefore") is not None:
        import capo_opensearchmemory.types.event_timestamp

        out["event_timestamp_before"] = (
            capo_opensearchmemory.types.event_timestamp.deserialize_aws_json_1_0(
                data["eventTimestampBefore"]
            )
        )
    if data.get("eventTimestampAfter") is not None:
        import capo_opensearchmemory.types.event_timestamp

        out["event_timestamp_after"] = (
            capo_opensearchmemory.types.event_timestamp.deserialize_aws_json_1_0(
                data["eventTimestampAfter"]
            )
        )
    if data.get("sortOrder") is not None:
        import capo_opensearchmemory.types.sort_order

        out["sort_order"] = (
            capo_opensearchmemory.types.sort_order.deserialize_aws_json_1_0(
                data["sortOrder"]
            )
        )
    if data.get("metadataFilters") is not None:
        import capo_opensearchmemory.types.metadata_map

        out["metadata_filters"] = (
            capo_opensearchmemory.types.metadata_map.deserialize_aws_json_1_0(
                data["metadataFilters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

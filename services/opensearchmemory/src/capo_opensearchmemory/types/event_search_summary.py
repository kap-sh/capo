"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#EventSearchSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_id
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.sensitive_content
    import capo_opensearchmemory.types.system_metadata


class EventSearchSummary(TypedDict, closed=True):
    event_id: "capo_opensearchmemory.types.event_id.EventId"
    """<p>The ID of the event that the chunk belongs to. Use it with <code>GetEvent</code> or <code>DeleteEvent</code>.</p>"""
    score: NotRequired["float"]
    """<p>The relevance score of the result. A higher score is more relevant. Scores aren't normalized to a fixed range and can be greater than 1, so use them only to order results.</p>"""
    system_metadata: NotRequired[
        "capo_opensearchmemory.types.system_metadata.SystemMetadata"
    ]
    """<p>Provenance for the chunk: the owning actor and session, and when it was created and last updated. It is the same block that <code>ListMemories</code> and <code>SearchMemories</code> return. Event chunks are never modified, so <code>updatedAt</code> always equals <code>createdAt</code>.</p> <p>Absent when the service has no provenance for the chunk.</p>"""
    metadata: NotRequired["capo_opensearchmemory.types.metadata_map.MetadataMap"]
    """<p>The event's metadata tags. All values are strings. In a query, filter on a tag as <code>metadata.&lt;key&gt;</code>.</p>"""
    matched_content: NotRequired[
        "capo_opensearchmemory.types.sensitive_content.SensitiveContent"
    ]
    """<p>The text of the matching chunk.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventSearchSummary) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    if "score" in value:
        out["score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "system_metadata" in value:
        import capo_opensearchmemory.types.system_metadata

        out["systemMetadata"] = (
            capo_opensearchmemory.types.system_metadata.serialize_aws_json_1_0(
                value["system_metadata"]
            )
        )
    if "metadata" in value:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.serialize_aws_json_1_0(
                value["metadata"]
            )
        )
    if "matched_content" in value:
        out["matchedContent"] = value["matched_content"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EventSearchSummary:
    out: EventSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    if data.get("systemMetadata") is not None:
        import capo_opensearchmemory.types.system_metadata

        out["system_metadata"] = (
            capo_opensearchmemory.types.system_metadata.deserialize_aws_json_1_0(
                data["systemMetadata"]
            )
        )
    if data.get("metadata") is not None:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.deserialize_aws_json_1_0(
                data["metadata"]
            )
        )
    if data.get("matchedContent") is not None:
        out["matched_content"] = data["matchedContent"]
    return out


def redact_sensitive(value: EventSearchSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "matched_content" in value:
        out["matched_content"] = "*** Sensitive Data Redacted ***"
    return out

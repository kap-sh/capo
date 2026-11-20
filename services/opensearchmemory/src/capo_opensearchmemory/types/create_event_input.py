"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#CreateEventInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.client_token
    import capo_opensearchmemory.types.event_payload
    import capo_opensearchmemory.types.event_timestamp
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.session_id
    import capo_opensearchmemory.types.space_id


class CreateEventInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space that owns the event, for example <code>sp-02864597b164</code>.</p>"""
    actor_id: "capo_opensearchmemory.types.actor_id.ActorId"
    """<p>The ID of the actor (end user or agent) that the event belongs to.</p>"""
    session_id: NotRequired["capo_opensearchmemory.types.session_id.SessionId"]
    """<p>The session the event belongs to. Send every event of one conversation with the same session ID, so that <code>SUMMARY</code> strategies summarize the conversation as one session. If you omit it, the service generates a session ID and returns it.</p>"""
    event_timestamp: NotRequired[
        "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
    ]
    """<p>When the event occurred. The default is the time that the service receives the request.</p>"""
    payload: "capo_opensearchmemory.types.event_payload.EventPayload"
    """<p>The event content. Set exactly one union member.</p>"""
    metadata: NotRequired["capo_opensearchmemory.types.metadata_map.MetadataMap"]
    """<p>Metadata tags to store with the event. Memories derived from the event carry the same tags. Keys that begin with <code>x-amz-</code>, the keys <code>documentS3Source</code> and <code>documentS3Url</code>, and other keys that the service uses internally are reserved: a request that sets one fails with <code>ValidationException</code>, and the message names the key.</p> <p>A space can use at most 50 distinct metadata keys across all of its events and memories. A request that would add a key beyond that fails with <code>ValidationException</code>. Reuse an existing key instead.</p>"""
    client_token: NotRequired["capo_opensearchmemory.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that makes the request idempotent. Within 2 hours of the first request, a retry with the same token and the same request, including the same <code>sessionId</code>, returns the same event. If you omit <code>sessionId</code>, the service generates a new one on each attempt, so a retry fails with <code>ConflictException</code>. Reusing the token with different request content also fails with <code>ConflictException</code>. <code>eventTimestamp</code> isn't compared. After 2 hours, the token starts a new event.</p>"""
    infer: NotRequired["bool"]
    """<p>Specifies whether to extract memories from this event. The default is <code>true</code>. Set it to <code>false</code> to store the event without extraction: the service skips strategies that infer memories, and still indexes the event's turns for <code>SearchEvents</code>. A document submitted as a <code>blob</code> is still extracted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEventInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["actorId"] = value["actor_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "event_timestamp" in value:
        import capo_opensearchmemory.types.event_timestamp

        out["eventTimestamp"] = (
            capo_opensearchmemory.types.event_timestamp.serialize_aws_json_1_0(
                value["event_timestamp"]
            )
        )
    import capo_opensearchmemory.types.event_payload

    out["payload"] = capo_opensearchmemory.types.event_payload.serialize_aws_json_1_0(
        value["payload"]
    )
    if "metadata" in value:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.serialize_aws_json_1_0(
                value["metadata"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "infer" in value:
        out["infer"] = value["infer"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEventInput:
    out: CreateEventInput = {}  # type: ignore[typeddict-item]
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
    if data.get("eventTimestamp") is not None:
        import capo_opensearchmemory.types.event_timestamp

        out["event_timestamp"] = (
            capo_opensearchmemory.types.event_timestamp.deserialize_aws_json_1_0(
                data["eventTimestamp"]
            )
        )
    if data.get("payload") is not None:
        import capo_opensearchmemory.types.event_payload

        out["payload"] = (
            capo_opensearchmemory.types.event_payload.deserialize_aws_json_1_0(
                data["payload"]
            )
        )
    else:
        out["payload"] = {"$unknown": {"name": ""}}
    if data.get("metadata") is not None:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.deserialize_aws_json_1_0(
                data["metadata"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("infer") is not None:
        out["infer"] = data["infer"]
    return out


def redact_sensitive(value: CreateEventInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_opensearchmemory.types.event_payload

        out["payload"] = capo_opensearchmemory.types.event_payload.redact_sensitive(
            value["payload"]
        )
    return out

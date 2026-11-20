"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#CreateMemoryInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.client_token
    import capo_opensearchmemory.types.create_memory_content
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.session_id
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.strategy_name


class CreateMemoryInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space that owns the memory, for example <code>sp-02864597b164</code>.</p>"""
    name: "capo_opensearchmemory.types.strategy_name.StrategyName"
    """<p>The name of the strategy that the memory belongs to. The space must already declare the strategy, and the memory's type comes from that strategy. The name must be 1 to 64 characters: letters, digits, periods, hyphens, and underscores, starting with a letter or digit.</p>"""
    content: "capo_opensearchmemory.types.create_memory_content.CreateMemoryContent"
    """<p>The memory text, stored and embedded as provided.</p>"""
    actor_id: "capo_opensearchmemory.types.actor_id.ActorId"
    """<p>The actor (end user or agent) that owns the memory.</p>"""
    session_id: NotRequired["capo_opensearchmemory.types.session_id.SessionId"]
    """<p>The session that the memory belongs to. If you omit it, the service generates a session ID and returns it.</p>"""
    metadata: NotRequired["capo_opensearchmemory.types.metadata_map.MetadataMap"]
    """<p>Metadata tags to store with the memory. Keys that begin with <code>x-amz-</code>, the key <code>documentS3Source</code>, and other keys that the service uses internally are reserved: a request that sets one fails with <code>ValidationException</code>, and the message names the key.</p> <p>A space can use at most 50 distinct metadata keys across all of its events and memories. A request that would add a key beyond that fails with <code>ValidationException</code>. Reuse an existing key instead.</p>"""
    client_token: NotRequired["capo_opensearchmemory.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that makes the request idempotent. Within 2 hours of the first request, a retry with the same token returns the same <code>memoryId</code> instead of creating a second memory. Reusing the token with a different <code>name</code>, <code>content</code>, <code>metadata</code>, <code>actorId</code>, or <code>sessionId</code> fails with <code>ConflictException</code>. If you omit <code>sessionId</code>, a retry with the same token gets the same session. If you omit the token, each call creates a new memory.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateMemoryInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["name"] = value["name"]
    out["content"] = value["content"]
    out["actorId"] = value["actor_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "metadata" in value:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.serialize_aws_json_1_0(
                value["metadata"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateMemoryInput:
    out: CreateMemoryInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        out["actor_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("metadata") is not None:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.deserialize_aws_json_1_0(
                data["metadata"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateMemoryInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out

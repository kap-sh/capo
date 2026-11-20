"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SystemMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.session_id


class SystemMetadata(TypedDict, closed=True):
    actor_id: NotRequired["capo_opensearchmemory.types.actor_id.ActorId"]
    """<p>The owning actor. Absent when none was recorded.</p>"""
    session_id: NotRequired["capo_opensearchmemory.types.session_id.SessionId"]
    """<p>The owning session. Absent when none was recorded.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>When the record was created. Always present on <code>ListMemories</code> and <code>GetMemory</code>. It can be absent from search results.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>When the record was last updated. Equals <code>createdAt</code> for a record that has never been updated, and always for a <code>SearchEvents</code> result.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SystemMetadata) -> dict:
    out: dict = {}
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "created_at" in value:
        import capo_opensearchmemory._protocol.serialize

        out["createdAt"] = capo_opensearchmemory._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_opensearchmemory._protocol.serialize

        out["updatedAt"] = capo_opensearchmemory._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SystemMetadata:
    out: SystemMetadata = {}  # type: ignore[typeddict-item]
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class SessionSummary(TypedDict, closed=True):
    session_id: "str"
    """The unique ID of the session."""
    created_at: NotRequired["datetime.datetime"]
    """The timestamp when the session was created."""
    last_activity_at: NotRequired["datetime.datetime"]
    """The timestamp of the most recent activity in the session."""
    session_name: NotRequired["str"]
    """The human-readable name of the session. Names under `/aws/` are reserved for service integrations."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    if "created_at" in value:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "last_activity_at" in value:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["lastActivityAt"] = (
            capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
                value["last_activity_at"]
            )
        )
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    return out


def deserialize_cbor(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    if data.get("lastActivityAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["last_activity_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["lastActivityAt"]
            )
        )
    if data.get("sessionName") is not None:
        out["session_name"] = data["sessionName"]
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.session_arn
    import capo_bedrock_agent_runtime.types.session_status
    import capo_bedrock_agent_runtime.types.uuid


class SessionSummary(TypedDict, closed=True):
    session_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the session.</p>"""
    session_arn: "capo_bedrock_agent_runtime.types.session_arn.SessionArn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    session_status: "capo_bedrock_agent_runtime.types.session_status.SessionStatus"
    """<p>The current status of the session.</p>"""
    created_at: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp for when the session was created.</p>"""
    last_updated_at: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp for when the session was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    import capo_bedrock_agent_runtime.types.session_status

    out["sessionStatus"] = (
        capo_bedrock_agent_runtime.types.session_status.serialize_json(
            value["session_status"]
        )
    )
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("sessionStatus") is not None:
        import capo_bedrock_agent_runtime.types.session_status

        out["session_status"] = (
            capo_bedrock_agent_runtime.types.session_status.deserialize_json(
                data["sessionStatus"]
            )
        )
    else:
        import typing

        out["session_status"] = typing.cast(
            "capo_bedrock_agent_runtime.types.session_status.SessionStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out

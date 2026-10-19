"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserSessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_session_id
    import capo_bedrock_agentcore.types.browser_session_status
    import capo_bedrock_agentcore.types.date_timestamp
    import capo_bedrock_agentcore.types.name


class BrowserSessionSummary(TypedDict, closed=True):
    browser_identifier: "str"
    """<p>The unique identifier of the browser associated with the session. This identifier specifies which browser environment is used for the session.</p>"""
    session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the browser session. This identifier is used in operations that interact with the session.</p>"""
    name: NotRequired["capo_bedrock_agentcore.types.name.Name"]
    """<p>The name of the browser session. This name helps identify and manage the session.</p>"""
    status: "capo_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"
    """<p>The current status of the browser session. Possible values include ACTIVE, STOPPING, and STOPPED.</p>"""
    created_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser session was created. This value is in ISO 8601 format.</p>"""
    last_updated_at: NotRequired[
        "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the browser session was last updated. This value is in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSessionSummary) -> dict:
    out: dict = {}
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_bedrock_agentcore.types.browser_session_status

    out["status"] = capo_bedrock_agentcore.types.browser_session_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "last_updated_at" in value:
        import capo_bedrock_agentcore.types.date_timestamp

        out["lastUpdatedAt"] = (
            capo_bedrock_agentcore.types.date_timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrowserSessionSummary:
    out: BrowserSessionSummary = {}  # type: ignore[typeddict-item]
    if data.get("browserIdentifier") is not None:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        out["browser_identifier"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.browser_session_status

        out["status"] = (
            capo_bedrock_agentcore.types.browser_session_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out

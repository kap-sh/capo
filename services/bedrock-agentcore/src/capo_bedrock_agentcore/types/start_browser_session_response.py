"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartBrowserSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_session_id
    import capo_bedrock_agentcore.types.browser_session_stream
    import capo_bedrock_agentcore.types.date_timestamp


class StartBrowserSessionResponse(TypedDict, closed=True):
    browser_identifier: "str"
    """<p>The identifier of the browser.</p>"""
    session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the created browser session.</p>"""
    created_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser session was created.</p>"""
    streams: NotRequired[
        "capo_bedrock_agentcore.types.browser_session_stream.BrowserSessionStream"
    ]
    """<p>The streams associated with this browser session. These include the automation stream and live view stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBrowserSessionResponse) -> dict:
    out: dict = {}
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    import capo_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "streams" in value:
        import capo_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            capo_bedrock_agentcore.types.browser_session_stream.serialize_json(
                value["streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartBrowserSessionResponse:
    out: StartBrowserSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("browserIdentifier") is not None:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        out["browser_identifier"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
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
    if data.get("streams") is not None:
        import capo_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            capo_bedrock_agentcore.types.browser_session_stream.deserialize_json(
                data["streams"]
            )
        )
    return out

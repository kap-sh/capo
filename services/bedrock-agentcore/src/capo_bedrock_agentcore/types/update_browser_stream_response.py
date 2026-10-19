"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UpdateBrowserStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_session_id
    import capo_bedrock_agentcore.types.browser_session_stream
    import capo_bedrock_agentcore.types.date_timestamp


class UpdateBrowserStreamResponse(TypedDict, closed=True):
    browser_identifier: "str"
    """<p>The identifier of the browser.</p>"""
    session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The identifier of the browser session.</p>"""
    streams: "capo_bedrock_agentcore.types.browser_session_stream.BrowserSessionStream"
    updated_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The time at which the browser stream was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrowserStreamResponse) -> dict:
    out: dict = {}
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    import capo_bedrock_agentcore.types.browser_session_stream

    out["streams"] = capo_bedrock_agentcore.types.browser_session_stream.serialize_json(
        value["streams"]
    )
    import capo_bedrock_agentcore.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateBrowserStreamResponse:
    out: UpdateBrowserStreamResponse = {}  # type: ignore[typeddict-item]
    if data.get("browserIdentifier") is not None:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        out["browser_identifier"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("streams") is not None:
        import capo_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            capo_bedrock_agentcore.types.browser_session_stream.deserialize_json(
                data["streams"]
            )
        )
    else:
        raise DeserializationError("UpdateBrowserStreamResponse.streams required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

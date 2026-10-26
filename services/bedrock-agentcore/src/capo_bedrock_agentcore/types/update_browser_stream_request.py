"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UpdateBrowserStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_session_id
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.stream_update


class UpdateBrowserStreamRequest(TypedDict, closed=True):
    browser_identifier: "str"
    """<p>The identifier of the browser.</p>"""
    session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The identifier of the browser session.</p>"""
    stream_update: "capo_bedrock_agentcore.types.stream_update.StreamUpdate"
    """<p>The update to apply to the browser stream.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrowserStreamRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.stream_update

    out["streamUpdate"] = capo_bedrock_agentcore.types.stream_update.serialize_json(
        value["stream_update"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateBrowserStreamRequest:
    out: UpdateBrowserStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("streamUpdate") is not None:
        import capo_bedrock_agentcore.types.stream_update

        out["stream_update"] = (
            capo_bedrock_agentcore.types.stream_update.deserialize_json(
                data["streamUpdate"]
            )
        )
    else:
        out["stream_update"] = {"$unknown": {"name": ""}}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

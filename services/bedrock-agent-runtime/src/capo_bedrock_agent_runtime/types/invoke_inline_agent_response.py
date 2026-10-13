"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeInlineAgentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.inline_agent_response_stream
    import capo_bedrock_agent_runtime.types.mime_type
    import capo_bedrock_agent_runtime.types.session_id


class InvokeInlineAgentResponse(TypedDict, closed=True):
    completion: "capo_bedrock_agent_runtime.types.inline_agent_response_stream.InlineAgentResponseStream"
    """<p>The inline agent's response to the user prompt. </p>"""
    content_type: "capo_bedrock_agent_runtime.types.mime_type.MimeType"
    """<p> The MIME type of the input data in the request. The default value is application/json. </p>"""
    session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId"
    """<p> The unique identifier of the session with the agent. </p>"""


def redact_sensitive(value: InvokeInlineAgentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "completion" in value:
        out["completion"] = "*** Streaming Data Redacted ***"
    return out

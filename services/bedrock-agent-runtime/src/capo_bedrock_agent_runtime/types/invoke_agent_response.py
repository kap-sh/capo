"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeAgentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.memory_id
    import capo_bedrock_agent_runtime.types.mime_type
    import capo_bedrock_agent_runtime.types.response_stream
    import capo_bedrock_agent_runtime.types.session_id


class InvokeAgentResponse(TypedDict, closed=True):
    completion: "capo_bedrock_agent_runtime.types.response_stream.ResponseStream"
    """<p>The agent's response to the user prompt.</p>"""
    content_type: "capo_bedrock_agent_runtime.types.mime_type.MimeType"
    """<p>The MIME type of the input data in the request. The default value is <code>application/json</code>.</p>"""
    session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId"
    """<p>The unique identifier of the session with the agent.</p>"""
    memory_id: NotRequired["capo_bedrock_agent_runtime.types.memory_id.MemoryId"]
    """<p>The unique identifier of the agent memory.</p>"""


def redact_sensitive(value: InvokeAgentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "completion" in value:
        out["completion"] = "*** Streaming Data Redacted ***"
    return out

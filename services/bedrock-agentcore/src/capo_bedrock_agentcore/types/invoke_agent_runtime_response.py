"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.http_response_code
    import capo_bedrock_agentcore.types.response_stream
    import capo_bedrock_agentcore.types.session_id


class InvokeAgentRuntimeResponse(TypedDict, closed=True):
    runtime_session_id: NotRequired["capo_bedrock_agentcore.types.session_id.SessionId"]
    """<p>The identifier of the runtime session.</p>"""
    mcp_session_id: NotRequired["capo_bedrock_agentcore.types.session_id.SessionId"]
    """<p>The identifier of the MCP session.</p>"""
    mcp_protocol_version: NotRequired["str"]
    """<p>The version of the MCP protocol being used.</p>"""
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    trace_state: NotRequired["str"]
    """<p>The trace state information for distributed tracing.</p>"""
    baggage: NotRequired["str"]
    """<p>Additional context information for distributed tracing.</p>"""
    content_type: "str"
    """<p>The MIME type of the response data. This indicates how to interpret the response data. Common values include application/json for JSON data.</p>"""
    response: "capo_bedrock_agentcore.types.response_stream.ResponseStream"
    """<p>The response data from the agent runtime. The format of this data depends on the specific agent configuration and the requested accept type. For most agents, this is a JSON object containing the agent's response to the user's request.</p>"""
    status_code: NotRequired[
        "capo_bedrock_agentcore.types.http_response_code.HttpResponseCode"
    ]
    """<p>The HTTP status code of the response. A status code of 200 indicates a successful operation. Other status codes indicate various error conditions.</p>"""


def redact_sensitive(value: InvokeAgentRuntimeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "response" in value:
        out["response"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeCommandResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.http_response_code
    import capo_bedrock_agentcore.types.invoke_agent_runtime_command_stream_output
    import capo_bedrock_agentcore.types.session_id


class InvokeAgentRuntimeCommandResponse(TypedDict, closed=True):
    runtime_session_id: NotRequired["capo_bedrock_agentcore.types.session_id.SessionId"]
    """<p>The unique identifier of the runtime session in which the command was executed.</p>"""
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
    status_code: NotRequired[
        "capo_bedrock_agentcore.types.http_response_code.HttpResponseCode"
    ]
    """<p>The HTTP status code of the response. A status code of 200 indicates a successful operation. Other status codes indicate various error conditions.</p>"""
    stream: "capo_bedrock_agentcore.types.invoke_agent_runtime_command_stream_output.InvokeAgentRuntimeCommandStreamOutput"
    """<p>The streaming output from the command execution. This stream contains events that provide real-time updates including standard output, standard error, and completion status.</p>"""


def redact_sensitive(value: InvokeAgentRuntimeCommandResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stream" in value:
        out["stream"] = "*** Streaming Data Redacted ***"
    return out

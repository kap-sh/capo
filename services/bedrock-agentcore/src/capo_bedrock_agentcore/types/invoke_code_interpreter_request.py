"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeCodeInterpreterRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.code_interpreter_session_id
    import capo_bedrock_agentcore.types.tool_arguments
    import capo_bedrock_agentcore.types.tool_name


class InvokeCodeInterpreterRequest(TypedDict, closed=True):
    code_interpreter_identifier: "str"
    """<p>The unique identifier of the code interpreter associated with the session. This must match the identifier used when creating the session with <code>StartCodeInterpreterSession</code>.</p>"""
    session_id: NotRequired[
        "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    ]
    """<p>The unique identifier of the code interpreter session to use. This must be an active session created with <code>StartCodeInterpreterSession</code>. If the session has expired or been stopped, the request will fail.</p>"""
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    name: "capo_bedrock_agentcore.types.tool_name.ToolName"
    """<p>The name of the code interpreter to invoke.</p>"""
    arguments: NotRequired["capo_bedrock_agentcore.types.tool_arguments.ToolArguments"]
    """<p>The arguments for the code interpreter. This includes the code to execute and any additional parameters such as the programming language, whether to clear the execution context, and other execution options. The structure of this parameter depends on the specific code interpreter being used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeCodeInterpreterRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.tool_name

    out["name"] = capo_bedrock_agentcore.types.tool_name.serialize_json(value["name"])
    if "arguments" in value:
        import capo_bedrock_agentcore.types.tool_arguments

        out["arguments"] = capo_bedrock_agentcore.types.tool_arguments.serialize_json(
            value["arguments"]
        )
    return out


def deserialize_json(data: dict) -> InvokeCodeInterpreterRequest:
    out: InvokeCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_bedrock_agentcore.types.tool_name

        out["name"] = capo_bedrock_agentcore.types.tool_name.deserialize_json(
            data["name"]
        )
    else:
        import typing

        out["name"] = typing.cast("capo_bedrock_agentcore.types.tool_name.ToolName", "")
    if data.get("arguments") is not None:
        import capo_bedrock_agentcore.types.tool_arguments

        out["arguments"] = capo_bedrock_agentcore.types.tool_arguments.deserialize_json(
            data["arguments"]
        )
    return out


def redact_sensitive(value: InvokeCodeInterpreterRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "arguments" in value:
        import capo_bedrock_agentcore.types.tool_arguments

        out["arguments"] = capo_bedrock_agentcore.types.tool_arguments.redact_sensitive(
            value["arguments"]
        )
    return out

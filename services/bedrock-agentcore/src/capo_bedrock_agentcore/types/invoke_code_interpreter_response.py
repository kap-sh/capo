"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeCodeInterpreterResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.code_interpreter_session_id
    import capo_bedrock_agentcore.types.code_interpreter_stream_output


class InvokeCodeInterpreterResponse(TypedDict, closed=True):
    session_id: NotRequired[
        "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    ]
    """<p>The identifier of the code interpreter session.</p>"""
    stream: "capo_bedrock_agentcore.types.code_interpreter_stream_output.CodeInterpreterStreamOutput"
    """<p>The stream containing the results of the code execution. This includes output, errors, and execution status.</p>"""


def redact_sensitive(value: InvokeCodeInterpreterResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stream" in value:
        out["stream"] = "*** Streaming Data Redacted ***"
    return out

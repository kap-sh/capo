"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarnessResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.invoke_harness_stream_output


class InvokeHarnessResponse(TypedDict, closed=True):
    stream: "capo_bedrock_agentcore.types.invoke_harness_stream_output.InvokeHarnessStreamOutput"
    """<p>The streaming output from the harness invocation.</p>"""


def redact_sensitive(value: InvokeHarnessResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stream" in value:
        out["stream"] = "*** Streaming Data Redacted ***"
    return out

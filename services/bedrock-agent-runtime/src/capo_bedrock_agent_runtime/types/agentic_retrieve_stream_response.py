"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveStreamResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response_output


class AgenticRetrieveStreamResponse(TypedDict, closed=True):
    stream: "capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response_output.AgenticRetrieveStreamResponseOutput"
    """<p>The output stream containing retrieval results and trace events.</p>"""


def redact_sensitive(value: AgenticRetrieveStreamResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stream" in value:
        out["stream"] = "*** Streaming Data Redacted ***"
    return out

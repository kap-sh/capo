"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateStreamResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response_output
    import capo_bedrock_agent_runtime.types.session_id


class RetrieveAndGenerateStreamResponse(TypedDict, closed=True):
    stream: "capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response_output.RetrieveAndGenerateStreamResponseOutput"
    """<p>A stream of events from the model.</p>"""
    session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId"
    """<p>The session ID.</p>"""


def redact_sensitive(value: RetrieveAndGenerateStreamResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stream" in value:
        out["stream"] = "*** Streaming Data Redacted ***"
    return out

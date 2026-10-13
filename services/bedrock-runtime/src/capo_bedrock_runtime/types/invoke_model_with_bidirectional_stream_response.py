"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output


class InvokeModelWithBidirectionalStreamResponse(TypedDict, closed=True):
    body: "capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output.InvokeModelWithBidirectionalStreamOutput"
    """<p>Streaming response from the model in the format specified by the <code>BidirectionalOutputPayloadPart</code> header.</p>"""


def redact_sensitive(
    value: InvokeModelWithBidirectionalStreamResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Streaming Data Redacted ***"
    return out

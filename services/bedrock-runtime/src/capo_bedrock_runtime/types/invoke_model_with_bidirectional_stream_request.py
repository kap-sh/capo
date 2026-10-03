"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.invoke_model_identifier
    import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input


class InvokeModelWithBidirectionalStreamRequest(TypedDict, closed=True):
    model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier"
    """<p>The model ID or ARN of the model ID to use. Currently, only <code>amazon.nova-sonic-v1:0</code> is supported.</p>"""
    body: "capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input.InvokeModelWithBidirectionalStreamInput"
    """<p>The prompt and inference parameters in the format specified in the <code>BidirectionalInputPayloadPart</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>"""

"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithResponseStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.mime_type
    import capo_bedrock_runtime.types.performance_config_latency
    import capo_bedrock_runtime.types.response_stream
    import capo_bedrock_runtime.types.service_tier_type


class InvokeModelWithResponseStreamResponse(TypedDict, closed=True):
    body: "capo_bedrock_runtime.types.response_stream.ResponseStream"
    """<p>Inference response from the model in the format specified by the <code>contentType</code> header. To see the format and content of this field for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>.</p>"""
    content_type: "capo_bedrock_runtime.types.mime_type.MimeType"
    """<p>The MIME type of the inference result.</p>"""
    performance_config_latency: NotRequired[
        "capo_bedrock_runtime.types.performance_config_latency.PerformanceConfigLatency"
    ]
    """<p>Model performance settings for the request.</p>"""
    service_tier: NotRequired[
        "capo_bedrock_runtime.types.service_tier_type.ServiceTierType"
    ]
    """<p>Specifies the processing tier type used for serving the request.</p>"""

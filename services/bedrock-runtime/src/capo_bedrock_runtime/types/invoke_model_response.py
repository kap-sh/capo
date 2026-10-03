"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.body
    import capo_bedrock_runtime.types.mime_type
    import capo_bedrock_runtime.types.performance_config_latency
    import capo_bedrock_runtime.types.service_tier_type


class InvokeModelResponse(TypedDict, closed=True):
    body: "capo_bedrock_runtime.types.body.Body"
    """<p>Inference response from the model in the format specified in the <code>contentType</code> header. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>.</p>"""
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


# --- restJson1 ser/de ---
def serialize_json(value: InvokeModelResponse) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.body

    out["body"] = capo_bedrock_runtime.types.body.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> InvokeModelResponse:
    out: InvokeModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_bedrock_runtime.types.body

        out["body"] = capo_bedrock_runtime.types.body.deserialize_json(data["body"])
    else:
        raise DeserializationError("InvokeModelResponse.body required")
    return out

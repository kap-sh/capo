"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_runtime.types.body_blob
    import capo_sagemaker_runtime.types.custom_attributes_header
    import capo_sagemaker_runtime.types.header
    import capo_sagemaker_runtime.types.new_session_response_header
    import capo_sagemaker_runtime.types.session_id_header


class InvokeEndpointOutput(TypedDict, closed=True):
    body: NotRequired["capo_sagemaker_runtime.types.body_blob.BodyBlob"]
    """<p>Includes the inference provided by the model. </p> <p>For information about the format of the response body, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html">Common Data Formats-Inference</a>.</p> <p>If the explainer is activated, the body includes the explanations provided by the model. For more information, see the <b>Response section</b> under <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response">Invoke the Endpoint</a> in the Developer Guide.</p>"""
    content_type: NotRequired["capo_sagemaker_runtime.types.header.Header"]
    """<p>The MIME type of the inference returned from the model container.</p>"""
    invoked_production_variant: NotRequired[
        "capo_sagemaker_runtime.types.header.Header"
    ]
    """<p>Identifies the production variant that was invoked.</p>"""
    custom_attributes: NotRequired[
        "capo_sagemaker_runtime.types.custom_attributes_header.CustomAttributesHeader"
    ]
    """<p>Provides additional information in the response about the inference returned by a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to return an ID received in the <code>CustomAttributes</code> header of a request or other metadata that a service endpoint was programmed to produce. The value must consist of no more than 1024 visible US-ASCII characters as specified in <a href="https://tools.ietf.org/html/rfc7230#section-3.2.6">Section 3.3.6. Field Value Components</a> of the Hypertext Transfer Protocol (HTTP/1.1). If the customer wants the custom attribute returned, the model must set the custom attribute to be included on the way back. </p> <p>The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with <code>Trace ID:</code> in your post-processing function.</p> <p>This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker AI Python SDK.</p>"""
    new_session_id: NotRequired[
        "capo_sagemaker_runtime.types.new_session_response_header.NewSessionResponseHeader"
    ]
    """<p>If you created a stateful session with your request, the ID and expiration time that the model assigns to that session.</p>"""
    closed_session_id: NotRequired[
        "capo_sagemaker_runtime.types.session_id_header.SessionIdHeader"
    ]
    """<p>If you closed a stateful session with your request, the ID of that session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeEndpointOutput) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_sagemaker_runtime.types.body_blob

        out["Body"] = capo_sagemaker_runtime.types.body_blob.serialize_json(
            value["body"]
        )
    return out


def deserialize_json(data: dict) -> InvokeEndpointOutput:
    out: InvokeEndpointOutput = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_sagemaker_runtime.types.body_blob

        out["body"] = capo_sagemaker_runtime.types.body_blob.deserialize_json(
            data["Body"]
        )
    return out

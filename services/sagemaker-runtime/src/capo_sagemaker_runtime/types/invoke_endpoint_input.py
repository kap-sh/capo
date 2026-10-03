"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_runtime.types.body_blob
    import capo_sagemaker_runtime.types.custom_attributes_header
    import capo_sagemaker_runtime.types.enable_explanations_header
    import capo_sagemaker_runtime.types.endpoint_name
    import capo_sagemaker_runtime.types.header
    import capo_sagemaker_runtime.types.inference_component_header
    import capo_sagemaker_runtime.types.inference_id
    import capo_sagemaker_runtime.types.prefix_aware_id_header
    import capo_sagemaker_runtime.types.session_id_or_new_session_constant_header
    import capo_sagemaker_runtime.types.target_container_hostname_header
    import capo_sagemaker_runtime.types.target_model_header
    import capo_sagemaker_runtime.types.target_variant_header


class InvokeEndpointInput(TypedDict, closed=True):
    endpoint_name: "capo_sagemaker_runtime.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint that you specified when you created the endpoint using the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html">CreateEndpoint</a> API.</p>"""
    body: NotRequired["capo_sagemaker_runtime.types.body_blob.BodyBlob"]
    """<p>Provides input data, in the format specified in the <code>ContentType</code> request header. Amazon SageMaker AI passes all of the data in the body to the model. </p> <p>For information about the format of the request body, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html">Common Data Formats-Inference</a>.</p>"""
    content_type: NotRequired["capo_sagemaker_runtime.types.header.Header"]
    """<p>The MIME type of the input data in the request body.</p>"""
    accept: NotRequired["capo_sagemaker_runtime.types.header.Header"]
    """<p>The desired MIME type of the inference response from the model container.</p>"""
    custom_attributes: NotRequired[
        "capo_sagemaker_runtime.types.custom_attributes_header.CustomAttributesHeader"
    ]
    """<p>Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in <a href="https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6">Section 3.3.6. Field Value Components</a> of the Hypertext Transfer Protocol (HTTP/1.1). </p> <p>The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with <code>Trace ID:</code> in your post-processing function. </p> <p>This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker AI Python SDK. </p>"""
    target_model: NotRequired[
        "capo_sagemaker_runtime.types.target_model_header.TargetModelHeader"
    ]
    """<p>The model to request for inference when invoking a multi-model endpoint.</p>"""
    target_variant: NotRequired[
        "capo_sagemaker_runtime.types.target_variant_header.TargetVariantHeader"
    ]
    """<p>Specify the production variant to send the inference request to when invoking an endpoint that is running two or more variants. Note that this parameter overrides the default behavior for the endpoint, which is to distribute the invocation traffic based on the variant weights.</p> <p>For information about how to use variant targeting to perform a/b testing, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html">Test models in production</a> </p>"""
    target_container_hostname: NotRequired[
        "capo_sagemaker_runtime.types.target_container_hostname_header.TargetContainerHostnameHeader"
    ]
    """<p>If the endpoint hosts multiple containers and is configured to use direct invocation, this parameter specifies the host name of the container to invoke.</p>"""
    inference_id: NotRequired["capo_sagemaker_runtime.types.inference_id.InferenceId"]
    """<p>If you provide a value, it is added to the captured data when you enable data capture on the endpoint. For information about data capture, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html">Capture Data</a>.</p>"""
    enable_explanations: NotRequired[
        "capo_sagemaker_runtime.types.enable_explanations_header.EnableExplanationsHeader"
    ]
    """<p>An optional JMESPath expression used to override the <code>EnableExplanations</code> parameter of the <code>ClarifyExplainerConfig</code> API. See the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable">EnableExplanations</a> section in the developer guide for more information. </p>"""
    inference_component_name: NotRequired[
        "capo_sagemaker_runtime.types.inference_component_header.InferenceComponentHeader"
    ]
    """<p>If the endpoint hosts one or more inference components, this parameter specifies the name of inference component to invoke.</p>"""
    session_id: NotRequired[
        "capo_sagemaker_runtime.types.session_id_or_new_session_constant_header.SessionIdOrNewSessionConstantHeader"
    ]
    """<p>Creates a stateful session or identifies an existing one. You can do one of the following:</p> <ul> <li> <p>Create a stateful session by specifying the value <code>NEW_SESSION</code>.</p> </li> <li> <p>Send your request to an existing stateful session by specifying the ID of that session.</p> </li> </ul> <p>With a stateful session, you can send multiple requests to a stateful model. When you create a session with a stateful model, the model must create the session ID and set the expiration time. The model must also provide that information in the response to your request. You can get the ID and timestamp from the <code>NewSessionId</code> response parameter. For any subsequent request where you specify that session ID, SageMaker AI routes the request to the same instance that supports the session.</p>"""
    prefix_aware_id: NotRequired[
        "capo_sagemaker_runtime.types.prefix_aware_id_header.PrefixAwareIdHeader"
    ]
    """<p>An optional, stable identifier that serves as a routing hint for prefix-aware routing. The service routes requests with the same prefix and the same identifier to the same instance. If requests from different applications might have the same prompt prefix, set a different identifier for each application to differentiate their routing decisions.</p> <p>Applies only to endpoints configured with a <code>RoutingStrategy</code> of <code>PREFIX_AWARE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeEndpointInput) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_sagemaker_runtime.types.body_blob

        out["Body"] = capo_sagemaker_runtime.types.body_blob.serialize_json(
            value["body"]
        )
    return out


def deserialize_json(data: dict) -> InvokeEndpointInput:
    out: InvokeEndpointInput = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_sagemaker_runtime.types.body_blob

        out["body"] = capo_sagemaker_runtime.types.body_blob.deserialize_json(
            data["Body"]
        )
    return out

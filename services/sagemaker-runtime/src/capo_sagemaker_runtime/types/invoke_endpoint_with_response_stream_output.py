"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointWithResponseStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_runtime.types.custom_attributes_header
    import capo_sagemaker_runtime.types.header
    import capo_sagemaker_runtime.types.response_stream


class InvokeEndpointWithResponseStreamOutput(TypedDict, closed=True):
    body: "capo_sagemaker_runtime.types.response_stream.ResponseStream"
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

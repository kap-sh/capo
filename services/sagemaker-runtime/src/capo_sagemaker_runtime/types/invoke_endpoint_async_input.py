"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointAsyncInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_runtime.types.async_body_blob
    import capo_sagemaker_runtime.types.custom_attributes_header
    import capo_sagemaker_runtime.types.endpoint_name
    import capo_sagemaker_runtime.types.filename_header
    import capo_sagemaker_runtime.types.header
    import capo_sagemaker_runtime.types.inference_id
    import capo_sagemaker_runtime.types.input_location_header
    import capo_sagemaker_runtime.types.invocation_timeout_seconds_header
    import capo_sagemaker_runtime.types.request_ttl_seconds_header
    import capo_sagemaker_runtime.types.s3_output_path_extension_header


class InvokeEndpointAsyncInput(TypedDict, closed=True):
    endpoint_name: "capo_sagemaker_runtime.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint that you specified when you created the endpoint using the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html">CreateEndpoint</a> API.</p>"""
    content_type: NotRequired["capo_sagemaker_runtime.types.header.Header"]
    """<p>The MIME type of the input data in the request body.</p>"""
    accept: NotRequired["capo_sagemaker_runtime.types.header.Header"]
    """<p>The desired MIME type of the inference response from the model container.</p>"""
    custom_attributes: NotRequired[
        "capo_sagemaker_runtime.types.custom_attributes_header.CustomAttributesHeader"
    ]
    """<p>Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in <a href="https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6">Section 3.3.6. Field Value Components</a> of the Hypertext Transfer Protocol (HTTP/1.1). </p> <p>The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with <code>Trace ID:</code> in your post-processing function. </p> <p>This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker AI Python SDK. </p>"""
    inference_id: NotRequired["capo_sagemaker_runtime.types.inference_id.InferenceId"]
    """<p>The identifier for the inference request. Amazon SageMaker AI will generate an identifier for you if none is specified. </p>"""
    input_location: NotRequired[
        "capo_sagemaker_runtime.types.input_location_header.InputLocationHeader"
    ]
    """<p>The Amazon S3 URI where the inference request payload is stored.</p>"""
    s3_output_path_extension: NotRequired[
        "capo_sagemaker_runtime.types.s3_output_path_extension_header.S3OutputPathExtensionHeader"
    ]
    """<p>The path extension that is appended to the Amazon S3 output path where the inference response payload is stored.</p>"""
    filename: NotRequired["capo_sagemaker_runtime.types.filename_header.FilenameHeader"]
    """<p>The filename for the inference response payload stored in Amazon S3. If not specified, Amazon SageMaker AI generates a filename based on the inference ID.</p>"""
    request_ttl_seconds: NotRequired[
        "capo_sagemaker_runtime.types.request_ttl_seconds_header.RequestTTLSecondsHeader"
    ]
    """<p>Maximum age in seconds a request can be in the queue before it is marked as expired. The default is 6 hours, or 21,600 seconds.</p>"""
    invocation_timeout_seconds: NotRequired[
        "capo_sagemaker_runtime.types.invocation_timeout_seconds_header.InvocationTimeoutSecondsHeader"
    ]
    """<p>Maximum amount of time in seconds a request can be processed before it is marked as expired. The default is 15 minutes, or 900 seconds.</p>"""
    body: NotRequired["capo_sagemaker_runtime.types.async_body_blob.AsyncBodyBlob"]
    """<p>Provides inline input data for the inference request, in the format specified in the <code>ContentType</code> request header. Use this parameter to send the request payload directly in the API call instead of uploading it to Amazon S3 and referencing it with <code>InputLocation</code>. The inline payload can be up to 128,000 bytes.</p> <p> <code>Body</code> and <code>InputLocation</code> are mutually exclusive. Provide exactly one of them.</p> <p>For information about the format of the request body, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html">Common Data Formats-Inference</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeEndpointAsyncInput) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_sagemaker_runtime.types.async_body_blob

        out["Body"] = capo_sagemaker_runtime.types.async_body_blob.serialize_json(
            value["body"]
        )
    return out


def deserialize_json(data: dict) -> InvokeEndpointAsyncInput:
    out: InvokeEndpointAsyncInput = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_sagemaker_runtime.types.async_body_blob

        out["body"] = capo_sagemaker_runtime.types.async_body_blob.deserialize_json(
            data["Body"]
        )
    return out
